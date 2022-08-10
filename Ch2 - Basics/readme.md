# run in file  dont excute when import

```python 
if __name__ == "__main__": # run inside selffile   except main    if import  name file 
    main()
```
# variable 
```python
# to access a member of a sequence type, use []
print(mylist[2])
print(mytuple[1])
# use slices to get parts of a sequence
print(mylist[1:4:2])
# you can use slices to reverse a sequence
print(mylist[::-1])
# dictionaries are accessed via keys
print(mydict["one"]) 
# ERROR: variables of different types cannot be combined
#print ("string type " + 123)
print ("string type " + str(123))
# Global vs. local variables in functions
def someFunction():
    #global mystr
    mystr = "def"
    print (mystr)
someFunction()
print (mystr) 
del mystr # delete declare mystr 
print (mystr)
```
# switch case

```python
   # new in Python 3.10
    # the match-case construct can be used for multiple comparisons
    value = "three"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3, 4)
        case _:
            result = -1
    print(result)
 ```
 
 
