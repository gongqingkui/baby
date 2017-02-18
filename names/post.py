#encoding:utf-8
import urllib
import urllib2

url = 'http://xmcs.buyiju.com/dafen.php'

values ={'xs':'巩','mz':'庆奎'}
data = urllib.urlencode(values)
print data
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
page = response.read()
print page
