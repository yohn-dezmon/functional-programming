# Python Functional Programming
- https://realpython.com/python-functional-programming/
- consists primarily in the evaluation of pure functions  
- computation proceeds by nested or composed function calls, without changes to state or mutable data
- transparency: purpose of a function can be seen from its inputs/outputs, not its intermediate values
- parallelizable: routines that don't cause side effects can more easily run in parallel with each other


**pure function**:  
- output value follows soley from its input values
- no observable side effects


**side effects**:
- e.g. modifying an argument from within a function so that change is reflected in the calling environment.  
- side effect: if you modify the calling environment in any way 
- if you're going to have side effects in your code, at least document them (!!)
- when they are hidden, they are hard to track down 


Language support for functional programming:
- one function can take another function as an argument
- a function should be able to return a function to its caller 
- in python, everything is an object, including functions 

