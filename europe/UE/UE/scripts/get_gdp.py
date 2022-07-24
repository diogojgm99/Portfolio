from europe.models import Country, GDP
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#usd to eur - 0.96040213

def get_years(df):
    years=[]
    for i in range(4,len(df)):
        years.append(df[i])
    logger.info(years)
    return years

try:
    df = pd.read_csv("UE/scripts/data/gdp.csv",sep=',')
    logger.info(df)
    years = get_years(df.columns)
    for index, row in df.iterrows():
        country = Country.objects.get(name=row[0])
        logger.info(country)
        for year in years:
            datacell = df.loc[index][year]
            logger.info("{} - {}".format(year,datacell))
            new_gdp = GDP(
                country = country,
                year = year,
                gdp = datacell
            )
            new_gdp.save()

except Exception as e:
    logger.info("exception: {}".format(e.message))