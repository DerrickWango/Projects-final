

class xrangeIterator:

    def __init__(self,xrange_obj):

        self._xrange_obj=xrange_obj


    def __next__(self):

        self.copy_gen=self._xrange_obj._result

        for i in self.copy_gen:

            return i
                
        raise StopIteration

class xrange:

    def __init__(self,*args):

        self._args=args

        self.start,self.step=0,1

        self._repr_string=None

        for i in self._args:

            if type(i) is not int:

                raise TypeError("Cannot interprate '{}' as integer!".format(type(i).__name__))


        if self._length(self._args)<1:

            raise TypeError( "xrange Must have at least one argument")


        elif self._length(self._args)==1:

            self.stop=self._args[0]

            self._repr_string="xrange(0,{})".format(self.stop)

            self._result=self._xrange(self.start-self.step,self.stop-self.step,self.step)

        elif self._length(self._args)==2:

            self.start=self._args[0]

            self.stop=self._args[1]

            self._result=self._xrange(self.start-self.step,self.stop-self.step,self.step)

        elif self._length(self._args)==3:

            self.step=self._args[2]

            self.start=self._args[0]

            self.stop=self._args[1]

            self._result=self._xrange(self.start-self.step,self.stop-self.step,self.step)


        else:

            raise TypeError("xrange expected at most three arguments,got {}".format(self._length(self._args)))


    def __repr__(self):

        if self._length(self._args)==1:

            return self._repr_string

        return "xrange{}".format(self._args)

    def __iter__(self):

        return xrangeIterator(self)
        

    def _length(self,n):

        counter=0

        for i in n:

            counter+=1

        return counter


    def _xrange(self,start,stop,step):

        if step==0:

                raise ValueError("Argument 3 should not be zero!")

        if start<stop and step<0:

                raise TypeError("argument 3 should not be {}".format(step))

        if start<stop:

            while start<stop:

                start+=step

                yield start
                    
        else:

            while start>stop and step<0:

                start+=step

                yield start

        


        


    
