# Copyright 2020, Sorren Chandra, All rights reserved

import os
import csv
from itertools import zip_longest
from itertools import izip
from database_exceptions import *

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
            os.remove(self.path)
        except FileNotFoundError:
            raise FileNotFoundError

    def read(self):

        try:
            with open(self.path,"r") as f:
                reader = csv.reader(f)
                for line in reader:
                    print(line)
                f.close()
        except FileNotFoundError:
            raise FileNotFoundError

    def addfields(self,*args): 
        
        datafield = []
        
        if os.path.exists(self.path) == True:

            with open(self.path,"r") as f: 
                reader = list(csv.reader(f))
                for line in reader:
                    datafield.extend(line)
                f.close()

        elif os.path.exists(self.path) == False:
            raise csvDoesNotExist()
        
        for arg in args:
            datafield.append(arg)

        with open(self.path,"a") as f:
            writer = csv.DictWriter(f,fieldnames=datafield)
            writer.writeheader()
            f.close()
            print("Success!")
    
    def add_data(self,header,*args):

        # Need to create a way to dynamically find exsisting headers
        # if header is in csv file; continue; if not; raise error

        datalist = [] # initialize inital data list 
        for arg in args: # Append N number of user arguments to data list
            datalist.append(arg)
        d = datalist
        writedata = zip_longest(*d, fillvalue='')

        with open(self.path,'w', encoding="ISO-8859-1", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(writedata)
                