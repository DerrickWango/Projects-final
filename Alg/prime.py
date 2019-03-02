

def caps(string):

    dct={'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K'

        ,'l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V'

        ,'w':'W','x':'X','y':'Y','z':'Z'

         }

    lst=[]
    
    for i in string:

            if i in dct:

                    i=dct[i]

                    lst.append(i)

                    string=''.join(lst)

            if i in dct.values():

                lst.insert(0,i[-1])

    return string

