import csv
# csv file
with open('/Users/patrickvargos/Documents/codingnomads/Week_08/twitter_ticker/project/tweet_find/companylist.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
# print(mydict)
# print(mydict['MSFT'])
queryform = 'MSFT'
query = mydict[queryform]

print(query)
