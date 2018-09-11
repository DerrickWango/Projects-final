

def links(list1,list2):

    if len(list1) != len(list2):

        print('''Error! lists not the same length.\nYour first list is {} characters and your second list is {} characters!'''.format(len(list1),len(list2)))

    else:

        y=list2

        x=list1

        z=zip(x,y)

        lst=[]

        dct={}

        for i in z:

            lst.append(i)

        for x in lst:

            dct[x[0]]=x[1]

        print(dct)













    

    

    
