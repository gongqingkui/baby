#encoding:utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup

url = 'http://xmcs.buyiju.com/dafen.php'

values ={'xs':'徐','mz':'翠平'}
data = urllib.urlencode(values)
print data
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
html_page = response.read()
#print html_page
soup = BeautifulSoup(html_page,'html.parser')

#print(soup.prettify())
print(soup.title)
print(soup.title.name)  
print(soup.title.string)
score = soup.find_all('font')
#print(type(score))
print(score[1].string)

#print (soup.get_text())
#for link in soup.find_all('a'):
    #print link
    #print link['href']
