#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

fhand=open('football.csv')
data=[]
linecount=0
for line in fhand:
    linecount+=1
    if linecount>1:
        line=line.rstrip()
        data.append(line.split(','))
data=sorted(data,key=lambda data: abs(int(data[5])-int(data[6])))
print data[0][0]

#Not the most elegant solution but up and running. I want to learn more about the csv module but wasn't finding
#the documentation online to be overly helpful. Directions to  further resources are much appreciated.
import csv

  def read_data(data):
   # COMPLETE THIS FUNCTION

  def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

  def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION
