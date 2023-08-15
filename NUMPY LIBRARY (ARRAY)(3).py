# NUMPY 

NUMPY is a general purpose array processing package . It provides a high performance multi dimensional objects and tools for working with these arrays.....it is the fundamental package for scientific computing with python.....


why we can import numpy packages.....this is beause that there are a lot of mathemtical tools like sin theta ...cos theta or other goemetric figures ...itr does not support by the pythomn....like pi ...it is not supported by the libraries of python...so you should import it first....
RTry to write in command...............conda install numpy...this will install numpy in your jptier book...please use this commando when you have not installed numpy in your computer....then simply import it as.....import numpy as np.............

# What is an array

An array is a structure that stores values of same data type .... In python ...this is the manin difference between arrays and lists....while python  list contains values corrosponding to different types , arrrays in python can only contains values corrosponding to same data types....

import numpy as np

np.pi
###Your numpy successfully added in your pythons.....

np.cos(34)
### this is the syntax of numpy.....

First of all we can start with the first dimensional array and then add two and multi dimesnioanl array ...


## Define the array...
## print type of an array
my_lst=[1,2,3,4,5]
arr=np.array(my_lst)
### this is important to note that you have storarray in my_lst ..then store the whole function in the
## arr.......
type(arr)

arr

arr.shape
## this inbuilt function will give us information about the dimension of an array....since there are 
5 rows ..so it is one dimesional array....

## No we can produce multi diemesional array.....
lst1=[1,2,3,4,5]
lst2=[4,3,4,5,2]
lst3=[3,2,3,3,3]
arr=np.array([lst1,lst2,lst3])
arr
## this is the multi diemsional array....
### Here in the given below result there are tow opening and two closing bracets..so it si two...
##dimesnioanl array .....but if there are one opeing and one closing then it will be single dimesioanl..


arr.shape
## this is two dimensional array....

arr.reshape(5,3)
## Here we only change the shpae of the array..it will take an elements in the sequenc and arrange it in
## the demanding order.....if we select an order to reshape the array as (5,4)..it will give an error..
###because there are 15 elements..so be careful...

arr.reshape(1,15)

# INDEXING ...

Accessing elements of an array....

arr=np.array([1,2,3,4,5,6,7,8,9])
arr

arr[3]
## Index start from 0......this is for dimesion.....

arr=np.array([lst1,lst2,lst3])
arr
####For finding the elements of two dimesional array....

arr[:,:]
##This syntax means that we can take the whole matrix...for first colon..it will take the whole row and 
##for second it will take whole coloumns,.....

arr[0:2]
## This means that it will take from 0 row to n row....beause i need first two rows....

arr[0:2,0:2]

arr[:,:]

arr[1:,3:] ### Here i need the second and third row and 4th and 5th coloumns..
## Kindly practice of these all things....

### There is another inbuilt function...which is arange....it will arrange the elements in the sequence
arr=np.arange(0,10,step=2)
arr
## This will take array of one dimesnion...

arr=np.arange(0,10,step=2)
arr
## Check the syntax.....it will give you a sequence of elements..

###There is another function....
np.linsapce





































