def count_failed_by_ip(filename):
    with open(filename,"r") as file:

        failed_counts = {}

        for f in file:
            f = f.strip()
            if not f:
                continue
            
            parts = f.split()
            ip = parts[2]
            status = parts[4]

            if status != "FAILED":
                continue

            if ip in failed_counts:
                failed_counts[ip] = failed_counts[ip] + 1
            else:
                failed_counts[ip] = 1

        return failed_counts       

def detect_bruteforce(failed_counts, threshold):
    
    alerts = []
    
    for ip in failed_counts:
        if failed_counts[ip] >= threshold:
            alerts.append(ip)

    return alerts

filename = "soc_logs.txt"
failed_counts = count_failed_by_ip(filename)
alerts = detect_bruteforce(failed_counts, 3)

for ip in alerts:
 print(f"ALERT: {ip} suspected brute force ({failed_counts[ip]} failures)")