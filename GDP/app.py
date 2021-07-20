import pandas as pd
import csv

with open('data1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row[str(1960)])
