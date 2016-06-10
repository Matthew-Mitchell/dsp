import csv
emailist=[]

with open('faculty.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        emailist.append(row[' email'])
        
with open('emails.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(emailist)
