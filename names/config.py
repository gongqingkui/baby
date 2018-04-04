#encoding:utf-8
import traceback
import pprint
import re

first_name = '王'
gender = 'M'
birthday='20170516120000'
birth_p='山东'
birth_c='滕州'


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
    '''score of x m'''
    import requests
    url = 'http://xmcs.buyiju.com/dafen.php'
    values ={'xs':x,'mz':m,'action':'test'}

    try:
        r = requests.post(url,data=values) 
        print r.text
        #rs = re.findall('<font color=ff0000 size=5>(.+)</font>',r.text.encode('utf-8'))
        rs = re.findall('font (.+)font',r.text)
        return rs[0]
    except Exception as e:
        traceback.print_exc()
        print e
