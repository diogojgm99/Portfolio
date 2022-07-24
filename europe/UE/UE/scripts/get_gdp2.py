from europe.models import Country, GDP
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#usd to eur - 0.96040213
def get_years(df):
    years=[]
    for i in range(2,len(df)):
        years.append(df[i])
    return years

try:
    df = pd.read_csv("/home/diogo/Portfolio/europe/UE/UE/scripts/data/new_gdp.csv")
    years = get_years(df.columns)
    for index, row in df.iterrows():
        country = Country.objects.get(name=row[0])
        country.sigla = row[1]
        country.save()
        for year in years:
            datacell = int(df.loc[index][year] * 0.96040213)
            print("{} - {}".format(year,datacell))
            new_gdp, created = GDP.objects.get_or_create(
                country = country,
                year = year,
                gdp = datacell
            )
            new_gdp.save()
except Exception as e:
    logger.info("exception: {}".format(e))