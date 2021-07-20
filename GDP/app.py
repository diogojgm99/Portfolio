from os import read
import pandas as pd
import csv

def gdp_over_years(reader,country,first_year,last_year):
    year = first_year
    for row in reader:
        if country == row['Country Name']:
            while (year <= last_year):
                print(f'{str(year)} : {row[str(year)]}')
                year +=1;
                


if __name__ == "__main__":
    #reading CSV file
    with open('data1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # gdp_over_years(reader,'Belize',1960,1965)
        while True:
            country = input("Insert the selected country: ")
            print(country)
            initial_year = int(input("Insert the initial year: "))
            print(initial_year)
            final_year = int(input("Insert the initial year: "))
            print(final_year)
            gdp_over_years(reader,country,initial_year,final_year)
            break

        