from os import stat
import pandas as pd
import statistics
import random

df = pd.read_csv(r'article_data.csv')

data = df['claps'].tolist()

mean_list = []

for i in range(0,100):
    sample_dataset = []

    for i in range(0,30):
        random_index = random.randint(0,len(data))
        randclaps = data[random_index]
        sample_dataset.append(randclaps)

    sample_mean = statistics.mean(sample_dataset)
    mean_list.append(sample_mean)

pop_mean = statistics.mean(data)
mean1000 = statistics.mean(mean_list)

print('population mean: ', pop_mean)
print('sample mean of 1000 means: ', mean1000)