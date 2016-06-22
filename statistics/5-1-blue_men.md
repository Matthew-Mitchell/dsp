[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>def ftin2cm(feet,inches):  
    totinches=feet*12+inches  
    cm=totinches*2.54  
    return cm  
lowercm=ftin2cm(5,10)  
uppercm=ftin2cm(6,1)  
dist.cdf(uppercm)-dist.cdf(lowercm)
