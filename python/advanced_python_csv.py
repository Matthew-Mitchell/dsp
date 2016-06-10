import csv
emailist=[]

with open('faculty.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        emailist.append(row[' email'])
        
with open('emails.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
    for row in emailist:
        writer.writerow(row)
