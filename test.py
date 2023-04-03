print("hello world")
a=5
b=10
print(a+b)
c="Sajib"
d=255
print(c,d)
x = 5
y = "John"
print(type(x))
print(type(y))
print(type(c))
ab,bc,cd,de="sajib","jahid","jannat","sallu"
print(ab,bc,cd,de)
movie=["john wick","avatar","Terminator"]
e,f,g=movie
print(e)
print(f)
print(g)
h="sajib"
def myfunc():
    print("My name is " +h)
myfunc()
i = "awesome"

def myfunc2():
  i = "fantastic"
  print("Python is " + i)

myfunc2()

print("Python is " + i)

x = "awesome"

def myfunc():
  global x
  x = "valo nah"

myfunc()

print("Python is " + x)

for x in "banana":
  print(x)

sajib='sajib'
print(len(sajib))
print('ib' in sajib)

a="hello world"
print(a[2:10])

b = "Hello World!"
print(b[-5:-2])

a=23
b="My name is sajib and im {} years old"
print(b.format(a))

a=250
b=100
if a>b:
   print("A is greater than B")
else:
   print("B is greater than A")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[2:4])
thislist[1]="sajib"
print(thislist)


i=1
while i<10:
   print(i)
   if i==3:
      break
   i+=1

i=1
while i<6:
   print(i)
   i+=1
else:
   print("i is no longer less than 5")

name=["sajib","jahid",'jannat',"sallu"]
for x in name:
 print(x)

for x in "Banananananananananana":
   print(x)

for x in range(2,30,5):
   print(x)

for x in range(6):
   print(x)
else:
   print('Finally Finishd')

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
   for y in fruits:
      print(x,y)
print(adj[0],fruits[0])
print(adj[1],fruits[1])   
print(adj[2],fruits[2])  

def my_func():
   print("hello from function")

my_func()

def test(fname):
   print(fname + " is my name")

test("sajib")
test("Talat")
test("Mahmud") 

def test(*kids):
   print("jahid kids name is " + kids[1])
test("jahid1","jahid2","jahid3")

def test(**kids):
   print("jahid kids name is " + kids["mname"])
test(fnme="jahid1",lname="jahid2",mname="jahid3")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def test(list):
   for x in list:
      print(x)
movie=["john wick","avatar","Terminator"]
test(movie)

def test(x):
   return 5*x
print(test(5))
print(test(10))
print(test(100))

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(5)