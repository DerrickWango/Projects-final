

def numnameint(*args):

        '''

	    A function that returns a number in words

	     usage:

	    num_name(args)

        '''

        dct_ones={

        'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0,

        'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19

        }


        dct_tens={

        'ten':10,'twenty':20,'thirty':30,'fourty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90

        }

        dct_hundred_n_beyond={

        'hundred':100,'thousand':1000,'million':1000000,'billion':1000000000,'trillion':1000000000000

        }

       #====================================================================The code======================================================================#

        for i in args:

            if type(i) is not int:

                if type(i) is not float:

                    raise TypeError("Arguments must be of type 'int' or 'float',got '{}'".format(type(i).__name__))
            

            if i<=dct_ones['nineteen']:

                        for a in dct_ones.keys():

                            if dct_ones[a]==i:

                                 return '{}'.format(a)

            if i==dct_tens['ten']:

                    return "ten"
                                

            if i>=dct_tens['twenty'] and i<=(dct_hundred_n_beyond['hundred']-dct_ones['one']):

                for t_h in dct_tens.keys():

                        if dct_tens[t_h]==i:

                                return '{}'.format(t_h)

                        for o_h in dct_ones.keys():

                                if (dct_tens[t_h]+dct_ones[o_h])==i and dct_ones[o_h]>dct_ones['zero'] and dct_ones[o_h]<=dct_ones['nine']:

                                        return '{} {}'.format(t_h,o_h)


            if i>=dct_hundred_n_beyond['hundred'] and i<=(dct_hundred_n_beyond['thousand']-dct_ones['one']):

                for o_t in dct_ones.keys():

                           if (dct_ones[o_t]*dct_hundred_n_beyond['hundred'])==i:

                                  return '{} hundred'.format(o_t)

                           for o_t_t in dct_ones.keys():

                               if ((dct_ones[o_t]*dct_hundred_n_beyond['hundred'])+dct_ones[o_t_t])==i and dct_ones[o_t_t]>dct_ones['zero']:

                                   return "{} hundred and {}".format(o_t,o_t_t)
                               

                           for t_t in dct_tens.keys():

                               if ((dct_ones[o_t]*dct_hundred_n_beyond['hundred'])+dct_tens[t_t])==i:

                                    return "{} hundred and {}".format(o_t,t_t)

                               for o_t_t_t in dct_ones.keys():

                                   if ((dct_ones[o_t]*dct_hundred_n_beyond['hundred'])+dct_tens[t_t]+dct_ones[o_t_t_t])==i and dct_ones[o_t_t_t]>dct_ones['zero'] and dct_ones[o_t_t_t]<dct_tens['ten'] and dct_tens[t_t]>dct_tens['ten']:

                                       return "{} hundred and {} {}".format(o_t,t_t,o_t_t_t)

            if i>=dct_hundred_n_beyond['thousand'] and i<=(dct_hundred_n_beyond['million']-dct_ones['one']):

                  for o_th in dct_ones.keys():

                        if (dct_ones[o_th]*dct_hundred_n_beyond['thousand'])==i:

                            return '{} thousand'.format(o_th)

                        for o_thh in dct_ones.keys():

                            if ((dct_ones[o_th]*dct_hundred_n_beyond['thousand'])+dct_ones[o_thh])==i and dct_ones[o_thh]>dct_ones['zero']:

                                return '{} thousand and {}'.format(o_th,o_thh)

                            for t_th in dct_tens.keys():

                                if ((dct_ones[o_th]*dct_hundred_n_beyond['thousand'])+(dct_tens[t_th]+dct_ones[o_thh]))==i and dct_ones[o_thh]>dct_ones['zero'] and dct_ones[o_thh]<=dct_ones['nine'] and dct_tens[t_th]>dct_tens['ten']:

                                    return "{} thousand and {} {}".format(o_th,t_th,o_thh)

                        for t_thh in dct_tens.keys():

                            if ((dct_ones[o_th]*dct_hundred_n_beyond['thousand'])+dct_tens[t_thh])==i :

                                return "{} thousand and {}".format(o_th,t_thh)

                        for o_thhh in dct_ones.keys():

                            for t_thhh in dct_tens.keys():
                        

                                for o_thhhh in dct_ones.keys():
                                    
                                    if ((dct_ones[o_th]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhh]*dct_hundred_n_beyond['hundred'])+(dct_tens[t_thhh]+dct_ones[o_thhhh]))==i and dct_tens[t_thhh]>dct_tens['ten'] and dct_ones[o_thhhh]>dct_ones['zero'] and dct_ones[o_thhhh]<=dct_ones['nine'] and dct_ones[o_thhh]>dct_ones['zero'] and dct_ones[o_thhh]<=dct_ones['nine']:

                                        return "{} thousand {} hundred and {} {}".format(o_th,o_thhh,t_thhh,o_thhhh)

                        for o_thhhhh in dct_ones.keys():

                            if ((dct_ones[o_th]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhh]*dct_hundred_n_beyond['hundred']))==i and dct_ones[o_thhhhh]<=dct_ones['nine'] and dct_ones[o_thhhhh]>dct_ones['zero']:

                                return " {} thousand {} hundred".format(o_th,o_thhhhh)


                            for o_thhhhhh in dct_ones.keys():

                                if ((dct_ones[o_th]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhh]*dct_hundred_n_beyond['hundred'])+dct_ones[o_thhhhhh])==i and dct_ones[o_th]>dct_ones['zero'] and dct_ones[o_thhhhhh]>dct_ones['zero'] and dct_ones[o_thhhhh]>dct_ones['zero'] and dct_ones[o_thhhhh]<=dct_ones['nine']:

                                    return " {} thousand {} hundred and {}".format(o_th,o_thhhhh,o_thhhhhh)

                            for t_thhhh in dct_tens.keys():

                                if ((dct_ones[o_th]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhh]*dct_hundred_n_beyond['hundred'])+dct_tens[t_thhhh])==i and dct_ones[o_th]>dct_ones['zero'] and dct_ones[o_thhhhh]<=dct_ones['nine'] and dct_ones[o_thhhhh]>dct_ones['zero']:

                                        return " {} thousand {} hundred and {}".format(o_th,o_thhhhh,t_thhhh)


                  for t_thhhhh in dct_tens.keys():

                      if (dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])==i:

                                return "{} thousand".format(t_thhhhh)

                      for o_thhhhhhh in dct_ones.keys():

                          if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhh]*dct_hundred_n_beyond['thousand']))==i and dct_ones[o_thhhhhhh]>dct_ones['zero'] and dct_ones[o_thhhhhhh]<=dct_ones['nine'] and dct_tens[t_thhhhh]>dct_tens['ten']:

                                    return '{} {} thousand'.format(t_thhhhh,o_thhhhhhh)

                          for o_thhhhhhhh in dct_ones.keys():

                                  if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhhh]*dct_hundred_n_beyond['hundred']))==i and dct_ones[o_thhhhhhhh]<=dct_ones['nine'] and  dct_ones[o_thhhhhhh]>dct_ones['zero'] and dct_ones[o_thhhhhhh]<=dct_ones['nine'] and dct_tens[t_thhhhh]>dct_tens['ten']:

                                                return '{} {} thousand {} hundred'.format(t_thhhhh,o_thhhhhhh,o_thhhhhhhh)


                                  if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhhh]*dct_hundred_n_beyond['hundred']))==i and dct_ones[o_thhhhhhhh]>dct_ones['zero']:

                                          return "{} thousand {} hundred".format(t_thhhhh,o_thhhhhhhh)

                                  for o_tx in dct_ones.keys():

                                          if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhhh]*dct_hundred_n_beyond['hundred'])+dct_ones[o_tx])==i and dct_ones[o_tx]>dct_ones['zero'] and dct_ones[o_thhhhhhhh]<=dct_ones['nine'] and  dct_ones[o_thhhhhhh]>dct_ones['zero'] and dct_ones[o_thhhhhhh]<=dct_ones['nine'] and dct_tens[t_thhhhh]>dct_tens['ten'] :
                                                  
                                                     return '{} {} thousand {} hundred and {}'.format(t_thhhhh,o_thhhhhhh,o_thhhhhhhh,o_tx)

                                          if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhhh]*dct_hundred_n_beyond['hundred'])+dct_ones[o_tx])==i and dct_ones[o_thhhhhhhh]>dct_ones['zero'] and dct_ones[o_tx]>dct_ones['zero']:

                                                     return "{} thousand {} hundred and {}".format(t_thhhhh,o_thhhhhhhh,o_tx)
                                                
                                  for o_txh in dct_ones.keys():

                                           if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhhh]*dct_hundred_n_beyond['hundred'])+dct_ones[o_txh])==i and dct_ones[o_thhhhhhhh]<=dct_ones['nine'] and  dct_ones[o_thhhhhhh]>dct_ones['zero'] and dct_ones[o_thhhhhhh]<=dct_ones['nine'] and dct_tens[t_thhhhh]>dct_tens['ten'] and dct_ones[o_txh]>dct_ones['zero']:

                                                return '{} {} thousand {} hundred and {}'.format(t_thhhhh,o_thhhhhhh,o_thhhhhhhh,o_txh)


                                           for t_thhhhhh in dct_tens.keys():

                                                   if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_thhhhhhhh]*dct_hundred_n_beyond['hundred'])+(dct_tens[t_thhhhhh]+dct_ones[o_txh]))==i and dct_ones[o_thhhhhhhh]<=dct_ones['nine'] and  dct_ones[o_thhhhhhh]>dct_ones['zero'] and dct_ones[o_thhhhhhh]<=dct_ones['nine'] and dct_tens[t_thhhhh]>dct_tens['ten'] and dct_ones[o_txh]>dct_ones['zero'] and dct_ones[o_thhhhhhhh]>dct_ones['zero']:

                                                           return '{} {} thousand {} hundred and {} {}'.format(t_thhhhh,o_thhhhhhh,o_thhhhhhhh,t_thhhhhh,o_txh)

                      for o_txhh in dct_ones.keys():


                                if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+dct_ones[o_txhh])==i and dct_ones[o_txhh]>dct_ones['zero']:

                                        return "{} thousand and {}".format(t_thhhhh,o_txhh)

                      for t_thhhhhhh in dct_tens.keys():


                              if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+dct_tens[t_thhhhhhh])==i:



                                      return "{} thousand and {}".format(t_thhhhh,t_thhhhhhh)

                              for o_txhhh in dct_ones.keys():

                                      if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+(dct_tens[t_thhhhhhh]+dct_ones[o_txhhh]))==i and dct_ones[o_txhhh]>dct_ones['zero'] and dct_ones[o_txhhh]<=dct_ones['nine']:

                                             return "{} thousand and {} {}".format(t_thhhhh,t_thhhhhhh,o_txhhh)

                      for o_txhhhh in dct_ones.keys():

                              for o_txhhhhh in dct_ones.keys():

                                   if ((dct_tens[t_thhhhh]*dct_hundred_n_beyond['thousand'])+(dct_ones[o_txhhhh]*dct_hundred_n_beyond['thousand'])+dct_ones[o_txhhhhh])==i and dct_ones[o_txhhhh]>dct_ones['zero'] and dct_ones[o_txhhhhh]>dct_ones['zero'] and dct_ones[o_txhhhh]<=dct_ones['nine'] and dct_tens[t_thhhhh]>dct_tens['ten']:

                                        return '{} {} thousand and {}'.format(t_thhhhh,o_txhhhh,o_txhhhhh)
                                           

                  for o_txhhhhhh in dct_ones.keys():
        
                      if (dct_ones[o_txhhhhhh]*dct_hundred_n_beyond['hundred']*dct_hundred_n_beyond['thousand'])==i:

                          return "{} hundred thousand".format(o_txhhhhhh)







              



def numnamefloat(*args):

    for i in args:

          numstr=str(i)

          split=numstr.split('.')

          b4pt=split[0]

          afpt=split[1]

          ptnums=[numnameint(int(i)) for i in afpt]

          new_pt_str=(numnameint(int(b4pt)) + ' point '+(' '.join(ptnums)))

          return new_pt_str




def numname(*args):

        for i in args:

            if type(i) is float:

                return numnamefloat(i)

            else:

                return numnameint(i)

                        





















                            
            

        
    
