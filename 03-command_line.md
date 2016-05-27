# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

'cd' #change directory  
'cd ..' #change directory up one folder  
'cd -' #change directory to previous working directory  
'mkdir <foldername>' #make a new folder/directory  
'pwd' #print working directory  
'ff' #find files anywhere in the system  
'ps -u yourusername' #lists your current processes
'grep' #search for text strings within files    
'*' #wildcard  
'rm filename' #remove specified files  
'rm *' #reomove all files within current directory  
'ctrl u' #clears current line and moves cursor to start of line  
'ctrl r' #search through previous commands  
'ctrl a' #move cursor to beginning of line  
'ctrl e' #move curosr to end of line  





---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  

`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

'ls' #list directory, Windows: dir   
'ls -a' #list all files, . current folder ..parent folder  
'ls -l' #list long format (include permissions)  
'ls-lh' #list long format with file size  
'ls -lah' #list long format of all files and file size??  
'ls -t' #sort by time and date  




---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

'ls -s' #list files sorted by size  
'ls -r' #list files in reverse specified order  
'ls -d' #list only directories  
'ls -u' #list files by access time  
'ls -c' #list files by file timestamp  


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

Run commands on the output from other command line windows/functions.  

find *.txt|xargs rm  

 

