

class base:

        registered_subclasses={}

        _counter_key=0

        comp=lambda cls_name:[key for key,val in cls_name.__dict__.items()] 


        def __new__(cls, **kwds):

        	if not hasattr(cls,'__all_constraints__'):

        		raise TypeError("You must set the constraints of your derived class using '__all_constraints__ class variable!")
                        

        	else:

        		for i in cls.__all_constraints__:

        			if not hasattr(cls,i):

        				x=base.comp(cls)

        				constraint='''class '{}' does not have some or any of the following method(s),which are required:{}.It has the following attributes:{}'''.format(cls.__name__,cls.__all_constraints__,x[1:-1])
        				
        				raise TypeError(constraint)

        		cls.register_subclasses(base,cls)
                        
        		return super().__new__(cls, **kwds)

        def register_subclasses(self,subclass):

                "registers subclasses into a dict object"

                if not issubclass(subclass,base):

                        return subclass

                if issubclass(base,subclass):

                        raise RuntimeError("Cannot create inheritance loop")

                k=base.comp(subclass)

                if subclass.__name__ in base.registered_subclasses:

                        raise Exception("Subclass {} already exists in registry!".format(subclass.__name__))

                
                base.registered_subclasses[subclass.__name__]=k[1:-1]

                base._counter_key+=1


                return base.registered_subclasses
                        

                                

                                

                        

        	
