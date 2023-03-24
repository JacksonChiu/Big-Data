import requests
import csv
import datetime
import time

url="https://covid-19.nchc.org.tw/myDT_staff.php?TB_name=covidtable_taiwan_cdc4_1&limitColumn=id&limitValue=0&equalValue=!=&encodeKey=MTY3OTUxNzUwNg==&c[]=id&t[]=int&d[]=NO&c[]=a01&t[]=date&d[]=NO&c[]=a02&t[]=date&d[]=NO&c[]=a03&t[]=varchar&d[]=NO&c[]=a04&t[]=varchar&d[]=NO&c[]=a05&t[]=int&d[]=NO&c[]=a06&t[]=int&d[]=NO"

res=requests.get(url).json()['data']

with open('temp.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['個案研判日', '縣市別', '區域', '新增確診人數', '累計確診人數'])
    for i in res:
        temp_date_time = time.strptime(i['a01'],'%Y-%m-%d')   
        temp_date_time = datetime.date(temp_date_time.tm_year,temp_date_time.tm_mon,temp_date_time.tm_mday)
        if(i['a04']=='全區' and (temp_date_time<=datetime.date(2023, 3 ,14)) ):
            writer.writerow([i['a02'],i['a03'],i['a04'],i['a05'],i['a06']])

