with open ("soc_logs.txt","r") as file:

    failed_counts = {}

    for f in file:
       f = f.strip()
       if not f:
          continue
       
       columns = f.split()
    
       if f in failed_counts:
          failed_counts[f] = failed_counts[f] + 1
       else:
          failed_counts[f] = 1

for f in failed_counts:
    print (f,"->",failed_counts[f])        