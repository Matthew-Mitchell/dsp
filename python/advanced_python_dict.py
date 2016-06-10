import csv
import re
directory=dict()
rowdata=[]

with open('faculty.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        rowdata.append(row)
for row in rowdata[1:]:
    try:
        directory[row[0].split()[-1]]=directory.get(row[0].split()[-1])+[row[1:]]
    except:
        directory[row[0].split()[-1]]=[row[1:]]
print(directory)
#Written in Python 3; to convert to Python 2 change 2nd argument ins open from newline='' to 'rb'
