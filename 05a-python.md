# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in that they both are a sequence of values. The main difference is that tuples are immutable (they cannot be changed) while lists are mutable. As a result, tuples should always be used as keys in dictionaries. This is to prevent reassigning the key in a dictionary which would cause an error in the hash table. See page 106.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets in python are similar in that they both contain a sequence of values. Lists are ordered (by their index number) while sets are unordered. Sets are also required to have no duplicates. As a result, additional mathematical ooperations are available for sets including union and intersect. I have also read that sets are hashable. I take this to also mean that sets are immutable, for as discussed in dictionaries having mutable keys will cause problems with the hash function.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda allows one to define a temporary "throw-away" function. This allows one to write more concise code by embedding functions. An example of using lambda within sorted is useful when trying to sort a tuple or nested list. Here is an example involving a mock database:

>>>basic_info=[('Matt','Queens',26),('Jordan','Queens',27),('Amit','Manhattan',32)]  
>>>sorted(basic_info,key=lambda age: age[2])

>>In this case the tuple is already sorted by age, but in general the lambda function would allow sorted to arrange the entries by the jth entry of every row.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow one to loop a function over a list, or apply a function to certain elements of a list. Similarly, the map function itself applies a function to every ith element of a list, while the filter function apply a function to all elements of a list that meets a certain criterion and returns a list of the results that were passed through the function.  
A basic mathematical example might be generating the first 10 perfect squares:
>>>y= (i**2 for i in range (1,11))  
>>>print list(y)

>>It should be noted here that simply trying 'print y' yields a generator object not the desired list itself. I am still unsure of why this is.

>>To produce the same list of the first 10 perfect squares using map (and lambda) one could do the following:  
>>>y=map(lambda x:x**2,range(1,11))  
>>>print y  
>>A really basic example of list comprehension versus filter might be generating the multiples of five from 1 to 100:  
>>>y=(y for y in range(1,101) if y%5==0)  
>>>print y  
>>>print filter(lambda x:x%5==0,range(1,101))  

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>>937 days, 0:00:00

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days, 0:00:00

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days, 0:00:00

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





