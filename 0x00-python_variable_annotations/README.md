# 0x00. Python - Variable Annotations
### Type annotations in Python 3
* Since python is a dynamically typed language that allows for the initialization of variables at run-time, this means that the code is well documented with type annotations. 
	* This is done so that the type annotations provide a easy reference for all developers to understand all variables that are needed for the program to run.
Ex.
```
def greeting(name:str) -> str:
	return "Hello " + name
/* In the Fucntion greeting, name is expected to be of type str and returns a string*/
```
