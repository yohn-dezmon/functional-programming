# function value dictionary 
def add_values(x, y):
    return x + y 

def subtract_values(x, y):
    return x - y 

def multiply_values(x, y):
    return x * y 



func_val_dict = { 'add': add_values, 
                  'subtract': subtract_values, 
                   'multiply': multiply_values }

x = 5
y = 7
add_res = func_val_dict['add'](x, y)
sub_res = func_val_dict['subtract'](x, y)
multiply_res = func_val_dict['multiply'](x, y)
print(add_res)
print(sub_res)
print(multiply_res)

# sorted()'s 2nd parameter is an example of functional composition 

strs = ['a', 'zee', 'ceee', 'dee']
alpha_sort = sorted(strs)
len_sort = sorted(strs, key=len)
backwards_word_sort = sorted(strs, key=lambda x: x[::-1])
print(alpha_sort)
print(len_sort)
print(backwards_word_sort)


# returning a function from a function 

def outer():
    def inner():
        print("I am become inner fn")
    return inner

# here we essentially assign `inner` to fn
fn = outer()
# this just shows that fn is a function
print(fn)
# this calls inner()
fn()
# this also calls inner()
outer()()

# map(<fn>, <iterable>)

listo = ['i', 'am', 'iterable']
iterator = map(lambda x: x[::-1], listo)

# iterate over iterator 
for variable in iterator:
    print(variable)
# at this point, `iterator` is empty! you used up its values.

iterator = map(lambda x: x[::-1], listo)
# converting an iterator into a list(!!)
print(list(iterator))

# you can call a lambda function without saving it to a variable 
res = (lambda x: x[::-1])('beige')
print(res)
res2 = (lambda x1, x2, x3: x1 + x2 + x3)(1, 2, 3)
print(res2) 

# conditional statement in a lambda function 
res = (lambda x: "even" if x % 2 == 0 else "odd")(1)
print(res)

# combining `map()` and `lambda`

res = list(map(lambda x: x[::-1], ['woop', 'powwow', 'corn']))
print(res)

# convert a list of numbers to strs then joining them with +

joined = "+".join(map(lambda x: str(x), [1,2,3,4]))
print(joined)
# even simpler!
# join can consume an iterator...

joined = "+".join(map(str, [1,2,3,4]))
print(joined)

# map() with multiple iterables

iter1 = [1,2,3]
iter2 = [10, 20 , 30]
iter3 = [100, 200, 300]

# there have to be three arguments into the fn bc there are three iterables
res = list(map((lambda x1,x2,x3: x1 + x2 + x3), iter1, iter2, iter3))
print(res)

# experiment
# the 1000 doesn't get used bc there are not other values to add it to 
iter1 = [1,2,3, 1000]
iter2 = [10, 20 , 30]
iter3 = [100, 200, 300]

# there have to be three arguments into the fn bc there are three iterables
res = list(map((lambda x1,x2,x3: x1 + x2 + x3), iter1, iter2, iter3))
print(res)

# filter()
res = list(filter(lambda x: x % 2 == 0, [2,3,4,5]))
print(res)

# reduce()
from functools import reduce 
 