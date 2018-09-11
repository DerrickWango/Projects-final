



def next_permutation(items):
  
  n = len(items)
  
  # Find pivot
  
  k = None
  
  for i in range(n-1):
    
    if(items[i] < items[i+1]):
      
      k = i
      
  if k is None:
    
    # items is maximal. We need to wrap around
    
    return None
  
  # Find new pivot
  
  for i in range(k, n):
    
    if(items[k] < items[i]):
      
      l = i
      
  # Swap pivot
  
  items[k], items[l] = items[l], items[k]
  
  # Reverse suffix
  
  for i in range(k+1, int((k+1+n)/2)):
    
    items[i], items[n-i] = items[n-i], items[i]
    
  return items



permutation = [1,2,3,4,5,6,7,8,9,10]

while permutation != None:
  
    print(permutation)
    
    permutation = next_permutation(permutation)







