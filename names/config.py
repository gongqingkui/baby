#encoding:utf-8

import traceback

first_name = '巩'

gender = '女'
birthday='20170407120000'
birth_p='河北'
birth_c='沧州'





def convert(ch):
    length = len('汉') #测试汉字占用字节数，utf-8，汉字占用3字节.bg2312，汉字占用2字节
    intord = ord(ch[0:1])
    if (intord >= 48 and intord <= 57):
         return ch[0:1]
    if (intord >= 65 and intord <=90 ) or (intord >= 97 and intord <=122):
        return ch[0:1].lower()
    ch = ch[0:length] #多个汉字只获取第一个
    with open(r'pinying.txt') as f:
        for line in f:
            if ch in line:
                 return line[len(line)-2:len(line)]

def score(x,m):
    import urllib
    import urllib2
    from bs4 import BeautifulSoup
    url = 'http://xmcs.buyiju.com/dafen.php'
    values ={'xs':x,'mz':m}
    try:
        data = urllib.urlencode(values)
        req = urllib2.Request(url,data)
        response = urllib2.urlopen(req)
        html_page = response.read()
    except Exception as e:
        traceback.print_exc()
        print e
    soup = BeautifulSoup(html_page,'html.parser')
    try:
        score = soup.find_all('font')
    except Exception as e:
        traceback.print_exc()
        print e
    return score[1].string
