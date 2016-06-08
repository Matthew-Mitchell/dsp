import csv
import re
count_title=dict()
emailist=[]
domainlist=[]
domaincount=dict()
count_degrees=dict()

with open('faculty.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row[' degree']=row[' degree'].strip()
        row[' degree']=row[' degree'].replace(".","")
        degreelist=row[' degree'].split(" ")
        count_title[(row[' title'])]=count_title.get(row[' title'],0)+1
        for degree in degreelist:
            count_degrees[degree]=count_degrees.get(degree,0)+1
        emailist.append(row[' email'])
        
print "Q1:\n\n", count_degrees, "\n\n"        
print "Q2:\n\n", count_title, "\n\n"
print "Q3:\n\n", emailist, "\n\n"


for address in emailist:
    domainlist.append(re.findall('@(\S+)', address))

for domain in domainlist:
    domain=str(domain)
    domaincount[domain]=domaincount.get(domain,0)+1
print "Q4:\n\n", domaincount
