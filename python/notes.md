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

Function composition:
- passing a function as an argument into another function  
- when you do this you pass in a function as `fn` instead of `fn()` would would add the result of `fn` as an argument 
- when you pass a function as an argument to another function, the function being passed in is called a `callback` function 

# sorted()
- sorted takes in a list (as the first ordered parameter) and returns a sorted list 
- optionally as a second parameter it has `key=`
- key expects a function, e.g. `len` which it uses to sort the list, so `len` would sort the values based on their lengths 
- the fn passed into `key` is a callback function

# functions as return values 
...

# Lambda functions 
- functional programming involves calling lots of... functions
- lambda functions = anonymous functions
- lambda comes from lambda calculus 
- `lambda <parameter-list>: <expression>` --> this is called a lambda expression
- `callable(fn)` will return true if `fn` is a function or a lambda expression 


# map()
- it calls a function on each element of an iterable 
- `map(<fn>, <iterable>)` --> return `<iterator>` 

# iterable 
- data collection that can be iterated over
- returns its members one at a time
- anything you can iterate over (list, dictionary, tuples, strings, sets, files, etc.)
- `for <item> in <iterable>: ...`

# iterator
- supports both `__iter__()` and `__next__()`
- can also be iterated over (like an iterable)
- all iterators are iretables, but not vice versa
- https://realpython.com/python-iterators-iterables/

