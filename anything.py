# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt

countries = pd.read_csv("countries_top10.csv")
df_countries = pd.DataFrame(data=countries)

print(df_countries.head())

population = df_countries["Population"]
area = df_countries["Area"]
gdp = df_countries["GDP"]

df_countries["Pop_per_km^(2)"] = population / area
df_countries["GDP_per_head"] = gdp / population

print(df_countries.head())
df_countries.to_excel("countries_t10(new).xlsx", sheet_name="Excel_Main")

# NO. 2

gdp_2015 = pd.read_excel("GDP_2015dollars.xls", sheet_name="GDP(2015$)")
df_gdp15 = pd.DataFrame(data=gdp_2015)
print(df_gdp15.head())

plt.figure()
plt.plot(gdp_2015["Year"], gdp_2015["China"], label="China")
plt.plot(gdp_2015["Year"], gdp_2015["Germany"], label="Germany")
plt.plot(gdp_2015["Year"], gdp_2015["Japan"], label="Japan")
plt.plot(gdp_2015["Year"], gdp_2015["United States"], label="United States")

plt.xlabel("Year")
plt.ylabel("GDP")
plt.legend()

plt.show()

gdp_2015["GDP of China/USA"] = (gdp_2015["China"] /
                                gdp_2015["United States"]) * 100
gdp_2015["GDP of Germany/USA"] = (gdp_2015["Germany"] /
                                  gdp_2015["United States"]) * 100
gdp_2015["GDP of Japan/USA"] = (gdp_2015["Japan"] /
                                gdp_2015["United States"]) * 100

print(gdp_2015)
plt.figure()
plt.plot(gdp_2015["Year"], gdp_2015["GDP of China/USA"], label="China/USA")
plt.plot(gdp_2015["Year"], gdp_2015["GDP of Germany/USA"], label="Germany/USA")
plt.plot(gdp_2015["Year"], gdp_2015["GDP of Japan/USA"], label="Japan/USA")

plt.xlabel("Year")
plt.ylabel("GDP/GDP USA")
plt.legend()


print(gdp_2015[41:51])
