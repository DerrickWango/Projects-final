

def presents(*args):
    
    N=[*args]
    
    R=reversed(N)
    
    A=[]
    
    for i in R:
        
        A.append(i)
        
        
    x=[a*b for a,b in zip(N,A)]
    
    print(sum(x))
    
    

if __name__=='__main__':

    presents(4,8,3,8,32,9,99,543,333,9,777,322)

