from os import read
import pandas as pd
import csv
import time
import matplotlib.pyplot as plt
import numpy as np

def see_countries():
    with open('data1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Country Name'])
        csvfile.close()

def gdp_over_years(country,first_year,last_year):
    with open('data1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        year = first_year
        years=[]
        gdp=[]
        for row in reader:
            if country == row['Country Name']:
                while (year <= last_year):
                    print(f'{str(year)} : {row[str(year)]}')
                    gdp.append(int(float(row[str(year)])))
                    years.append(year)
                    year +=1
        csvfile.close()
    if len(gdp) == 0:
        print("Country/Region not found. Check list to see available countries or regions.")
        return False
    plt.plot(years, gdp)
    plt.axis([years[0],years[-1],min(gdp),max(gdp)])
    plt.show()
                
def gdp_all_years(country):
    with open('data1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        year=1960
        years =[]
        gdp=[]
        for row in reader:
            if country == row['Country Name']:
                while (year <= 2020):
                    print(f'{str(year)} : {row[str(year)]}')
                    gdp.append(int(float(row[str(year)])))
                    years.append(year)
                    year +=1
        csvfile.close()
    if len(gdp) == 0:
        print("Country/Region not found. Check list to see available countries or regions.")
        return False
    plt.plot(years, gdp)
    plt.axis([years[0],years[-1],min(gdp),max(gdp)])
    plt.show()
    
def gdp_year(country, year):
    with open('data1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if country == row['Country Name']:
                print(f'{str(year)} : {row[str(year)]}')
        csvfile.close()

def gdp_two_countries(country1,country2):
    with open('data1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        years1,years2 = [],[]
        gdp1,gdp2 = [],[]
        for row in reader:
            year=1960
            if country1 == row['Country Name']:
                print('\n'+country1+'\n')
                while (year <= 2020):
                    print(f'{str(year)} : {row[str(year)]}')
                    gdp1.append(int(float(row[str(year)])))
                    years1.append(year)
                    year +=1
            year=1960
            if country2 == row['Country Name']:
                print('\n'+country2+'\n')
                while (year <= 2020):
                    print(f'{str(year)} : {row[str(year)]}')
                    gdp2.append(int(float(row[str(year)])))
                    years2.append(year)
                    year +=1
        csvfile.close()
    # plt.plot(years1, gdp1)
    # plt.plot(years2, gdp2)
    # plt.show()
    fig,ax = plt.subplots()
    ax.plot(years1, gdp1, color="red")
    ax.set_xlabel("year")
    ax.set_ylabel(country1)

    ax2=ax.twinx()
    ax2.plot(years2, gdp2, color="blue")
    ax2.set_ylabel(country2)
    plt.show()


if __name__ == "__main__":
    while True:
        print('-----------------------------------------')
        print('--   GROSS DOMESTIC PRODUT 1960-2020   --')
        print('-----------------------------------------')
        print('1 - See all Countries and Regions.')
        print('2 - See GDP of one country/region between 1960-2020.')
        print('3 - See GDP of one country/region between a choosen interval.')
        print('4 - See GDP of one country/regions in a specific year.')
        print('5 - Compare GDP of two countries/regions between 1960 2020.')
        print('e - Exit')
        choose = input('Choose one of the options above: ')

        if choose == '1':
            see_countries()
            
        elif choose == '2':
            country = input("Insert the selected country: ")
            print(country)
            gdp_all_years(country)

        elif choose == '3':
            country = input("Insert the selected country: ")
            print(country)
            initial_year = int(input("Insert the initial year: "))
            print(initial_year)
            final_year = int(input("Insert the final year: "))
            print(final_year)
            gdp_over_years(country,initial_year,final_year)

        elif choose == '4':
            country = input("Insert the selected country: ")
            print(country)
            year = int(input("Insert the year: "))
            print(year)
            gdp_year(country,year)

        elif choose == '5':
            country1 = input("Insert the first country: ")
            country2 = input("Insert the second country: ")
            print(country1 + ' '+ country2)
            gdp_two_countries(country1, country2)
        elif choose == 'e':
            break
        

        