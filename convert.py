import csv
import time
from datetime import datetime

with open('data/old-data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(round(int(row[0])) / 1000))
            print(f'\t{row[0]} is the time  {row[1]}')
            WriteData = open("data-old/"+time.strftime("%Y-%m-%d", time.localtime(round(int(row[0])) / 1000))+"-count.csv", "a")   
            WriteData.write(row[1]+","+ now +"\n")
            WriteData.close()
            line_count += 1
    print(f'Processed {line_count} lines.')