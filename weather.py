import requests
import re
from bs4 import BeautifulSoup
r=requests.get('http://www.indiaweather.gov.in/?page_id=942&tags=Safdarjung')
indiaweather_site=open('indiaweather_site.lxml','a+')
indiaweather_site.write(r.content)
soup=BeautifulSoup(r.content,'lxml')
x= soup.body.table.tr.find_all(re.compile('font'))[3]
print 'Current Temperature is %s degree celsius.'%(x.string)						
	






