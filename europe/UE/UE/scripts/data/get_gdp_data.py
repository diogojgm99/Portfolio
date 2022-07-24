import pandas as pd
from europe.models import *
import logging
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

df = pd.read_csv("UE/scripts/data/gdp_data.csv",sep=',')
columns = list(df.columns)
years_list=[]
data_value = {}
for index in range(len(df.index)):
    for index_columns in range(len(columns)):
        if columns[index_columns] == "Country Code":
            country = df.loc[index][index_columns]
        elif columns[index_columns] == "Series Name":
            report = df.loc[index][index_columns]
        else:
            year = columns[index_columns]
            years_list.append(year)
            if df.loc[index][index_columns] == "None":
                data_value[year] = ""
            else:
                data_value[year] = df.loc[index][index_columns]

    country_obj = Country.objects.get(code=country)
    report_obj = Report.objects.get(name=report)
    for year in years_list:
        new_report = Data_report(
            country=country_obj,
            report=report_obj,
            year = int(year)
        )
        try:
            value = float(data_value[year])
            new_report.value = value
        except:
            print("empty value")

        new_report.save()

    years_list=[]