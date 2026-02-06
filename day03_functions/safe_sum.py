data = [1, 2, "a", 3.5, None, 4]
 
def safe_sum(data):

    total = 0

    for n in data:
     if isinstance(n,(int,float)):
      total = total + n
    return total 

result = safe_sum(data)
print("sum is:",result)

