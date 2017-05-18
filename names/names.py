#encoding:utf-8
from config import * 

print '%s±¦±¦ÐÕ%s,³öÉúÓÚ%s,%s,%s'%(gender,first_name,birthday,birth_p,birth_c)
first_n_tone = convert(first_name)

if gender == 'ÄÐ':
    f = open('boy_name.txt')
elif gender == 'Å®':
    f = open('girl_name.txt')
for l in f:
    if l[0]=='-':
        print l
    elif len(l)>(len('Çì')+1): 
         middle_n_tone = convert(l[0:len('Çì')])
         last_n_tone = convert(l[len('Çì'):len(l)-1])
         
         if middle_n_tone != first_n_tone and last_n_tone != middle_n_tone : 
             try:
                 print first_name,l[:len(l)-1],score(first_name,l)
             except Exception as e:
                 print e 
                 continue
         else:
             middle_n_tone = convert(l[0:len('Çì')])
             if middle_n_tone != first_n_tone : 
                 try:
                     print first_name,l[:len(l)-1],score(first_name,l)
                 except Exception as e:
                     print e 
                     continue
