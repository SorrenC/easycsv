# Copyright 2020, Sorren Chandra, All rights reserved

import os
import csv

class PathNotFound(Exception):
    pass

class csvAlreadyExists(Exception):
    pass

class csvDoesNotExist(Exception):
    pass

class UnknownError(Exception):
    pass

class database():

    def __init__(self,dir,filename):
        self.dir = dir
        self.filename = filename
        self.path = os.path.join(self.dir,self.filename+".csv")

    def create(self):

        if os.path.exists(self.dir) == True:
            pass
        elif os.path.exists(self.dir) == False:
            os.mkdir(self.dir)
        else:
            raise UnknownError

        if os.path.exists(self.path) == True:
            raise csvAlreadyExists()
        elif os.path.exists(self.path) == False:
            pass

        with open(self.path,"w+") as csv_file:
            csv_file.close()
            print(".csv created")

    def delete(self):

        try:
            os.remove(os.path.join(self.dir,self.filename+'.csv'))
        except FileNotFoundError:
            raise FileNotFoundError

    def read(self):

        try:
            with open(os.path.join(self.dir,self.filename+'.csv'),"r") as f:
                reader = csv.reader(f)
                for line in reader:
                    print(line)
                f.close()
        except FileNotFoundError:
            raise FileNotFoundError

    def addfields(self,*args): 
        
        datafield = []

        # Need to check if there is already headers, append to new headers 
        
        if os.path.exists(os.path.join(self.dir,self.filename+'.csv')) == True:

            with open(os.path.join(self.dir,self.filename+'.csv'),"r") as f: # Check if csv already has headers, add existing headers to list [NOT WORKING NEED TO FIX]
                reader = csv.reader(f)
                for line in reader:
                    datafield.append(line)
                f.close()

        elif os.path.exists(os.path.join(self.dir,self.filename+'.csv')) == False:
            raise csvDoesNotExist()
        
        for arg in args:
            datafield.append(arg)

        with open(os.path.join(self.dir,self.filename+'.csv'),"a") as f:
            writer = csv.DictWriter(f,fieldnames=datafield)
            writer.writeheader()
            f.close()
            print("Success!")
    
    def add_data(self,header,*args):
        data = []
        