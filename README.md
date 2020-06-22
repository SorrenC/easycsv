![Alt text](logo.png?raw=true "Title")

[![forthebadge made-with-python](https://img.shields.io/badge/Python-v3.8-blue)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/SorrenC/easycsv/blob/master/LICENSE)
![shields.io](https://img.shields.io/badge/Status%20-Work%20In%20Progress-red)

Provides a group of functions for simple .csv editing. The inital need for such a script was to provide easy csv functions to help automate testing procedures. 
This project is a work in progress 


Copyright © 2020 Sorren Chandra 

# Getting Started 
Start by cloning the repository 
```
git clone *url*
```
import database_edit.py
```
from database_edit import *
```
# Usage 
Create a database obejct. Pass in the path and name of an existing csv file or one you wish to create 
```
d = database(r'\path\to\location','filename')
```
## Functions 
create: creates a .csv file at the specified location with the given name
```
d.create()
```
delete: if said .csv exists, deletes the fi;e
```
d.delete()
```
addfields: adds headers to the first row. Takes N number of arguments
```
d.addfields('Header1','Header2','Header3',...,'HeaderN')
```
read: Reads the .csv 
```
d.read()
```
