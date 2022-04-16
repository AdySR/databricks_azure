# import pandas as pd;

# df1 = pd.read_csv(r'C:\projects\docs\cars (1).csv')
# df2 = pd.read_csv(r'C:\projects\docs\cars (2).csv')
# df3 = pd.read_csv(r'C:\projects\docs\cars (3).csv')
# df4 = pd.read_csv(r'C:\projects\docs\cars (4).csv')

# result_set = pd.concat((df1,df2,df3,df4), ignore_index=True)
# # print(df3)
# print(result_set)



########################################################################
########################################################################
########################################################################

# import pandas as pd;
# from glob import glob;

# path =r'C:\projects\docs'

# all_files = glob(path+'\car*.csv')
# # init a list variable to contain comma sep DFs
# li = []

# for f in all_files:
#     df = pd.read_csv(f,header=0,index_col=None)
#     li.append(df)


# result_set = pd.concat((li), ignore_index=True)

# result_set.to_csv(r'C:\projects\docs\result.csv')
# # print(result_set)

########################################################################
########################################################################
########################################################################

# import pandas as pd;
# from glob import glob;
# all_files = glob(r'C:\projects\docs\cars*.csv')
# car_final_result = pd.concat((pd.read_csv(file) for file in all_files), ignore_index=True)
# print(car_final_result)

########################################################################
########################################################################
########################################################################
