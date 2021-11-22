import requests
from bs4 import BeautifulSoup
import pathlib
import os
import csv

a = 0
tl = []

def dulieu(link):
    try:
        global a, t1
        a=a+1

        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")

        t= soup.find('ul', class_='breadcrumb')
        titles = (t.find('a').attrs["data-medium"])[5:]
        t1 = "D:/Python/Crawl_vnexpress/data/"+titles+'/'+titles+'.csv'
        if tl.count(titles) == 0:
            tl.append(titles)
            os.mkdir("D:/Python/Crawl_vnexpress/data/"+titles)
            p1 = pathlib.Path(t1)
            p1.touch()

        with open(t1, mode='a+') as file:
            whiter = csv.writer(file)
            whiter.writerow(['news'+str(a), str(link)])

        t="D:/Python/Crawl_vnexpress/data/"+titles+'/news'+str(a)+'.txt'
        p = pathlib.Path(t)
        p.touch()
        f = open(t, 'w', encoding='UTF-8')

        f.write(soup.find('h1', class_='title-detail').text+' ')

        f.write(soup.find('p', class_='description').text)

        contents = soup.findAll('p', class_='Normal')
        for i in range(0, len(contents)-1):
            f.write(' '+ contents[i].text )

        f.close
    except:
        print(link)


def get_link3(linkc):
    try:
        response = requests.get(linkc)
        soup = BeautifulSoup(response.content, "html.parser")
        titles = soup.find_all('h3', class_='title-news')
        links = [link.find('a').attrs["href"] for link in titles]
        for link in links:
            dulieu(link)
    except:
        print(linkc+'sai')

def get_link2(linkc):
    try:
        response = requests.get(linkc)
        soup = BeautifulSoup(response.content, "html.parser")
        titles = soup.find_all('h2', class_='title-news')
        links = [link.find('a').attrs["href"] for link in titles]
        for link in links:
            dulieu(link)
    except:
        print(linkc+'sai')

try:
    os.mkdir('D:/Python/Crawl_vnexpress/data')
except OSError:
    print('Failed creating the directory')
else:
    print('Directory created')

links2 = [
    'https://vnexpress.net/suc-khoe',
    'https://vnexpress.net/du-lich',
    'https://vnexpress.net/so-hoa',
    'https://vnexpress.net/kinh-doanh',
    'https://vnexpress.net/giai-tri',
    'https://vnexpress.net/the-thao'
]

links3 = [
    'https://vnexpress.net/thoi-su',
    'https://vnexpress.net/goc-nhin',
    'https://vnexpress.net/the-gioi',
    'https://vnexpress.net/khoa-hoc',
    'https://vnexpress.net/phap-luat',
    'https://vnexpress.net/giao-duc',
    'https://vnexpress.net/oto-xe-may',
    'https://vnexpress.net/hai',
]
try:
    for link in links2:
        for i in range(2, 42):
            get_link2(link+'-p'+str(i))

    for link in links3:
        for i in range(2, 42):
            get_link3(link+'-p'+str(i))
except:
    print('1')