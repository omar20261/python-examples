#!/usr/bin/python
#====================================================
print("Hello World")
raw_input("\n\nPress the enter key to exit.")
#==================== Data Type =====================
MyInteger = 124               # int ==> An integer assignment  
MyFloat = 3.14              # float ==> A floating point
MyStr = "John"           # str ==> A string
MyBool = True            # bool ==> A Boolean
MyComplex = 1j           # complex ==> lj
MyBytes = True           # bytes ==> b'Hello'
MyBytearray = bytearray(5)   # bytearray ==>  bytearray(b'\x00\x00\x00\x00\x00')
MyMemoryview = memoryview(bytes(5))  # memoryview ==> <memory at 0x00B08FA0>
MyRange = range(6) # range
MyList = [ 'abcd', 786 , 2.23, 'john', 70.2 ]   # List 
MyTuple = ( 'abcd', 786 , 2.23, 'john', 70.2  ) # Tuple
MyDict = {'name': 'john','code':6734, 'dept': 'sales'} # dict ===> Dictionary
MySet = {'name': 'john','code':6734, 'dept': 'sales'} # set ===> 
MyFrozenset = frozenset({"apple", "banana", "cherry"}) # frozenset ===> 
#=================== if ======================
if 5 > 2:print("Five is greater than two!")
#================= if elif else ========================
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#=============== function ==========================
#In Python a function is defined using the def keyword:
def MyFun():
  x = "fantastic"
  print("Python is " + x)

def my_function(fname = "Name"): # Default Parameter Value
  print(fname + " Refsnes")

MyFun()
my_function()
my_function('Omar')
#=============== lambda function ==========================
x = lambda a : a + 10
x2 = lambda a, b : a * b
print('====lambda 1====> {}').format(x(5)) 
print('====lambda 2====> {}').format(x2(5,6)) 
#================= while loop ========================
i = 1
while i < 6:
  print("while loop no. {}").format(i)
  i += 1
#================= for loop ========================
for x in range(6,11):
  print("for loop no. {}").format(x)
#================= for loop 2 ========================
MyList = [ 'abcd', 786 , 2.23, 'john', 70.2 ]   # List 
for item in MyList:
  print("list item = {}").format(item)
#================= arrays ========================
#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda") # to add an element to an array.
cars.pop(1) # to remove an element from the array.
cars.remove("Ford") 
print("item no.2 in cars array  = {}").format(cars[1])
print("length of cars array  = {}").format(len(cars))
#==================================================
