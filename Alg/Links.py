

from Selection_sort import selection_sort

def links(list1,list2):


    if len(list1) != len(list2):

        print('''Error! lists not the same length.\nYour first list is {} characters and your second list is {} characters!'''.format(selection_sort.length(list1),selection_sort.length(list2)))

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

        return dct




names=['Derrick','Warren','Ann','Kingboy','Carollyn','Benson','Mary','Teddy','Justin','Loise','Gina','Andrew','Vick',

     'Samuel','Patricia','Washington','James','Christine','Lavender','Roy','David','Patsy','Ed','Philip','Cornellius',

     'Grace','Daphine','Zazi','Yvonne','Zuenna','Eric','Aden','Joe','Noel','Charles','Evans','Clinton','Paul','Simon',

     'Daniel','Janet','Maria','Joab','Ezekiel','Ezra','John','Moana','Nancy','Ivan','Edwin','Hillary','Sean','Phoebe',

     'Avan','Nina','Matilda','Elodie','Rahab','Keziah','Doreen','Jay','Enoch','Theodore','Mitchelle','Jackson','Lori',

     'Roxanne','Maureen','Everlyn','Esther','Francis','Norah','Joyce','Magdaline','Jacqline','Barrack','Betty','Saul',

     'Alan','Renny','Bill','William','Diana','Emma','Emm','Jo','Ryan','Nicole','Sophia','Donald','Luke','Edward','Bo',

     'Joel','Madilyn','Anastacia','Doug','Susan','Taby','Sharon','Bob','Fabiana','Shane','Mathew','Jason','Mark','Ty',

     'Abu','Timothy','Sarah','Faith','Bryan','Bernice','Elijah','Alvin','Yvette','Angela','Miriam','Adam','Lisa','An',

     'Cathryn','Emmanuel','Keith','George','Hellen','Jessy','Solomon','Job','Derek','Felicia','Keisha','Leah','Sylvia',

     'Chandler','Vanessa','Kacy','Victoria','Elizabeth','Laureen','Vincent','Elise','Lydia','Thomas','Marques','Beryl',

     'Vivian','Rick','Ben','Gerald','Nathan','Annabell','Damaris','Henry','Leonardo','Ivy','Nicholas','Morris','Wendy',

     'Gladwell','Rose','Branston','Rebecca','Cynthia','Moses','Peter','Anthony','Jack','Lenny','Isaac','Travis','Noah']


srt=selection_sort(names).sort('a')

num=len(names)

lst=[i for i in range(1,num+1)]
    
res=links(lst,srt)

print(res)















