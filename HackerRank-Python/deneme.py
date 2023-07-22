# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:51:55 2023

@author: musad
"""


from datetime import datetime


tr = "Wed 12 May 2269 23:22:15 -0500"
tr1 = "Tue 05 Oct 2269 02:12:07 -0200"

tr = tr.split()
tr1 = tr1.split()


date_day1 = datetime.strptime(" ".join(tr[1:4]), "%d %b %Y")
date_day2 = datetime.strptime(" ".join(tr1[1:4]), "%d %b %Y")

fark_gün = date_day1 - date_day2

print(fark_gün)

a = abs(fark_gün.total_seconds())
print(a)

date_hour1 = datetime.strptime(tr[-2], "%H:%M:%S")
date_hour2 = datetime.strptime(tr1[-2], "%H:%M:%S")

if date_hour1 >= date_hour2:
    fark_saat = date_hour1 - date_hour2
    print(fark_saat)
    b = (fark_saat.total_seconds()) * (-1)
    print(b)

else:
    fark_saat = date_hour1 - date_hour2
    print(fark_saat)
    b = fark_saat.total_seconds()
    print(b)

if (tr[-1][0] == "+") and (tr1[-1][0] == "-"):
    date_mnu1 = datetime.strptime(tr[-1][1:], "%H%M")
    data_start = datetime.strptime("0000", "%H%M")
    date_mnu2 = datetime.strptime(tr1[-1][1:], "%H%M")
    
    farkk1 = date_mnu1 - data_start
    farkk2 = date_mnu2 - data_start
    
    x = farkk1.total_seconds()
    y = farkk2.total_seconds()    
    
    total_fark = x + y
    print(total_fark)
    
    print(int(abs(a+b-total_fark)))

elif (tr[-1][0] == "-") and (tr1[-1][0] == "+"):
    date_mnu11 = datetime.strptime(tr[-1][1:], "%H%M")
    data_start1 = datetime.strptime("0000", "%H%M")
    date_mnu21 = datetime.strptime(tr1[-1][1:], "%H%M")
    
    farkk11 = date_mnu11 - data_start1
    farkk21 = date_mnu21 - data_start1
    
    x1 = farkk11.total_seconds()
    y1 = farkk21.total_seconds()    
    
    total_fark1 = x1 + y1
    
    print(total_fark1)
    print(int(abs(a+b-total_fark1)))

else:
    date_mnu111 = datetime.strptime(tr[-1][1:], "%H%M")
    date_mnu211 = datetime.strptime(tr1[-1][1:], "%H%M")
    
    fark_dak = date_mnu111 - date_mnu211
    
    c = fark_dak.total_seconds()
    print(c)
    
    print(int(abs(a+b-c)))

