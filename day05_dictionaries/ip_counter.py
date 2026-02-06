ip_list=["192.168.1.1",
"10.0.0.1",
"192.168.1.1",
"10.0.0.1",
"10.0.0.1",
]
ip_counter={}
for ip in ip_list:
   
    if ip in ip_counter:
       ip_counter[ip] = ip_counter[ip] + 1
        
    else:
     ip_counter[ip] = 1

for ip in ip_counter:
   print(ip ,"->" ,ip_counter[ip])         

