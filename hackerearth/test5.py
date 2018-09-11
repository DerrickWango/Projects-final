def game(index,n):

    init_prob=0.5
    
    lst=[0,1,2]

    print('original:',lst)
    
    for i in range(n):
    
        f,s,t=lst.index(0),lst.index(1),lst.index(2)
        
        lst[f],lst[s]=lst[s],lst[f]
        
        lst[s],lst[t]=lst[t],lst[s]

        print(lst)

    
    
game(1,40)
