#encoding:utf-8

from config import * 

print(score('巩','庆奎'))
print '%s宝宝姓%s.出生在%s日，出生于%s%s'%(gender,first_name,birthday,birth_p,birth_c)
first_n_tone = convert(first_name)
if gender == '男':
    with open('boy_name.txt') as f:
         for l in f:
             if l[0]=='-':
                 print l
                 #continue
             elif len(l)>(len('汉')+1): 
                 middle_n_tone = convert(l[0:len('汉')])
                 last_n_tone = convert(l[len('汉'):len(l)-1])
                 if middle_n_tone != first_n_tone and last_n_tone != middle_n_tone : 
                     print first_name,l[:len(l)-1],score(first_name,l)
             else:
                 middle_n_tone = convert(l[0:len('汉')])
                 if middle_n_tone != first_n_tone : 
                     print first_name,l ,score(first_name,l)

elif gender == '女':
    print '女'
