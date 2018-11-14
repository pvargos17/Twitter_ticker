import csv

# csv file
with open('companylist.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}

print(mydict['MSFT'])


