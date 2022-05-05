from config import * 

print('%s%s,%s,%s,%s'%(gender,first_name,birthday,birth_p,birth_c))
first_n_tone = convert(first_name)

if gender == 'M':
    f = open('boy_name.txt',encoding='utf-8')
elif gender == 'F':
    f = open('girl_name.txt',encoding='utf-8')
for l in f:
    if l[0]=='-':
        print(l)
    elif len(l)>3: 
         middle_n_tone = convert(l[0:3])
         last_n_tone = convert(l[3:len(l)-1])
         
         if middle_n_tone != first_n_tone and last_n_tone != middle_n_tone : 
             print(first_name,l[:-1],score(first_name.decode('utf-8'),l.decode('utf-8')))
         else:
             middle_n_tone = convert(l[0:3])
             if middle_n_tone != first_n_tone : 
                 try:
                     print(first_name,l[:len(l)-1],score(first_name,l))
                 except Exception as e:
                     print(e)
                     continue
