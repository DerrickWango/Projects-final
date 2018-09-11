
def num_name(lst):

    dct_ones={

        'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0,

        'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19

        }

    dct_tens_only={'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19}

    dct_tens={

        'ten':10,'twenty':20,'thirty':30,'fourty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90

        }

    dct_hundred_n_beyond={

        'hundred':100,'thousand':1000,'million':1000000,'billion':1000000000,'trillion':1000000000000

        }

    for i in lst:

        if i<=19:

            for x in dct_ones.values():

                if i is x:

                    for a in dct_ones.keys():

                        if dct_ones[a]==x:

                            print('{} : This is number {}'.format(i,a))
                            

        if i>=20 and i<=99:

            for x_h in dct_tens.values():

                if i>=x_h and i<=x_h+10:

                    for a_h in dct_tens.keys():

                        if dct_tens[a_h]==x_h:

                            for o_h in dct_ones.keys():

                                if dct_ones[o_h]==(i-x_h):

                                    if (i-x_h)==0:

                                        print('{}: This is number {}'.format(i,a_h))

                                    elif (i-x_h) !=0:

                                        print('{}: This is number {} {}.'.format(i,a_h,o_h))

           

        if i>=100 and i<=999:

                   for o_t in dct_ones.keys():

                       if (dct_ones[o_t]*dct_hundred_n_beyond['hundred'])==i:

                           print('{} : This is number {} hundred.'.format(i,o_t))

                       for t_t in dct_tens.keys():

                           if (dct_ones[o_t]*dct_hundred_n_beyond['hundred']+dct_tens[t_t])==i:

                                print('{} : This is number {} hundred and {}'.format(i,o_t,t_t))

                       

                           if dct_ones[o_t]==(i-(dct_ones[o_t]*dct_hundred_n_beyond['hundred']+dct_tens[t_t])):
                                    

                                print('{} : This is number {} hundred and {} {} '.format(i,o_t,t_t,o_t))

                        
                       
                           
                           for o_t_t in dct_ones.keys():

                               if dct_ones[o_t] != dct_ones[o_t_t] and (dct_ones[o_t]*dct_hundred_n_beyond['hundred']+dct_tens[t_t]+dct_ones[o_t_t])==i and dct_ones[o_t_t]<=9 and dct_ones[o_t_t]>0:

                                   
                                        print('{} : This is number {} hundred and {} {}'.format(i,o_t,t_t,o_t_t))



                           for t_t_t in dct_tens_only:

                                if (dct_ones[o_t]

                               


                                   


                                    

                       


                                

                       

                                                



if __name__=='__main__':

    for i in range(0,201):

        num_name([i])





























                            
            

        
    
