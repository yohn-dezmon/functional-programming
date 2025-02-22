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