#######
#separate data by countries

def chile_data(countries, year, life, gdp):
    chile_year = []
    chile_life = []
    chile_gdp = []

    for i in range(len(countries)):
        if countries[i] == 'Chile':
            chile_year.append(int(year[i]))
            chile_life.append(float(life[i]))
            chile_gdp.append(float(gdp[i]))
    return chile_year, chile_life, chile_gdp

def china_data(countries, year, life, gdp):
    china_year = []
    china_life = []
    china_gdp = []

    for i in range(len(countries)):
        if countries[i] == 'China':
            china_year.append(int(year[i]))
            china_life.append(float(life[i]))
            china_gdp.append(float(gdp[i]))
            
    return china_year, china_life, china_gdp

def germany_data(countries, year, life, gdp):
    germany_year = []
    germany_life = []
    germany_gdp = []

    for i in range(len(countries)):
        if countries[i] == 'Germany':
            germany_year.append(int(year[i]))
            germany_life.append(float(life[i]))
            germany_gdp.append(float(gdp[i]))

    return germany_year, germany_life, germany_gdp

def mex_data(countries, year, life, gdp):
    mex_year = []
    mex_life = []
    mex_gdp = []

    for i in range(len(countries)):
        if countries[i] == 'Mexico':
            mex_year.append(int(year[i]))
            mex_life.append(float(life[i]))
            mex_gdp.append(float(gdp[i]))
    return mex_year, mex_life, mex_gdp

def usa_data(countries, year, life, gdp):
    usa_year = []
    usa_life = []
    usa_gdp = []

    for i in range(len(countries)):
        if countries[i] == 'United States of America':
            usa_year.append(int(year[i]))
            usa_life.append(float(life[i]))
            usa_gdp.append(float(gdp[i]))

    return usa_year, usa_life, usa_gdp

def zim_data(countries, year, life, gdp):
    zim_year = []
    zim_life = []
    zim_gdp = []

    for i in range(len(countries)):
        if countries[i] == 'Zimbabwe':
            zim_year.append(int(year[i]))
            zim_life.append(float(life[i]))
            zim_gdp.append(float(gdp[i]))

    return zim_year, zim_life, zim_gdp