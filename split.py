from webbrowser import get
import pandas as pd;
import os;

bigfilepath =r'C:\projects\docs\SalesRecord.csv'
PartNum =10
OutputPath =r'C:\projects\docs\output\\'

with open(bigfilepath) as fp:
    for (count, _) in enumerate(fp, 1):
       pass

print(count)
ChunkSizePart = (count)//PartNum
print(ChunkSizePart)
for i,chunk in enumerate(pd.read_csv(bigfilepath, chunksize=ChunkSizePart)):
    chunk.to_csv(OutputPath+'chunk{}.csv'.format(i), index=False)

