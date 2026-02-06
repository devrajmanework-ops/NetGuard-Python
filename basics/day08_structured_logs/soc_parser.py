def count_failed_by_ip (filename):
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

filename = ("soc_logs.txt")
result = count_failed_by_ip (filename)

for ip in result:
   print(ip,"->",result[ip])