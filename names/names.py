#encoding:utf-8

from config import * 

print '%s宝宝姓%s.出生在%s日，出生于%s%s'%(gender,first_name,birthday,birth_p,birth_c)
first_n_tone = convert(first_name)
if gender == '男':
    with open('boy_name.txt') as f:
         for l in f:
             if l[0]=='-':
                 continue
             elif len(l)>(len('汉')+1): 
                 middle_n_tone = convert(l[0:len('汉')])
                 last_n_tone = convert(l[len('汉'):len(l)-1])
                 if middle_n_tone != first_n_tone and last_n_tone != middle_n_tone : 
                     print first_name,l 
             else:
                 #print convert(l[0:len('汉')])
                 print ''
elif gender == '女':
    print '女'
