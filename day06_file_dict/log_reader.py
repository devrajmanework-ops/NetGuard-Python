with open("logs.txt","r") as file: 

 count_logs = {}
 
 for f in file:
    f = f.strip()
    if not f:
       continue
    if f in count_logs:
       count_logs[f] = count_logs[f] + 1
    else:
       count_logs[f] = 1

for f in count_logs:
   print(f, "->",count_logs[f])
