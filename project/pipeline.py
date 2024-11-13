import os
import pandas as pd

print('Getting the data...')

data_dir = '../data/'

data_links = ['https://data.wa.gov/resource/3d5d-sdqb.csv?$limit=50000',
              'https://data.transportation.gov/resource/5qxh-t94v.csv?$limit=50000',
              'https://data.transportation.gov/resource/5n49-mh85.csv?$limit=50000']

file_names = ['electric_car_population.csv', 
              'motor_fuel_distribution.csv', 
              'special_fuel_distribution.csv']
# read
df0 = pd.read_csv(data_links[0])
df1 = pd.read_csv(data_links[1])
df2 = pd.read_csv(data_links[2])

# select only Washington state
df0 = df0[df0['state'] == 'WA']
df1 = df1[df1['state'] == 'Washington']
df2 = df2[df2['state'] == 'Washington']

# save
df0.to_csv(os.path.join(data_dir, file_names[0]), index=False)
df1.to_csv(os.path.join(data_dir, file_names[1]), index=False)
df2.to_csv(os.path.join(data_dir, file_names[2]), index=False)

print(f'Done! Data saved in {data_dir}')