ips = [
    "192.168.1.1",
    "192.168.1.2",
    "10.0.0.1",         #it is a list which stores ips
    "10.0.0.1",
    "10.0.0.1",
    "192.168.1.1"
]
ip_count = {}          #empty dir

for ip in ips:         #for loop  to check if ip was seen before
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

for ip, count in ip_count.items():
    print(ip,"->",count)    #final count which will print