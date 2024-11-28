import os
import requests
import zipfile
import pandas as pd

print('Getting the data...')

# define directories
data_dir = "../data/"
temp_dir = "../data/temp/"
os.makedirs(temp_dir, exist_ok=True)

# electric vehicle population data
ev_population_link = 'https://data.wa.gov/resource/3d5d-sdqb.csv?$limit=50000'

# root link for AQS data
aqs_root_link = 'https://aqs.epa.gov/aqsweb/airdata/daily_'

# link leafs for each pollutant
data_links = {
    "CO": "42101",
    "NO2": "42602",
    "PM10_Speciation": "PM10SPEC",
    "PM25_Speciation": "SPEC"   # PM2.5
}

# years range for AQS data
years = range(2016, 2025)

# ----------------------------------------------------------------------------
## Get EV population data:

df = pd.read_csv(ev_population_link)
# select only Washington state
df = df[df['state'] == 'WA']
# save
df.to_csv(os.path.join(data_dir, 'electric_car_population.csv'), index=False)

# ----------------------------------------------------------------------------
## Get AQS data:

def download_and_extract(link_key, code, year, temp_dir):
    """Download and extract zip file if not already downloaded."""
    zip_url = f"{aqs_root_link}{code}_{year}.zip"
    zip_file = os.path.join(temp_dir, f"{link_key}_{year}.zip")
    
    # download the file if it doesn't exist (to avoid unneccessary requests)
    if not os.path.exists(zip_file):
        print(f"Downloading: {zip_url}")
        response = requests.get(zip_url)
        with open(zip_file, "wb") as f:
            f.write(response.content)
    else:
        print(f"File already exists: {zip_file}")
    
    # extract the zip file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

def process_data(link_key, code, temp_dir, years):
    """Process data for a specific pollutant link."""
    dataframes = []
    for year in years:
        download_and_extract(link_key, code, year, temp_dir)
        
        # collect CSV files
        csv_files = [os.path.join(temp_dir, f) for f in os.listdir(temp_dir) if f.endswith('.csv')]
        for csv_file in csv_files:
            try:
                # read the CSV and filter
                df = pd.read_csv(csv_file, low_memory=False)
                df = df[df['County Name'] == 'King']
                dataframes.append(df)
            finally:
                # close and delete the file
                os.remove(csv_file)
    
    # concatenate all dataframes for the pollutant
    if dataframes:
        final_df = pd.concat(dataframes, ignore_index=True)
        output_file = os.path.join(data_dir, f"{link_key}.csv")
        final_df.to_csv(output_file, index=False)
        print(f"Saved: {output_file}")
    else:
        print(f"No data found for {link_key} in any year.")

# process each pollutant
for key, code in data_links.items():
    process_data(key, code, temp_dir, years)

print(f'Done! Data saved in {data_dir}')