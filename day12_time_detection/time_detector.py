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

#print(collect_failure_times("soc_logs.txt"))

def time_to_seconds(time_str):
    parts = time_str.split(":")

    h = int(parts[0])
    m = int(parts[1])
    s = int(parts[2])

    total = h*3600 + m*60 + s

    return total
#print(time_to_seconds("10:15:40"))

def detect_bruteforce_time(data, threshold, window):

    for ip in data:

        times = data[ip]

        seconds = []

        for t in times:
            seconds.append(time_to_seconds(t))

            seconds.sort()

            if len(seconds) >= threshold:

                if seconds[-1] - seconds[0] <= window:
                    print(f"ALERT: {ip} brute force within {window} seconds")
data = collect_failure_times("soc_logs.txt")

detect_bruteforce_time(data, 3, 60)
                   