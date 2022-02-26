from countries.models import Country
from economy.models import GDP_per_capita, GDP
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_years(df):
    years=[]
    for i in range(1,len(df)):
        years.append(df[i])
    return years

print("get_data")
countries = list(Country.objects.all().values_list("sigla",flat=True))
logger.info(countries)

try:
    df = pd.read_csv("scripts/data/sdg_10_10.tsv",sep='\t')
    years = get_years(df.columns)
    # logger.info(df)
    for index, row in df.iterrows():
        if row[0] in countries:
            # logger.info(df['2000'].values[1])
            country = Country.objects.get(sigla = row[0])
            logger.info(country)
            for i in range(1,len(years)+1):
                datacell = df.loc[index][i]
                logger.info("{} - {}".format(years[i-1],datacell))

                new_gdp = GDP_per_capita(
                    country = country,
                    year = years[i-1],
                    gdp_per_capita = datacell
                )
                new_gdp.save()
except Exception as e:
    logger.info("exception {}".format(e))

