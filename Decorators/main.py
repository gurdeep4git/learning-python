
# def my_decor(func):
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#     return wrapper

# @my_decor
# def greet():
#     print("Main function called")    

# greet()    


#Create a decorator that:
# takes a number
# multiplies function result by 2

def multiplier_2(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrap

@multiplier_2
def get_number():
    return 10

print(get_number())

# 2. Square the Result
# Decorator should:
# take function result
# return its square

def square(func):
    def wrap(*args):
        result = func(*args)
        return result ** 2
    return wrap

@square
def set_number(n):
    return n

print(set_number(50))

# 5. Check Positive Number

# Decorator should:
# allow function only if input number > 0
# otherwise print "Invalid number"

def check_positive(func):
    def wrap(num):
        if num < 0:
            print("Invalid number")
            return
        return func(num)
    return wrap    

@check_positive
def square_me(n):
    print(n * n)

square_me(2)

# 7. Simple Login System 🔐

# Decorator should:

# allow access only if user == "admin"

# otherwise print "Access Denied"

def isAuth(func):
    def wrap(user):
        if user == 'admin':
            return func(user)
        else:
            print('Access denied')

    return wrap        

@isAuth
def login(user):
    return f"Welcome {user}"

print(login('admin')) 