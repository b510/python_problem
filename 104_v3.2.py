from selenium import webdriver
from bs4 import BeautifulSoup
import multiprocessing as mp
import requests
import time


def page_age(p):
    for i in range(p):
        chrome.execute_script("window.scrollBy(0,30000)")#瀑布式，往下拉30000點(最多拉一頁)
        time.sleep(3)
        soup = BeautifulSoup(chrome.page_source,"lxml")
    return soup

def all_url(soup):
    box=[]
    for link in soup.find_all('article'):
        try:
            a=link.find_all('a')[0]["href"]
            url=('http:'+a)
            box.append(url)
        except:
            print('get url ERREO')
    return box

def data():
    for i in range(len(url)):
        try:
            r=requests.get(url[i])
            soup=BeautifulSoup(r.text,"html.parser")
            title=soup.find_all('title')[0].string#title
            ability=soup.find_all('p')[0].text	#ability
            money=soup.find_all('dl')[0]('dd')[1].text#money
            f = open('pool_test.txt','a',encoding="UTF-8")
            f.write("%s\n" % title)
            f.write("%s\n" % ability)
            f.write("%s\n\n" % money)
            f.write("------------------------------------------------------------")
        except:
            print('第%d筆URL ERREO' % i)
            f.close()
    f.close()

def pool_test():
    pool = mp.Pool()
    res = pool.map(data())
    pool.close()
    pool.join()

if __name__ == '__main__':
    page=1#要爬的頁數，1頁+20
    add_url="https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&order=15&asc=0&sctp=M&scmin=40000&scstrict=1&scneg=0&page=1&mode=s"
    chrome_options = webdriver.ChromeOptions()
    chrome = webdriver.Chrome(options=chrome_options)
    chrome.get(add_url)
    print('----------cat url!!----------')
    url=all_url(page_age(page))
    print("URL AGE=%d" % len(url))
    chrome.quit()#關網頁
    print('----------cat data!!----------')
    pool_test()