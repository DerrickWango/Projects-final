import sqlite3

import random

import re

import os





class Models:


    def __init__(self,database_dir):

       if not  os.path.exists(database_dir):

             os.mkdir(database_dir)

       with sqlite3.connect('{}/{}.db'.format(database_dir,database_dir)) as db:

                    self.cursor=db.cursor()

       self.db_obj=db


    def close(self):

        return self.db_obj.close()
    

    def Re(self,result):

        return re.sub("[()'',]","",str(result))


    def schema(self):

        parent_schema=('''CREATE TABLE IF NOT EXISTS Categories(

                            category_id INTEGER PRIMARY KEY NOT NULL,

                            category_name TEXT NOT NULL);''')

        child_schema=('''CREATE TABLE IF NOT EXISTS Data(

                            id INTEGER PRIMARY KEY NOT NULL,

                            entry_name TEXT NOT NULL,

                            ref_no INTEGER NOT NULL,

                            entry_description TEXT NOT NULL,

                            entry_id INTEGER NOT NULL DEFAULT 0 REFERENCES Categories(category_id)

                            ON UPDATE CASCADE

                            ON DELETE SET DEFAULT

                            
                            );''')

        try:

            self.cursor.execute(parent_schema)

            self.cursor.execute(child_schema)

        except Exception as e:

            print(e)

            

        default_value=('''INSERT OR IGNORE INTO Categories VALUES(0,'No category selected')''')


        self.cursor.execute(default_value)

        self.db_obj.commit()
        

    def insert_parent(self,category_ref_no,entry_description,error=None):

        try:

            if len(entry_description) !=0:

                parent_schema=('''INSERT INTO Categories(category_id,category_name)

                                        VALUES(?,?)''')

                self.cursor.execute(parent_schema,[(category_ref_no),(entry_description)])

                self.db_obj.commit()

            else:

                return error

        except Exception as e:

            import time

            import sys

            timestr = time.strftime("Error occured on %Y//%m//%d----at-----%H::%M::%S.")

            x=open('logs/user_errors.txt','a')

            print(e,"------------",timestr,file=x,end='\n\n\n')

            x.close()

            return error,sys.exit()

            

        parent_schema2=('''UPDATE Categories SET category_name=UPPER(category_name) WHERE category_name=?''')

        self.cursor.execute(parent_schema2,[(entry_description)])

        self.db_obj.commit()

        

    def insert_child(self,entry_name,start,stop,category_ref_no=0,error=None):

        ref=random.randint(start,stop)

        if len(entry_name) !=0:

            found_record=0

            while found_record==0:
                

                check=('''SELECT entry_name FROM Data WHERE entry_name=?''')

                self.cursor.execute(check,[(str(entry_name).upper())])

                result_check=self.cursor.fetchall()

                if result_check:


                    return error

                else:

                    found_record=1
   
                select=('''SELECT DISTINCT category_name FROM Categories WHERE category_id=?''')

                self.cursor.execute(select,[(category_ref_no)])

                result=self.cursor.fetchone()

                clean_result=re.sub("[(),'']","",str(result))

                select_id=('''SELECT category_id FROM Categories WHERE category_id=?''')

                self.cursor.execute(select_id,[(category_ref_no)])

                result2=self.cursor.fetchone()

                clean_result2=self.Re(result2)

                if str(category_ref_no) in clean_result2:

                    child_schema=('''INSERT OR IGNORE INTO Data(entry_name,ref_no,entry_description,entry_id)

                                            VALUES(?,?,?,?)''')

                    
                    self.cursor.execute(child_schema,[(str(entry_name).upper()),(ref),(clean_result),(category_ref_no)])

                    self.db_obj.commit()

                else:

                    child_schema=('''INSERT OR IGNORE INTO Data(entry_name,ref_no,entry_description,entry_id)

                                            VALUES(?,?,?,?)''')

                    
                    self.cursor.execute(child_schema,[(str(entry_name).upper()),(ref),('No category selected'),(0)])

                    self.db_obj.commit()

        else:

            return error

        

    def update_parent(self,new_category_name,category_name):

        #Updates category name

        parent_schema=('''UPDATE Categories SET category_name=? WHERE category_name=?''')

        self.cursor.execute(parent_schema,[(new_category_name),(str(category_name)).upper()])

        self.db_obj.commit()

        self.cursor.execute('''UPDATE Categories SET category_name=UPPER(category_name) WHERE category_name=?''',[(new_category_name)])

        self.db_obj.commit()

        #updates child category name

        parent_schema_2=('''SELECT category_name FROM Categories WHERE category_name=?''')

        self.cursor.execute(parent_schema_2,[(str(new_category_name).upper())])

        result=self.cursor.fetchone()

        clean_result=self.Re(result)

        child_schema=('''UPDATE Data SET entry_description=? WHERE entry_description=?''')

        self.cursor.execute(child_schema,[(clean_result),(str(category_name).upper())])

        self.db_obj.commit()

        

    def update_child(self,new_entry_name,entry_name,entry_description='',category_id=0,old_entry=''):

        child_schema=('''UPDATE Data SET entry_name=? WHERE entry_name=?''')

        self.cursor.execute(child_schema,[(str(new_entry_name)).upper(),(str(entry_name).upper())])

        self.db_obj.commit()

        if  entry_description != '' and category_id !=0 and old_entry !='' :

            select=('''SELECT category_name FROM Categories WHERE category_name=? OR category_id=?''')

            self.cursor.execute(select,[(str(entry_description).upper()),(category_id)])

            result=self.cursor.fetchone()

            clean_result=self.Re(result)

            self.cursor.execute('''UPDATE Data SET entry_description=?,entry_id=? WHERE entry_description=?''',[(clean_result),(category_id),(str(old_entry).upper())])

            self.db_obj.commit()

    def delete_parent(self,category_id,entry_description):

        pass

 
        
def main():
    
        '''usage :'''




        connection=Models('Jacmil supermarket records')



        connection.schema()

        connection.insert_parent(25551,'foodstuff')

        connection.insert_parent(25552,'Cleaning Products')

        connection.insert_child('Omo',3535353,2626262626,25552)



        connection.update_child('Indomine','omo',entry_description='foodstuff',category_id=2552,old_entry='household cleaning products')

        connection.update_parent('Household cleaning products','Cleaning Products')

        connection.close()

        

if __name__=='__main__':

    main()




















