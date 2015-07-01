import csv

with open('data/corpus.csv', 'rU') as f:
  reader = csv.reader(f, delimiter=",")
  for row in reader:
    f = open('data/output/' + str(row[0]) + '.txt', 'w')
    f.write(row[1].decode('ascii', 'ignore'))
    f.close()