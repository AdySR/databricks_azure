###Final code####
##input Parameter
config_path = '/dbfs/FileStore/tables/oss/pyspark_config_teamc.ini'
regex = '.*yellow_trip_taxi_\d{8}\.csv$'
#regex='.*sample\d+\.json$'
#regex = '.*userdata\d+\.parquet$'
date_format= 'current_date'
#date_format= 'period'
#date_format= 'current_week'

#### Function Body
def get_df_qualified_files(var_config_path,regex,date_format):
    import pyspark ;
    from pyspark.sql import SparkSession;
    import os;
    from datetime import date,datetime, timedelta;
    from configparser import ConfigParser;
    import re;
    ## Assign values
    spark = SparkSession.builder.appName('TeamC').master('master').getOrCreate()
    ini_parser = ConfigParser()
    ini_parser.read(var_config_path)
    pass_hours =int(ini_parser.get('FILE_OSS','pass_hours'))
    path = ini_parser.get('FILE_OSS','path')
    lookback_period = datetime.now() - timedelta(hours =pass_hours)
    today = date.today()
    now = datetime.now()
    now_day_1 = now - timedelta(days=now.weekday()) ##first date of current week
    
    ## extract date modified and pick the latest files based on hour/ current week/ current date
    files_at_path= [path+"/"+fd for fd in os.listdir(path)]
    qualified_files =[];
    pattern = re.compile(r''+regex+'')
    
    for file in files_at_path:
        get_stats = os.stat(file)
        file_last_modified_date = datetime.fromtimestamp(get_stats.st_mtime)
        get_file_last_modified_date_short = date.fromtimestamp(get_stats.st_mtime)
        
        if date_format=='period':
            if (file_last_modified_date >= lookback_period ):
                file = file.replace('/dbfs','')
                qualified_files.append(file)
                qualified_files = [s for s in qualified_files if pattern.match(s)]
        elif date_format=='current_date':
            if (get_file_last_modified_date_short == today):
                file = file.replace('/dbfs','')
                qualified_files.append(file)
                qualified_files = [s for s in qualified_files if pattern.match(s)]
        elif date_format=='current_week':
            if (file_last_modified_date >= now_day_1):
                file = file.replace('/dbfs','')
                qualified_files.append(file)
                qualified_files = [s for s in qualified_files if pattern.match(s)]
    ##check for file extension and read the files   
    if qualified_files!=[]:
        extension = os.path.splitext(qualified_files[0])[1][1:]
        print(extension)
        out_df_files= spark.read.format(r''+extension+'').option("header","true").load(qualified_files);
    else:
        out_df_files= spark.sparkContext.emptyRDD();
        print('No files present');
        
    return out_df_files;

## call function
df = get_df_qualified_files(config_path,regex,date_format)

df.show()
