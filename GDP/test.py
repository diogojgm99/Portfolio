import pandas as pd
import csv

def gdp_over_years(reader,country,first_year,last_year):
    i=1
    for row in reader:
        #print(row[str(1960)])
        if country == row['Country Name']:
            print(row[str(first_year)])
            print(row[str(last_year)])
        i+=1


#reading CSV file
with open('data1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    gdp_over_years(reader,'Belize',1960,1965)