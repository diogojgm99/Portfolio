import csv
import pandas as pd
import numpy as np 
import math
from country_data import chile_data, china_data, germany_data,mex_data,usa_data,zim_data
import matplotlib.pyplot as plt

class Country:
    def __init__(self, year, life,gdp):
        self.year = year
        self.life = life
        self.gdp = gdp
    
    def average_gdp(self):
        total_gdp = sum(self.gdp)
        average = total_gdp/len(self.gdp)
    
        return average
    
    def graph_life(self):
        x = self.year
        y = self.life
        plt.scatter(x,y)
        plt.xlabel('Year')
        plt.ylabel('Life expectancy (Years)')
        plt.title('Life expectancy')
        plt.legend()
        plt.show()
    
    def graph_gdp(self):
        x = self.year
        y = self.gdp
        
        plt.bar(x,y)
        plt.xlabel('Year')
        plt.ylabel('Gdp in dollars')
        plt.title('Gdp')
        plt.legend()
        plt.show()
    
    def get_gdp_by_year(self, ano):
        for i in range(len(self.year)):
            if self.year[i] == ano:
                return self.gdp[i]
    
    def get_life_by_year(self, ano):
        for i in range(len(self.year)):
            if self.year[i] == ano:
                return self.life[i]

#######
# Reading file and put csv file data in differents arrays
def reading_file(filename):
    countries = []
    year = []
    life = []
    gdp = []
    with open('all_data.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            countries.append(row[0])
            year.append(row[1])
            life.append(row[2])
            gdp.append(row[3])
    countries.pop(0)
    year.pop(0)
    life.pop(0)
    gdp.pop(0)
    return countries, year, life, gdp

def all_gdp_graph():
    gdp_list = [chile.average_gdp(),china.average_gdp(),germany.average_gdp(),mexico.average_gdp(),usa.average_gdp(),zimbabwe.average_gdp()]
    cnts = ['Chile','China','Germany','Mexico','USA','Zimbabwe']
    print(gdp_list)

    plt.bar(cnts,gdp_list)
    plt.xlabel('country')
    plt.ylabel("average gdp")
    plt.title('GDP by country')
    plt.legend()
    plt.show()

countries, year, life, gdp = reading_file('all_data.csv')


while(True):
    print("For exit insert q")
    choice = input("Choose one of these countries: Chile, China, Germany, Mexico , USA and Zimbabwe: \n")

    if choice == 'Chile':
        chile_year, chile_life, chile_gdp = chile_data(countries, year, life, gdp)
        chile = Country (chile_year, chile_life, chile_gdp)
        selected_country = chile

    elif choice == 'China':
        china_year, china_life, china_gdp = china_data(countries, year, life, gdp)
        china = Country (china_year, china_life, china_gdp)
        selected_country = china

    elif choice == 'Germany':
        ger_year, ger_life, ger_gdp = germany_data(countries, year, life, gdp)
        germany = Country (ger_year, ger_life, ger_gdp)
        selected_country = germany

    elif choice == 'Mexico':
        mex_year, mex_life, mex_gdp = mex_data(countries, year, life, gdp)
        mexico = Country (mex_year, mex_life, mex_gdp)
        selected_country = mexico

    elif choice == 'USA':
        usa_year, usa_life, usa_gdp = usa_data(countries, year, life, gdp)
        usa = Country (usa_year, usa_life, usa_gdp)
        selected_country = usa

    elif choice == 'Zimbabwe':
        zim_year, zim_life, zim_gdp = zim_data(countries, year, life, gdp)
        zimbabwe = Country (zim_year, zim_life, zim_gdp)
        selected_country = zimbabwe

    elif choice == 'q':
        break
    else:
        print("Insert a valid country or lookout for syntax. Ignore next stage")
        
    while True:
        print("Press b to back to previous menu")
        option = input("1- Graph of GDP \n 2-Graph of Life Expectancy \n 3- Average of GDP \n 4-GDP in selected year \n 5- Life Expectancy in selected year \n")
        
        if option == '1':
            selected_country.graph_gdp()

        elif option == '2':
            selected_country.graph_life()

        elif option == '3':
            print(selected_country.average_gdp())
        
        elif option == '4':
            date = int(input("Select year (2010-2015): "))
            print(selected_country.get_gdp_by_year(date))

        elif option == '5':
            date = int(input("Select year (2010-2015): "))
            print(selected_country.get_life_by_year(date))
        elif option == 'b':
            break

