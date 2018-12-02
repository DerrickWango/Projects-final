
class sorting:

    def __init__(self,org):

        self.org=org

        self.items=[]

        for i in self.org:

            self.items.append(i)

    #=========================Other methods================#

    def original(self):

        return self.org

    def length(self,array):

        counter=0

        for char in array:

            counter+=1

        return counter

    def c_min(self,array):

            check=0

            for i in range(self.length(array)):

                    if array[check]>array[i]:

                        array[check],array[i]=array[i],array[check]

            return array[check]

    def c_max(self,array):

        check=0

        for i in range(self.length(array)):

                    if array[check]<array[i]:

                        array[check],array[i]=array[i],array[check]

        return array[check]


    
    #==========================The algorithms=====================#


    def selection_sort(self,choice):

        sorted_list=[]

        for i in range(self.length(self.items)):

            if choice=='a':

                a=self.c_min(self.items)

            elif choice=='d':

                a=self.c_max(self.items)

            else:

                raise Exception('Options must be either "a" for ascending order or "d" for descending order')

            sorted_list.append(a)
            
            self.items.remove(a)

        for i in sorted_list:

            self.items.append(i)


        return self.items

        








        
#===================================================Test data=========================================================#



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

arr=[-25,-99,67,94,-37,83,49,-65,39,90,13,29,87,57,63,45,54,-77,88,1,3,44,32,21,91,66,51,-55,37,11,-23,22,46,0]


y=sorting(arr)

srt=y.selection_sort('a')


print(srt)
























