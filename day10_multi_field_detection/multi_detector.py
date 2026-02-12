def  count_failed_by_ip(filename):
    with open (filename,"r") as file:
        count_failures = {}

        for f in file:
            f = f.strip()
            if not f:
                continue

            parts = f.split()
            ip = parts[2]
            service = parts[3]
            status = parts[4]

            if status != "FAILED":
                continue
            
            if ip not in count_failures:
                count_failures[ip] = {}

            if service not in count_failures[ip]:
                count_failures[ip][service] = 1
            else:
                count_failures[ip][service] +=1   

        return count_failures        
    
result = count_failed_by_ip("soc_logs.txt")
print (result)

def detect_bruteforce(count_failures, threshold):

    alerts = []

    for ip in count_failures:

        for service in count_failures[ip]:
            count = count_failures[ip][service]

            if count >= threshold:
                alerts.append((ip,service,count))
    return alerts
            
filename = "soc_logs.txt"

count_failures = count_failed_by_ip(filename)

alerts = detect_bruteforce(count_failures,3)

for ip, service, count in alerts:
    print(f"ALERT: {ip} brute force dected on {service} ({count} failures)")