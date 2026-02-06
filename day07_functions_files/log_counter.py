def count_log_entries(filename):
    with open (filename,"r") as file:
    
     log_count = {}

     for f in file:
        f = f.strip()
        if not f:
           continue
        if f in log_count:
           log_count[f] = log_count[f] + 1
        else:
           log_count[f] = 1
     return log_count
    
filename = ("sample_logs.txt")
result = count_log_entries(filename)
for f in result:
  print(f,"->",result[f])    