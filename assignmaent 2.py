#!/usr/bin/env python
# coding: utf-8

# In[1]:


#program to print marks sheet using grades
s1=int(input("Enter marks of english:"))
s2=int(input("Enter marks of urdu:#"))
s3=int(input("Enter marks of islamiat:"))
s4=int(input("Enter marks of mathematics:"))
s5=int(input("Enter marks of sindhi:"))
avg=(s1+s2+s3+s4+s5)/500
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")


# In[25]:


#program to check even or odd
num = int(input("Enter your number: "))
m = num % 2
if m > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
        


# In[23]:


#program to print the lenght of the list
list=['a','b','c','d','e']
print "Lenght of list:",len(list)


# In[10]:


#program to sum all number in list
list=[1,34,67,87]
total=sum(list)
print"Sum of All number",total


# In[11]:


#program to print largest num in a given list
list=[23,5,66,78,9]
print "Largest number in a given list:",max(list)


# In[18]:


#program to print all less num from 5
list=[1,26,3,43,5]
for num in list:
    if num <5:
        print(num)


# In[ ]:




