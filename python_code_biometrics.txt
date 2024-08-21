# import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# average biometrics of Olympic athletes
biometrics = pd.read_csv('athlete_results_bio.csv')
print(biometrics.head())
print(biometrics.describe())

print(biometrics.groupby('sport').Age.min())
print(biometrics.groupby('sport').Age.max())
print(biometrics.groupby('sport').height.min())
print(biometrics.groupby('sport').height.max())
print(biometrics.groupby('sport').weight_average.min())
print(biometrics.groupby('sport').weight_average.max())
print(biometrics.groupby('sport').BMI.min())
print(biometrics.groupby('sport').BMI.max())

# graphs of Olympic athletes biometrics
plt.figure(figsize = (8, 6))
for i in range(0,4):
    biometrics_type = ['Age', 'height', 'weight_average', 'BMI']
    labels = ['Age (years)', 'Height (cm)', 'Weight (kg)', 'BMI']
    plt.subplot(2,2,i+1)
    plt.hist(biometrics[biometrics_type[i]], bins=20)
    plt.xlabel(labels[i])
    plt.ylabel('Frequency')
    plt.title('{} distribution'.format(labels[i]))

plt.tight_layout()
plt.savefig('histogram_all.png')
plt.show()
plt.clf()

# eventing
biometrics_eventing = biometrics[biometrics.sport == 'Equestrian Eventing']
biometrics_not_eventing = biometrics[biometrics.sport != 'Equestrian Eventing']

biometrics_type = ['Age', 'height', 'weight_average', 'BMI']
for biometric in biometrics_type:
    mean_eventing = round(biometrics_eventing[biometric].mean(),2)
    mean_olympian = round(biometrics_not_eventing[biometric].mean(),2)
    std_eventing = round(biometrics_eventing[biometric].std(),2)
    std_olympian = round(biometrics_not_eventing[biometric].std(), 2)
    print('Eventing {}: {} std: {}'.format(biometric, mean_eventing, std_eventing))
    print('Olympian {}: {} std: {}'.format(biometric, mean_olympian, std_olympian))

for biometric in biometrics_type:
    t_val, p_val = ttest_ind(biometrics_eventing[biometric], biometrics_not_eventing[biometric], equal_var=False)
    print('{} p_val:'.format(biometric), (p_val))

# mens 100m
biometrics_men_100m = biometrics[biometrics.event == '100 metres, Men']
biometrics_men_not_100m = biometrics[biometrics.sport != '100 metres, Men']

biometrics_type = ['Age', 'height', 'weight_average', 'BMI']
for biometric in biometrics_type:
    mean_100m = round(biometrics_men_100m[biometric].mean(),2)
    mean_olympian = round(biometrics_men_not_100m[biometric].mean(),2)
    std_100m = round(biometrics_men_100m[biometric].std(),2)
    std_olympian = round(biometrics_men_not_100m[biometric].std(), 2)
    print('100m {}: {} std: {}'.format(biometric, mean_100m, std_100m))
    print('Olympian {}: {} std: {}'.format(biometric, mean_olympian, std_olympian))

for biometric in biometrics_type:
    t_val, p_val = ttest_ind(biometrics_men_100m[biometric], biometrics_men_not_100m[biometric], equal_var=False)
    print('{} p_val:'.format(biometric), (p_val))

# mens marathon
biometrics_men_marathon = biometrics[biometrics.event == 'Marathon, Men']
biometrics_men_not_marathon = biometrics[biometrics.sport != 'Marathon, Men']

biometrics_type = ['Age', 'height', 'weight_average', 'BMI']
for biometric in biometrics_type:
    mean_marathon = round(biometrics_men_marathon[biometric].mean(),2)
    mean_olympian = round(biometrics_men_not_marathon[biometric].mean(),2)
    std_marathon = round(biometrics_men_marathon[biometric].std(),2)
    std_olympian = round(biometrics_men_not_marathon[biometric].std(), 2)
    print('Marathon {}: {} std: {}'.format(biometric, mean_marathon, std_marathon))
    print('Olympian {}: {} std: {}'.format(biometric, mean_olympian, std_olympian))

for biometric in biometrics_type:
    t_val, p_val = ttest_ind(biometrics_men_marathon[biometric], biometrics_men_not_marathon[biometric], equal_var=False)
    print('{} p_val:'.format(biometric), (p_val))

# mens shot put
biometrics_men_shot = biometrics[biometrics.event == 'Shot Put, Men']
biometrics_men_not_shot = biometrics[biometrics.sport != 'Shot Put, Men']

biometrics_type = ['Age', 'height', 'weight_average', 'BMI']
for biometric in biometrics_type:
    mean_shot = round(biometrics_men_shot[biometric].mean(),2)
    mean_olympian = round(biometrics_men_not_shot[biometric].mean(),2)
    std_shot = round(biometrics_men_shot[biometric].std(),2)
    std_olympian = round(biometrics_men_not_shot[biometric].std(), 2)
    print('Shot put {}: {} std: {}'.format(biometric, mean_shot, std_shot))
    print('Olympian {}: {} std: {}'.format(biometric, mean_olympian, std_olympian))

for biometric in biometrics_type:
    t_val, p_val = ttest_ind(biometrics_men_shot[biometric], biometrics_men_not_shot[biometric], equal_var=False)
    print('{} p_val:'.format(biometric), (p_val))

# mens high jump
biometrics_men_jump = biometrics[biometrics.event == 'High Jump, Men']
biometrics_men_not_jump = biometrics[biometrics.sport != 'High Jump, Men']

biometrics_type = ['Age', 'height', 'weight_average', 'BMI']
for biometric in biometrics_type:
    mean_jump = round(biometrics_men_jump[biometric].mean(),2)
    mean_olympian = round(biometrics_men_not_jump[biometric].mean(),2)
    std_jump = round(biometrics_men_jump[biometric].std(),2)
    std_olympian = round(biometrics_men_not_jump[biometric].std(), 2)
    print('High jump {}: {} std: {}'.format(biometric, mean_jump, std_jump))
    print('Olympian {}: {} std: {}'.format(biometric, mean_olympian, std_olympian))

for biometric in biometrics_type:
    t_val, p_val = ttest_ind(biometrics_men_jump[biometric], biometrics_men_not_jump[biometric], equal_var=False)
    print('{} p_val:'.format(biometric), (p_val))

# comparison histograms
df = [biometrics_eventing, biometrics_men_100m, biometrics_men_marathon, biometrics_men_shot, biometrics_men_jump]
not_df = [biometrics_not_eventing, biometrics_men_not_100m, biometrics_men_not_marathon, biometrics_men_not_shot, biometrics_men_not_jump]
events = ['Eventing', '100 m', 'Marathon', 'Shot put', 'High jump']
file = ['eventing.png', 'men100m.png', 'marathon.png', 'shotput.png', 'highjump.png']


for j in range(0,5):
    plt.figure(figsize = (8, 6))
    for i in range(0,4):
        biometrics_type = ['Age', 'height', 'weight_average', 'BMI']
        labels = ['Age (years)', 'Height (cm)', 'Weight (kg)', 'BMI']
        plt.subplot(2,2,i+1)
        plt.hist(df[j][biometrics_type[i]], bins=20, label=events[j], density=True, alpha=0.5)
        plt.hist(not_df[j][biometrics_type[i]], bins=20, label='Olympians', density=True, alpha=0.5)
        plt.legend()
        plt.xlabel(labels[i])
        plt.ylabel('Frequency')
        plt.title('{} - {}'.format(events[j], labels[i]))
    plt.tight_layout()
    plt.savefig(file[j])
    plt.show()
    plt.clf()

# Comparison across sports
plt.figure(figsize = (8,6))
for i in range(1,5):
    x_labels = ['Eventing', '100 m', 'Marathon', 'Shot put', 'High jump']
    sports = [biometrics_eventing, biometrics_men_100m, biometrics_men_marathon, biometrics_men_shot, biometrics_men_jump]
    biometrics_type = ['Age', 'height', 'weight_average', 'BMI']
    xlabels = ['Age (years)', 'Height (cm)', 'Weight (kg)', 'BMI']
    
    ax=plt.subplot(2,2,i)
    y_values = []
    error = []

    for sport in sports:
        mean = sport[biometrics_type[i-1]].mean()
        y_values.append(mean)
        std = sport[biometrics_type[i-1]].std()
        error.append(std)
    
    plt.bar(range(len(y_values)), y_values, yerr = error, capsize=5)
    ax.set_xticks(range(len(y_values)))
    ax.set_xticklabels(x_labels)
    plt.xticks(rotation = 30)
    plt.xlabel('Sport')
    plt.ylabel(xlabels[i-1])
    plt.title(xlabels[i-1])

plt.tight_layout()
plt.savefig('sport_comparison.png')
plt.show()
plt.clf()



