#-*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

with open('data.txt', 'r') as f:
    data = f.readlines()
data_row = len(open('data.txt','r',encoding ='UTF-8').readlines())

success=0
failure=0
T=5									#timeout時間設定

r=requests.get("http://ip.42.pl/raw")
soup=BeautifulSoup(r.text,"html.parser")

f = open('http_OK1.txt','a',encoding="UTF-8")
f.write("myip:%s\n" % soup)
f.write("timeout=%d\n\n" % T)

headers = {'user-agent': '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 77.0.3865.120 Safari/537.36'}

print("--------------------執行中--------------------")
for x in range(data_row):
	try:
		url = data[x].strip('\n')
		rr = requests.get(("http://"+url),headers=headers,timeout=T)
		r = str(rr)
		b = re.findall(r"\d+",r)
		soup = BeautifulSoup(rr.text,"html.parser")
		if((b[0]=="401") or (b[0]=="200")):
			
			title_data= (soup.title).text
			f.write('[%s]%s,%s\n' % (b[0],url,title_data))
			b[0]="0"
			success+=1
		else:
			failure+=1
	except:
		failure+=1
print("all=%d success=%d failure=%d" % (data_row,success,failure))
f.write("\n all=%d success=%d failure=%d" % (data_row,success,failure,))
f.close()