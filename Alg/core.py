
from Api import api


class meta(type):

    def __new__(cls,name,bases,body,**kw):

        cls=type.__new__(cls,name,bases,body,**kw)

        cls.body=body

        cls.name=name

        cls.bases=bases

        cls.kwds=kw

        return cls


class derived(api,metaclass=meta):

        pass

    

class foo(derived):

    def Foo(self):

        pass

    def Bar(self):

        pass

f=foo()












        
