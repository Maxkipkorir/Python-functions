#Creating a function
def my_function():
    print("Hello world")
my_function()



#A function to add  numbers
def sum(x,y,z):
    a=x+y+z
    print("The sum is",a)
    
sum(10,20,30)
sum(100,300,4)

#A function to multiply two numbers
def multiply(x,y):
    q=x*y
    print("The product is",q)
    
multiply(10,28)

#A function to divide two numbers
def divide(x,y):
    a=(y/x)
    print("The division is",a)

divide(23,498)
#using return to call a function
def sum(x,y):
    a=x+y
    return a
print(sum(23,9))

#Arbitrary arguments
def courses(*args):
    for subject in args:
        print(subject)
courses("IT","BBAM","IR")

#Keyword arguments
def courses(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))
        
courses(first="IT",second="BBAM",third="IR")
#Default parameter value
def kenya(county="Kericho"):
    print("I am from" + county)
    
kenya()
kenya(" Nairobi")
kenya(" Mombasa")
kenya(" kiambu")

def Emotion(love="Matilda"):
    print("I love you",love)
    
Emotion()
Emotion("Victoria")
    
