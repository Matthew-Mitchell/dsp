# Hint:  use Google to find python function
from datetime import datetime
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
print datetime.strptime(date_stop,'%m-%d-%Y')-datetime.strptime(date_start,'%m-%d-%Y')  
####b)  
date_start = '12312013'  
date_stop = '05282015'  
print datetime.strptime(date_stop,'%m%d%Y')-datetime.strptime(date_start,'%m%d%Y')  
####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
print datetime.strptime(date_stop,'%d-%b-%Y')-datetime.strptime(date_start,'%d-%b-%Y')

#I did this using incremental development, originally reassigning date_start and date_stop as datetime objects using datetime.strptime and then calculating the change using a seperate variable. Here I have consolidated the code into one line.
