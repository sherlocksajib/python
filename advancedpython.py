class sajib:
    def __init__(self, name, age):
        self.name=name
        self.age=age 
        
p1=sajib("Sajib", 23)
print(p1.name)
print(p1.age)


#Map function
def cube(x):
    return x*x*x
num=[1,2,3,4,5,6]
result=list(map(cube,num))
print(result)


#Filter function

num=[1,2,3,4,5]
result=list(filter(lambda x: x%2==0, num))
print(result)

#Comprehensive list
num=[1,2,3,4,5,6,7,8,9]
result=[x for x in num if x%2==0]
print(result)

num=[1,2,3,4,5,6,7,8,9]
result=[x+x for x in num]
print(result)

#Zip function
roll=[101,102,103,104,105,106]
name=["sajib","rashed","pikachu","talat","mahmud","sherlock"]
print(list(zip(roll,name)))

#FILE

file=  open("sajib.txt","r+")
text=file.read()
print(text)
file.close()

#file write
file=  open("sajib.txt","r+")
file.write('\n Salauddin is the father of Porimoni')
file.close()

#Exception handling
# num2=int(input("Enter a number : "))
# result= 20/num2
# print(result)
# print("Done")

# try:
#     list=[20,0,30]
#     result=list[0]/list[20]
#     print(result)
#     print("done")
# except ZeroDivisionError:
#     print("Divide by zero not possible") 
# # except IndexError:
# #     print("Index error") 
# finally:   
#     print("succesfull") 


try:
    num2= int(input("Enter first number: "))
    num1= int(input("Enter second number: "))
    result=num2/num1
    print(result)
except ValueError:
    print("Only integer valude are acceptabe")
except ZeroDivisionError:
    print("cant divide by zero")
finally:
    print("Thanks")