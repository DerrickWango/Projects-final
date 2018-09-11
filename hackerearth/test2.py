import math


def div(x,y):

    if ((x/y)- int(('%.0f'%(x/y)))) >= 0.5:

        return math.ceil(x/y)

    else:

        return round(x/y)





def main(*args):

    ans=0

    num=1

    X=[*args]

    Y=[]

    for i in X:

        result=div(X[num],i)

        Y.append(result)

        print(Y)

if __name__=="__main__":

    main(1,2,3)
