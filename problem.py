x=list(input("Enter the list :"))
# y=list(input("Enter the list :"))
# for x in x:
#     for y in y:
#         if x==y:
#             print("False")
        
#         else:
#             print("True")

# a=int(input("Enter a value: "))
# b=a
# c=int( "%s%s" % (a,a) )
# d=int( "%s%s%s" % (a,a,a) )
# print(b+c+d)

# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))

# Factorial
# def fact(n):
#     if n<0:
#         return 0
#     elif n==1 or n==0:
#         return 1
#     else:
#         fact=1
#         while (n>1):
#             fact *=n
#             n -=1
#         return fact
# num=int(input("Enter the value to calculate the factorial :"))
# print("Factorial of",num,"is",
# fact(num))

# Prime Number
# def prime(start,end):
#     lst=[]
#     flag=0
#     for i in range(start,end):
#         for j in range(2,i):
#             if i%2==0:
#                 flag=1
#             else:
#                 flag=0
#         if flag==0:
#                 lst.append(i)
#     return lst
# #driver code
# star=int(input("Enter the starting value: "))
# end=int(input("Enter the ending value: "))
# lst = prime(star, end)
# if len(lst) == 0:
#     print("There are no prime numbers in this range")
# else:
#     print("The prime numbers in this range are: ", lst)




# num = int(input("Enter the value to check: "))
# if num > 1:
   
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number") 


# num=int(input("Enter the nTH number of fibibnacci series :"))
# a=0
# b=1
# if num<0:
#     print("incorrect value")
# elif num==0:
#     a=0
# elif num==1:
#     b=1
# else:
#     for x in range(2,num):
#         c=a+b
#         a=b
#         b=c
# print(b)


# abstractmethod   
# from abc import ABC, abstractmethod   
# class Car(ABC):   
#     def mileage(self):   
#         print("this is jannat") 
  
# class Tesla(Car):   
#     def mileage(self):   
#         print("The mileage is 30kmph")   
# class Suzuki(Car):   
#     def mileage(self):   
#         print("The mileage is 25kmph ")   
# class Duster(Car):   
#      def mileage(self):   
#           print("The mileage is 24kmph ")   
  
# class Renault(Car):   
#     def mileage(self):   
#             print("The mileage is 27kmph ")   
          
# # Driver code  
# t= Tesla ()   
# t.mileage()   
  
# r = Renault()   
# r.mileage()   
  
# s = Suzuki()   
# s.mileage()   
# d = Duster()   
# d.mileage()

# num=int(input("Enter the nth value of natural number :"))
# sum=0
# for x in range(1,num+1):
#     sum=sum+(x*x)
# print(sum)

# sum of array element
# def _arr(arr):
#     sum=0
#     for x in arr:
#         sum=sum+x
#     return sum
# arr=[]
# x=int(input("Enter the lenth :"))
# for i in range(1,x+1):
#     ell=int(input())
#     arr.append(ell)
# ans=_arr(arr)
# print("the sum is: ",ans)

# max element of array element
# def _arr(arr,x):
#     max=arr[0]  
#     for x in range (1,x):
#         if arr[x]>max:
#           max=arr[x]
#     return max
# arr=[]
# x=int(input("Enter the lenth :"))
# for i in range(1,x+1):
#     ell=int(input())
#     arr.append(ell)
# ans=_arr(arr,x)
# print("the max elemnt is: ",ans)

# def swapList(newList):
#     size = len(newList)
     
#     # Swapping
#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp
     
#     return newList
     
# # Driver code
# newList = [12, 35, 9, 56, 24]
           
# newList = [12, 35, 9, 56, 24]
# newList.reverse()
# print(newList)

# list=[10,20,30,40,50,60]
# a=len(list)
# print(a)

# s=int(input("lenth of the list: "))
# list=[]
# for x in range(0,s):
#     ell=int(input())
#     list.append(ell)
# sum=0
# for x in range(0,s):
#     sum=sum+list[x]
# print(sum)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=' ')
#     print()