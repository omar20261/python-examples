#!/usr/bin/python
print("Hello World")
raw_input("\n\nPress the enter key to exit.")

num =124               # An integer assignment
flo =3.14              # A floating point
str = "John"           # A string
Tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  ) #Tuple
List = [ 'abcd', 786 , 2.23, 'john', 70.2 ]   #List
dict = {'name': 'john','code':6734, 'dept': 'sales'} #Dictionary
#=========================================
#if True:
    #print("hello world");
#elif(True):
    #print("HA Ha Ha");
#else:
    #print "False"
#=========================================
def MyFun():
    for item in List:
        print("list item = {}").format(item);

if __name__ == "__main__":MyFun()
#=========================================
