from Numname import numname


def length(array):

    counter=0

    for x in array:

        counter+=1

    return counter



def xrange(*args:'xrange(stop) defaults to start=0,step=1'):

    """An implementation of the python 2 xrange() function"""

    start,step=-1,1

    lst1=[]

    for i in args:

        if type(i) is not int:

            return "Cannot interprate '{}' as integer!".format(type(i).__name__)

    if length(args)<1:

        return "c_range Must have at least one argument"

    if length(args)==1:

        stop=(args[0]-step)

        while start<stop:

            start+=(step)

            lst1.append(start)

        return lst1

    if length(args)==2:

        start=(args[0]-step)

        stop=(args[1]-step)

        while start<stop:

            start+=(step)

            lst1.append(start)

        return lst1

    if length(args)==3:

        step=args[2]

        if step==0:

            return "Argument 3 should not be {}!".format(numname(step))

        start=(args[0]-(step))

        stop=(args[1]-(step))

        if start<stop:

            while start<stop:

                if start<stop:

                    start+=step

                    lst1.append(start)
                    
        else:

            while start>stop and step<0:

                start+=step

                lst1.append(start)

        return lst1

    if length(args)>3:

        return "Expected at most {} arguments,got {}".format(numname(3),numname(length(args)))


    

        
        

    
