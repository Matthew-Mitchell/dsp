import csv
d=dict()
with open('faculty.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        row[1]=row[1].strip()
        degrees=row[1].split()
        for degree in degrees:
            degree=degree.replace(".","")
            d[degree]=d.get(degree,0)+1
print d


#Need an alternative method for dealing with multiple degrees.
#Multiple for loops are to be avoided.
#Current thoughts: which csv read method will be best?
#Should I incorporate regular expressions or simply reformat using string methods?
