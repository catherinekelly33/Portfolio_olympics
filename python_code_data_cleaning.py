# import modules
import pandas as pd
import numpy as np

# load and inspect files
athlete_bio = pd.read_csv('Olympic_Athlete_Bio.csv')
print(athlete_bio.head())
print(athlete_bio.info())

athlete_results = pd.read_csv('Olympic_Athlete_Event_Results.csv')
print(athlete_results.head())
print(athlete_results.info())

# data combining
combined_df = pd.merge(athlete_bio, athlete_results)
df_split = combined_df.edition.str.split(' ')
combined_df['Year'] = df_split.str.get(0)
combined_df['Year'] = combined_df['Year'].astype('int64')
combined_df['Olympics'] = df_split.str.get(1)

summer_olympics = combined_df[(combined_df.Olympics == 'Summer') & (combined_df.isTeamSport == False)].reset_index()

summer_olympics['born'] = pd.to_datetime(summer_olympics['born'], errors="coerce").dt.year

print(summer_olympics.head())
print(summer_olympics.info())

# testing for parameters with missing data
summer_olympics_missing = combined_df[(combined_df.Olympics == 'Summer') & (combined_df.isTeamSport == False)].reset_index()
summer_olympics_missing['born'] = summer_olympics_missing['born'].fillna(value=3000)
summer_olympics_missing['height'] = summer_olympics_missing['height'].fillna(value=3000)

summer_olympics_missing_dob = summer_olympics_missing[summer_olympics_missing.born == 3000].reset_index()
print('DOB - Olympics:', summer_olympics_missing_dob.edition.value_counts())
print('DOB - Sport: ', summer_olympics_missing_dob.sport.value_counts())
print('DOB - Medal: ', summer_olympics_missing_dob.medal.value_counts())

summer_olympics_missing_height = summer_olympics_missing[summer_olympics_missing.height == 3000].reset_index()
print('Height - Olympics:', summer_olympics_missing_height.edition.value_counts())
print('Height - Sport: ', summer_olympics_missing_height.sport.value_counts())
print('Height - Medal: ', summer_olympics_missing_height.medal.value_counts())

# data wrangling
summer_olympics_trimmed = summer_olympics[(summer_olympics.Year >= 2004) & (summer_olympics.Year < 2020)].reset_index()

print(summer_olympics_trimmed.info())
summer_olympics_trimmed['born'] = summer_olympics_trimmed['born'].fillna(value=3000)
summer_olympics_trimmed['height'] = summer_olympics_trimmed['height'].fillna(value=3000)

summer_olympics_trimmed_dob = summer_olympics_trimmed[summer_olympics_trimmed.born == 3000]
print('DOB - Olympics:', summer_olympics_trimmed_dob.edition.value_counts())
print('DOB - Sport: ', summer_olympics_trimmed_dob.sport.value_counts())
print('DOB - Medal: ', summer_olympics_trimmed_dob.medal.value_counts())

summer_olympics_trimmed_height = summer_olympics_trimmed[summer_olympics_trimmed.height == 3000]
print('Height - Olympics:', summer_olympics_trimmed_height.edition.value_counts())
print('Height - Sport: ', summer_olympics_trimmed_height.sport.value_counts())
print('Height - Medal: ', summer_olympics_trimmed_height.medal.value_counts())

# data cleaning
summer_olympics_cleaned = summer_olympics[(summer_olympics.Year >= 2004) & (summer_olympics.Year < 2020)].reset_index()
summer_olympics_cleaned = summer_olympics_cleaned.dropna(subset=['born', 'height', 'weight'])
print(summer_olympics_cleaned.head())
print(summer_olympics_cleaned.info())
print(summer_olympics_cleaned.weight.unique())

summer_olympics_cleaned = summer_olympics_cleaned[summer_olympics_cleaned.name != 'Nick Buckfield']
summer_olympics_cleaned['weight'] = summer_olympics_cleaned['weight'].replace('\xa0', '', regex=True)

summer_olympics_cleaned[['weight_low', 'weight_high']] = summer_olympics_cleaned['weight'].str.split('[-,]', expand=True)
summer_olympics_cleaned[['weight_low', 'weight_high']] = summer_olympics_cleaned[['weight_low', 'weight_high']].astype('float')
summer_olympics_cleaned = summer_olympics_cleaned.fillna(value={'weight_high':summer_olympics_cleaned.weight_low})


summer_olympics_cleaned['weight_average'] = (summer_olympics_cleaned['weight_low'] + summer_olympics_cleaned['weight_high']) * 0.5

summer_olympics_cleaned['BMI'] = summer_olympics_cleaned['weight_average'] / ((summer_olympics_cleaned['height']/100) ** 2) 
summer_olympics_cleaned['Age'] = summer_olympics_cleaned['Year'] - summer_olympics_cleaned['born']

print(summer_olympics_cleaned.head())
print(summer_olympics_cleaned.height.describe())
print(summer_olympics_cleaned.born.describe())

summer_olympics_final  = summer_olympics_cleaned[summer_olympics_cleaned.sex == 'Male'] 


print(summer_olympics_final.head())

# saving database
summer_olympics_final.to_csv(r'athlete_results_bio.csv')