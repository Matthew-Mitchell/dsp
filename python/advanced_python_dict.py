#Question 6
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
for x in range(0,3):
    print directory.keys()[x],directory.values()[x]



#Question 7
import csv
import re
directory=dict()
rowdata=[]

with open('faculty.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        rowdata.append(row)
for row in rowdata[1:]:
    firstlast=row[0].split()[0],row[0].split()[-1]
    try:
        directory[firstlast]=directory.get(firstlast)+[row[1:]]
    except:
        directory[firstlast]=[row[1:]]
for x in range(0,3):
    print directory.keys()[x],directory.values()[x]


#Q8
import csv
import re
directory=dict()
rowdata=[]

with open('faculty.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        rowdata.append(row)
for row in rowdata[1:]:
    firstlast=row[0].split()[0],row[0].split()[-1]
    try:
        directory[firstlast]=directory.get(firstlast)+[row[1:]]
    except:
        directory[firstlast]=[row[1:]]
directorykeys=sorted(directory.keys(),key=lambda x: x[-1])
directoryvalues=[directory[x] for x in directorysort]
directorybook=zip(directorykeys,directoryvalues)
for person in directorybook:
    print(person)
#Written in Python 3; to convert to Python 2 change 2nd argument ins open from newline='' to 'rb'
