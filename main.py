import pandas as pd

river_data = pd.read_csv("country_data.csv")
print(river_data[river_data["Country"] == "Myanmar"].sort_values(by="dots_exten").tail(15))
print(river_data[river_data["Country"] == "Myanmar"].dots_exten.sum())