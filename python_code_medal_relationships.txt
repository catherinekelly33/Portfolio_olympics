# import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import pearsonr

# host countries
medal_tally = pd.read_csv('Olympic_Games_Medal_Tally.csv')
medal_tally['Olympics'] = medal_tally.edition.str[-15:]
medal_tally_summer = medal_tally[medal_tally.Olympics == 'Summer Olympics']

print(medal_tally_summer.head())

plt.figure(figsize = (10,6))
plt.plot(medal_tally_summer[medal_tally_summer.country == 'United States'].year, medal_tally_summer[medal_tally_summer.country == 'United States'].gold)
plt.plot(medal_tally_summer[medal_tally_summer.country == 'Great Britain'].year, medal_tally_summer[medal_tally_summer.country == 'Great Britain'].gold)
plt.plot(medal_tally_summer[medal_tally_summer.country == 'Australia'].year, medal_tally_summer[medal_tally_summer.country == 'Australia'].gold)
plt.plot(medal_tally_summer[medal_tally_summer.country == 'France'].year, medal_tally_summer[medal_tally_summer.country == 'France'].gold)
plt.legend(['USA', 'Great Britain', 'Austrailia', 'France'])
plt.xlabel('Year')
plt.ylabel('Gold Medals')
plt.savefig('gold_medals_time.png')

plt.figure(figsize = (10,6))
plt.plot(medal_tally_summer[medal_tally_summer.country == 'United States'].year, medal_tally_summer[medal_tally_summer.country == 'United States'].total)
plt.plot(medal_tally_summer[medal_tally_summer.country == 'Great Britain'].year, medal_tally_summer[medal_tally_summer.country == 'Great Britain'].total)
plt.plot(medal_tally_summer[medal_tally_summer.country == 'Australia'].year, medal_tally_summer[medal_tally_summer.country == 'Australia'].total)
plt.plot(medal_tally_summer[medal_tally_summer.country == 'France'].year, medal_tally_summer[medal_tally_summer.country == 'France'].total)
plt.legend(['USA', 'Great Britain', 'Austrailia', 'France'])
plt.xlabel('Year')
plt.ylabel('Total Medals')

plt.savefig('total_medals_time.png')
plt.show()
plt.clf()

# uplaoding GDP and population files
GDP = pd.read_csv('GDP_correct.csv')
GDP_melt = GDP.melt(id_vars='Country', value_vars = ['2004', '2008', '2012', '2016'], value_name = 'GDP', var_name = 'year')
print(GDP_melt.head())

population = pd.read_csv('population_correct.csv')
population_melt = population.melt(id_vars='Country', value_vars = ['2004', '2008', '2012', '2016'], value_name = 'population', var_name = 'year')
print(population_melt.head())
print(population_melt.year.unique())

GDP_population = pd.merge(GDP_melt, population_melt, how='outer')
GDP_population['year'] = GDP_population['year'].astype('int64')
GDP_population['GDP'] = GDP_population['GDP'].str.replace(',', '', regex=True)
GDP_population['GDP'] = GDP_population['GDP'].astype('float')

medal_tally_2004_2016 = medal_tally_summer[(medal_tally_summer.year >= 2004) & (medal_tally_summer.year < 2020)]


medals_GDP_population = pd.merge(medal_tally_2004_2016, GDP_population, how='left', left_on=[medal_tally_2004_2016.country, medal_tally_2004_2016.year], right_on=[GDP_population.Country, GDP_population.year])
medals_GDP_population = medals_GDP_population.dropna(subset = ['year_y'])
medals_GDP_population = medals_GDP_population.dropna(subset = ['gold'])
medals_GDP_population = medals_GDP_population.dropna(subset = ['total'])
medals_GDP_population = medals_GDP_population.dropna(subset = ['GDP'])
medals_GDP_population = medals_GDP_population.dropna(subset = ['population'])

print(medals_GDP_population.head())
print(medals_GDP_population.info())

# population
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.scatter(medals_GDP_population.population, medals_GDP_population.total)
plt.xlabel('Population')
plt.ylabel('total medals')
plt.title('Total medals versus population')


high_population = medals_GDP_population[medals_GDP_population.population > 1000000000]
print(high_population)

medals_GDP_population_trimmed = medals_GDP_population[medals_GDP_population.population < 1000000000]

plt.subplot(1,2,2)
plt.scatter(medals_GDP_population_trimmed.population, medals_GDP_population_trimmed.total)
plt.xlabel('Population')
plt.ylabel('Total medals')
plt.title('Total medals versus population')
plt.tight_layout()
plt.savefig('population_total')
plt.show()
plt.clf()

corr, p = pearsonr(medals_GDP_population.population, medals_GDP_population.total)
print('Pearson correlation total medals:', corr)

corr, p = pearsonr(medals_GDP_population_trimmed.population, medals_GDP_population_trimmed.total)
print('Pearson correlation trimmed total medals:', corr)

plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.scatter(medals_GDP_population.population, medals_GDP_population.gold)
plt.xlabel('Population')
plt.ylabel('Gold medals')
plt.title('Gold medals versus population')

plt.subplot(1,2,2)
plt.scatter(medals_GDP_population_trimmed.population, medals_GDP_population_trimmed.gold)
plt.xlabel('Population')
plt.ylabel('Gold medals')
plt.title('Gold medals versus population')
plt.axis([0, 600000000, 0, 50])
plt.tight_layout()
plt.savefig('population_gold.png')
plt.show()
plt.clf()

corr, p = pearsonr(medals_GDP_population.population, medals_GDP_population.gold)
print('Pearson correlation Gold medals:', corr)

corr, p = pearsonr(medals_GDP_population_trimmed.population, medals_GDP_population_trimmed.gold)
print('Pearson correlation trimmed Gold medals:', corr)

# medals versus GDP
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.scatter(medals_GDP_population.GDP, medals_GDP_population.total)
plt.xlabel('GDP')
plt.ylabel('Total medals')
plt.title('Total medals versus GDP')

plt.subplot(1,2,2)
plt.scatter(medals_GDP_population.GDP, medals_GDP_population.gold)
plt.xlabel('GDP')
plt.ylabel('Gold medals')
plt.title('Gold medals versus GDP')
plt.tight_layout()
plt.savefig('GDP')
plt.show()
plt.clf()

corr, p = pearsonr(medals_GDP_population.GDP, medals_GDP_population.total)
print('Pearson correlation total:', corr)

corr, p = pearsonr(medals_GDP_population.GDP, medals_GDP_population.gold)
print('Pearson correlation gold:', corr)

# GDP per population
medals_GDP_population ['GDP_per_person'] = medals_GDP_population ['GDP'] / medals_GDP_population ['population']
print(medals_GDP_population.head())

plt.scatter(medals_GDP_population.GDP_per_person, medals_GDP_population.total)
plt.xlabel('GDP per person')
plt.ylabel('Total medals')
plt.title('Total medals versus GDP per person')
plt.show()
plt.clf()


corr, p = pearsonr(medals_GDP_population.GDP_per_person, medals_GDP_population.total)
print('Pearson correlation:', corr)


