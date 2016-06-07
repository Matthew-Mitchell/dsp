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
