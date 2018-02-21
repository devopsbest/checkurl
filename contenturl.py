import requests
import pandas as pd

df = pd.read_excel("/Users/anderson/Downloads/Engage_Lesson_Image_Url.xlsx",index_col=None)
uls = df["Default Url"].str.replace("\\","/")


error_list = []

host = "http://staging.englishtown.com"

for x in uls.map(lambda x: host + x):
    if requests.get(x).status_code != 200:
        error_list.append(x)

if error_list != []:
    print ("faile {0}".format(error_list))
else:
    print("pass! no error found")

