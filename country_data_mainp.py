import pandas as pd

data = pd.read_csv("countries of the world.csv")
country_codes_key = pd.read_csv('Country Codes - Sheet1.csv')

data["Country"] = data["Country"].str.strip(" ")

data = pd.merge(data, country_codes_key, on="Country", how="left")

river_data = pd.read_csv("country_data.csv")
river_data = river_data.groupby(["Alpha-3 code", "Country", "Alpha-2 code"])['dots_exten'].agg(['sum', 'count'])
river_data = river_data.reset_index()
print(river_data.head())

dataset = pd.merge(river_data, data, on="Alpha-3 code", how="left")
print(dataset.info())
dataset = dataset.drop(["Alpha-2 code_y"], axis=1)
dataset["plastic poll"] = dataset["sum"]
dataset["no. rivers"] = dataset["count"]
dataset.drop(labels=["Numeric", "sum", "count"], axis=1, inplace=True)

# print(dataset.head())
print(dataset.info())


def string_converter(string):
    dec = string.str.replace(",", ".")
    pd.to_numeric(dec)
    return dec


dataset[['Pop. Density (per sq. mi.)',
         'Coastline (coast/area ratio)', 'Net migration',
         'Infant mortality (per 1000 births)', 'Industry', 'Service',
         'Literacy (%)', 'Phones (per 1000)', 'Arable (%)', 'Crops (%)',
         'Other (%)', 'Climate', 'Birthrate', 'Deathrate', 'Agriculture']] = dataset[['Pop. Density (per sq. mi.)',
       'Coastline (coast/area ratio)', 'Net migration',
       'Infant mortality (per 1000 births)','Industry', 'Service',
       'Literacy (%)', 'Phones (per 1000)', 'Arable (%)', 'Crops (%)',
       'Other (%)', 'Climate', 'Birthrate', 'Deathrate', 'Agriculture']].apply(string_converter, axis=1)

dataset.to_csv("data_for_analysis")
