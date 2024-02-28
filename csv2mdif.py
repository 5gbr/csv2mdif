import csv
import sys

if (len(sys.argv) == 1):
    print('usage: '+sys.argv[0]+' csv_in.csv mdif_out.mdif')
    sys.exit()

with open(sys.argv[1], newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    with open(sys.argv[2], 'w', newline='') as outtxt:
        writer = csv.writer(outtxt, delimiter=' ')
        for i, row in enumerate(reader):
            row.insert(0, i)
            writer.writerow(row)