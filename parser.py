import re
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'https://www.dramteatr.ru/seasons'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('div', class_='region region-content')
    rows = table.find_all('div', class_='views-field views-field-title')
    dates = soup.find_all("span", class_= "dt1")
    month = soup.find_all("span", class_="dt2")
    a = (re.sub("\<span class\=\"dt1\"\>","", str(dates)))
    b = (re.sub("\<\/span\>", "", str(a)))
    c = b.split()
       # month = soup.find_all("span", class_= "dt2")
       # weekday = soup.find_all("span", class_="dt3")
    projects = []
    for row in rows:
        projects.append({
            'title': row.a.text,
        })
    for i, j in zip(projects,c):
        print(i,j)
   # for dt1 in date:
   #     projects[0]['date'] = dt1.text
   # for dt2 in month:
   #     projects[0]['month'] = dt2.text

   # for project in projects:
    #    print(project)






def get_links(dirty_list,start,end):
#из "грязной" версии забираем чистые URL-ы
    links=[]
    for row in dirty_list:
        if row!='None':
            i_beg=row.find(start)
            i_end=row.rfind(end)
            if i_beg!=-1 & i_end!=-1:
                links.append(row[i_beg:i_end])
    return links

def main():
    parse(get_html('https://www.dramteatr.ru/seasons'))

if __name__ == '__main__':
    main()