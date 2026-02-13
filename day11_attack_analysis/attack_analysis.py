def count_failures_by_ip(filename):
    with open (filename,"r") as file:
        ip_failures = {}

        for f in file:
            f = f.strip()
            if not f :
                continue
            
            parts = f.split()
            ip = parts[2]
            status = parts[4]

            if status != "FAILED":
                continue
        
            if ip in ip_failures:
                ip_failures[ip] += 1
            else:
                ip_failures[ip] = 1

        return ip_failures

result = count_failures_by_ip("soc_logs.txt")
print(result)

def count_failures_by_service(filename):
    with open (filename,"r") as file:
    
     service_failures = {}
    
     for f in file:
         f = f.strip()
         if not f :
            continue
            
         parts = f.split()
         service = parts[3]
         status = parts[4] 

         if status != "FAILED":
            continue 
         
         if service in service_failures:
             service_failures[service] += 1
         else:
             service_failures[service] =1          
    
     return service_failures
    
print(count_failures_by_service("soc_logs.txt"))

def generate_report(ip_counts, service_counts):
    max_ip = None
    max_ip_count = 0

    for ip in ip_counts:

        if ip_counts[ip] > max_ip_count:

            max_ip = ip
            max_ip_count = ip_counts[ip]

    max_service = None
    max_service_count = 0

    for service in service_counts:
        if service_counts[service] > max_service_count:

            max_service = service
            max_service_count = service_counts[service]

    total_failures = sum(ip_counts.values())        
    unique_ips = len(ip_counts)

    print("\n=== SOC ATTACK SUMMARY ===\n")

    print(f"Most attacking IP: {max_ip} ({max_ip_count} failures)")


    print(f"most targated service:{max_service} ({max_service_count} failures)")

    print(f"total failures: {total_failures}")

    print(f"unique attacking IPs: {unique_ips}")

ip_counts = count_failures_by_ip("soc_logs.txt")

service_counts = count_failures_by_service("soc_logs.txt")

generate_report(ip_counts, service_counts)

