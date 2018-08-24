import numpy as np
import pandas as pd
import json
import difflib
from bs4 import BeautifulSoup


from collections import defaultdict
from pandas.io.json import json_normalize

filepath1 = './indeed_job_search_api/job_ad_fulltime_with_summary.txt'
filepath2 = './indeed_job_search_api/job_ad_parttime_with_summary.txt'

def read_data(filepath):
    file = open(filepath, 'r')
    text = file.read()
    dict = json.loads(text)
    data = dict['results']
    return json_normalize(data)

def analyse_df(df):
    print df.head()
    print df.describe()
    print df.dtypes
    print df.isnull().sum()

def parse_summary(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

fulltime_data = read_data(filepath1)
parttime_data = read_data(filepath2)

gov_data = pd.read_csv('./UK Gender Pay Gap Data - 2017 to 2018.csv')
#analyse_df(gov_data)

clean_summary_full = fulltime_data['jobsummary'].apply(lambda x: parse_summary(x))
clean_summary_part = parttime_data['jobsummary'].apply(lambda x: parse_summary(x))

df_fulltime = pd.concat([fulltime_data.drop(['jobsummary'], axis=1), clean_summary_full])
df_parttime = pd.concat([parttime_data.drop(['jobsummary'], axis=1), clean_summary_part])

df = pd.concat([df_fulltime, df_parttime]) # text files from with job summary
# df['Matches'] = df['company'].map(lambda x: difflib.get_close_matches(x, gov_data['EmployerName']))
# match_df = df.Matches.apply(pd.Series).rename(columns={0:'EmployerName'})
# df = pd.concat([match_df['EmployerName'],df], axis=1)
# pay_desc_df = pd.merge(pay_df,df, how="inner", on='EmployerName')
#analyse_df(pay_desc_df)

text1 = clean_summary_full.iloc[0]
print(text1)

#analyse_df(df)

#ad1 = fulltime_data[0]
#print(ad1)
#print(len(ad1))
#for item in ad1:
    #print item, "\n", ad1[item], "\n"

#print ad1["city"]

#for item in data[0:10]:
#    print item["city"], "\n"

# cities = []
# city_dict = defaultdict(int)
# for item in data:
#     city = item["city"]
#     if city not in city_dict:
#         city_dict[city] = 1
#         cities.append(city)
#     else:
#         city_dict[city] += 1

#print(len(cities))
#print(city_dict)

#title_and_summary = df[['jobtitle','jobsummary']]
#print(title_and_summary.head())




















