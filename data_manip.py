import geopandas as gpd
import pandas as pd
import reverse_geocoder as rg

# Set filepath
fp = "data/Meijer2021_midpoint_emissions.shp"

# Read file using gpd.read_file()
data = gpd.read_file(fp)

data['lon'] = data["geometry"].x
data['lat'] = data.geometry.y

country_codes_key = pd.read_csv('Country Codes - Sheet1.csv')
print(country_codes_key.head())


# Python3 program for reverse geocoding.

def reverse_geocode(coord):

    result = rg.search(coord)
    # result is a list containing ordered dictionary.
    return result


# Driver function
if __name__ == "__main__":
    # Coordinates tuple.Can contain more than one pair.
    coordinates = []
    for i in range(len(data["lon"])):
        coordinates.append((data["lat"].loc[i], data["lon"].loc[i]))
    print(coordinates[:5])
    output = reverse_geocode(coordinates)
    country_code = pd.DataFrame(output)
    data["Alpha-2 code"] = country_code["cc"]
    data = pd.merge(data, country_codes_key, on="Alpha-2 code", how="left" )
    # data.to_csv("country_data.csv")



