
import os
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
%matplotlib inline

import seaborn as sns
#get current path
currentPath = os.getcwd()
#change path
os.chdir('E:/workspace/Project_1/data')


data1 = pd.read_csv('시군구별 교통사고2_명칭통합.csv', encoding = 'EUC-KR')
data1.head(5)

data1.loc["2014":"2018"]
data1[["2014","2015","2016","2017","2018"]]
pd.data1["total"] = pd.data1["2014"]



data2 = pd.read_csv("시군구별 교통사고2_명칭통합_ver01.csv", encoding = 'EUC-KR')
data2.head()
import folium
import json
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
pop_folium = data2.set_index('명칭')

pop_folium.head()

geo_path = '02. skorea_municipalities_geo_simple.json'
geo_data = json.load(open(geo_path, encoding= 'utf-8'))

map = folium.Map(location=[37.2002, 127.054], zoom_start=6)

map.choropleth(geo_data,
               data = pop_folium['pct'],
               columns = [pop_folium.index, pop_folium['pct']],
               fill_color = 'PuBu',
               key_on = 'feature.id')

map


# 데이터 시각화
graph1 = pd.read_csv("graph_test1.csv")
graph1.head(5)
sns.barplot(x = '건수', y = '발생건수', hue = '년도', data = graph1)