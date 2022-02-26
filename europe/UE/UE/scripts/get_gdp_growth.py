from europe.models import Country,GDP_Growth
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_years(df):
    years=[]
    for i in range(4,len(df)):
        years.append(df[i])
    logger.info(years)
    return years

try:
    df = pd.read_csv("UE/scripts/data/gdp_growth.csv",sep=',')
    logger.info(df)
    years = get_years(df.columns)
    for index, row in df.iterrows():
        country = Country.objects.get(name=row[0])
        logger.info(country)
        for year in years:
            datacell = df.loc[index][year]
            logger.info("{} - {}".format(year,round(datacell, 2)))
            new_gdp = GDP_Growth(
                country = country,
                year = year,
                gdp_growth = round(datacell, 2)
            )
            new_gdp.save()

except Exception as e:
    logger.info("exception: {}".format(e))