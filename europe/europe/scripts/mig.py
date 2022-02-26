from countries.models import Country

countries = Country.objects.all()
list_countries=[]
for cnt in countries:
    list_countries.append({
        'name': cnt.name,
        'abbreviation': cnt.sigla,
        'population': cnt.population,
        'currency': cnt.currency
    })
print(list_countries)