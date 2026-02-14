"""
NetGuard Detection Engine v1
Author: Devraj Mane

Features:
- Detect brute force by failure count
- Detect brute force by time window
- Generate SOC attack summary report

Log format expected:
DATE TIME IP SERVICE STATUS
"""


def time_to_seconds(time_str):
    parts = time_str.split(":")

    h = int(parts[0])
    m = int(parts[1])
    s = int(parts[2])

    total = h*3600 + m*60 + s

    return total
    

def collect_failure_times(filename):
    with open(filename,"r") as file:

        count_failure = {}

        for f in file:
            f = f.strip()
            if not f:
                continue 
            
            parts = f.split()
            ip = parts[2]   
            time = parts[1]
            status = parts[4]

            if status != "FAILED":
                continue
            
            if ip not in count_failure:
                
                count_failure[ip] = []

            count_failure[ip].append(time)
            
        return count_failure


def count_failures_by_ip (filename):
    with open(filename,"r") as file:

     failed_count ={}

     for f in file:
        f  = f.strip()
        if not f:
           continue
        
        parts = f.split()     
        ip = parts[2]
        status = parts[4]
        if status !="FAILED":
            continue
        if ip in failed_count:
           failed_count[ip] = failed_count[ip] + 1
        else:
           failed_count[ip] = 1

    return failed_count


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
    
                  
def detect_bruteforce_count(ip_counts, threshold):

    for ip in ip_counts:

        if ip_counts[ip] >= threshold:

            print(f"[ALERT] Brute force detected from {ip} ({ip_counts[ip]} failures)")
    

def detect_bruteforce_time(data, threshold, window):

    for ip in data:

        times = data[ip]

        seconds = []

        for t in times:
            seconds.append(time_to_seconds(t))

        seconds.sort()

        for i in range(len(seconds) - threshold + 1):

            if seconds[i + threshold - 1] - seconds[i] <= window:
                    
                    print(f"[ALERT] Fast brute force detected from {ip} within {window} seconds")
                    
                    break

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


# Engine Execution

print("=== NetGuard Detection Engine v1 ===\n")

filename = "soc_logs.txt"

time_data = collect_failure_times(filename)

ip_counts = count_failures_by_ip(filename)

service_counts = count_failures_by_service(filename)


detect_bruteforce_count(ip_counts, 3)

detect_bruteforce_time(time_data, 3, 60)


generate_report(ip_counts, service_counts)

                   
