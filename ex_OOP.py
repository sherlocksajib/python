# try:
#     num2= int(input("Enter first number: "))
#     num1= int(input("Enter second number: "))
#     result=num2/num1
#     print(result)
# except ValueError:
#     print("Only integer valude are acceptabe")
# except ZeroDivisionError:
#     print("cant divide by zero")
# finally:
#     print("Thanks")

# def voter(age):
#     if age<18:
#         raise ValueError("You are not eligible for vote")
#     return "you are allowed to vote"
# print(voter(17))

#swapping

a=20
b=10
a,b=b,a
print(a,b)

#OOP

class student:
    roll=""
    gpa=""

    def display(self):
         print(f" Roll : {self.roll}, GPA : {self.gpa}")


rahim=student() 
rahim.roll=105
rahim.gpa=3.85
rahim.display()

kahim=student() 
kahim.roll=101
kahim.gpa=3.55
kahim.display()


class sports:
     radious=""
     weights=""
     def __init__(self,height,weight):
        self.radious=height
        self.weights=weight 
     def display(self):
         volume=3.1416*self.radious*self.radious*self.weights
         print(f"Volume is: ",volume)
          
football=sports(10,20)
football.display()
vollyball=sports(20,30)
vollyball.display()     

#Inheritence

class phone:
    def call(self):
        print("you can call")

    def message(self):
        print("you can message")
class laptop(phone):
    # def call(self):
    #     print("you can call")

    # def message(self):
    #     print("you can message")
    def code(self):
        print("you can code")

s=laptop()
s.message()
s.call()
s.code()