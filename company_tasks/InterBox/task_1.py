# TO DO: It is necessary to implement a class that will interact with a third-party API: API (https://restcountries.com) 
# The class must receive data from the API and then return it to the console in tabular form, namely the following data: 
# the name of the country, the name of the capital and a link to the image of the flag in png format.

import requests
from tabulate import tabulate

class CountryInfo:
    def __init__(self):
        self.api_url = "https://restcountries.com/v3.1/all"

    def fetch_countries_data(self):
        response = requests.get(self.api_url)
        response.raise_for_status()
        return response.json()
    
    def get_country_info(self) -> list:
        countries_data = self.fetch_countries_data()
        country_info_list = []
        for country in countries_data:
            name = country.get("name", {}).get("common", "N/A")
            capital = country.get("capital", [])[0] if country.get("capital") else "N/A" 
            flags = country.get("flags", {}).get("png", "N/A")
            country_info_list.append([name, capital, flags])

        return country_info_list
    
    def display_country_info(self) -> None:
        country_info_table = self.get_country_info()
        print(tabulate(country_info_table, headers=["Name", "Capital", "Flags"]))


if __name__ == "__main__":
    a = CountryInfo()
    a.display_country_info()