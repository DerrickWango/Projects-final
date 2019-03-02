import time



def exponentiate(x,y):

    return x**y

def add(x,y):

    return x+y

def subtract(x,y):

    return x-y

def divide(x,y):

    return x/y

def multiply(x,y):

    return x*y


def prime(n,y=None):

    if n==1:

        print("({} is special)".format(n))

        return False

    for x in range(2,n):

        if n%x==0:

                print("({} is equal to {} x {})".format(n,x,n//x))

                return False
                
    else:

        print("({} is prime)".format(n))

        return True


def mapping(funcs,items,items2):

            for x in items:

                for y in items2:

                    def process(proc):
                        
                            print("In function",funcs[proc].__name__,"the result is",funcs[proc](x,y),"with parameters",x,"and",y,".")
                            

                    for i in range(0,len(funcs)):

                        process(i)
                        
                        print("Time elapsed in process {}: {}".format(i,time.process_time()))

                        


mapping([exponentiate,multiply,add,divide,subtract],[2.06,4.07,6.08,8.09,10.1,12.2,14.3,16.4,18.5,20.5,34.99,22.5,24.5],

[24,48,72,96,120,144,168,192])




    
            

        

        























        




    


    
