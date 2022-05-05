from config import * 
import re
from urllib.parse import quote

def convert(ch):
    with open(r'pinying.txt','r',encoding='utf-8') as f:
        for line in f:
            if ch in line:
                 return line[len(line)-2:len(line)]

def score(x,m):
    '''score of x m'''
    import requests
    url = 'https://xmcs.buyiju.com/dafen.php'
    values ={'xs':quote(x),'mz':quote(m),'action':'test'}
    print(values)

    try:
        r = requests.post(url,data=values) 
        #print(r.text)
        rs = re.findall('<font color="ff0000" size="5">(.+)</font>',r.text) 
        #rs = re.findall('font (.+)font',r.text)
        return rs[0]
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print('%s,%s,%s,%s,%s'%(gender,first_name,birthday,birth_p,birth_c))
    first_n_tone = convert(first_name)

    if gender == 'M':
        f = open('boy_name.txt',encoding='utf-8')
    elif gender == 'F':
        f = open('girl_name.txt',encoding='utf-8')

    for l in f:
        if l[0]=='-':
            print(l)
        elif len(l) == 1:
             middle_n_tone = convert(l[0])
             if middle_n_tone != first_n_tone : 
                 print(first_name,l[0],score(first_name,l[0]))
        elif len(l)>=2: 
             middle_n_tone = convert(l[0])
             last_n_tone = convert(l[1]) 
             if middle_n_tone != first_n_tone and last_n_tone != middle_n_tone : 
                 print(first_name,l[0:2],score(first_name,l[0:2])) 
