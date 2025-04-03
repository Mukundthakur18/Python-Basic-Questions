# # question 1
# print("Hello World!")

# # question 2
# s = input("Enter a input: ")
# print(s)

# question 3
# m = int(input("Enter num1: "))
# n = int(input("Enter num2: "))
# print(m+n)



# question 4
a = 5
b = 8
# swapping without using 3rd variable
# a = a+b
# b = a-b
# a = a-b
# print(f"After swapping: a = {a}, b = {b}")

# another method for swapping (tuple unpacking)
# a,b = b,a
# print(f"After swapping: a = {a}, b = {b}")

# with using third variable 
# temp = a
# a = b
# b = temp
# print(f"After swapping: a = {a}, b = {b}")


# quesion 5
# s = int(input("Enter a number: "))
# print(f"Square of {s} is {s*s}") #multiplication method

# # eponentiation method
# num = s**2
# print(s)

# question 6
# a = int(input("Enter input: ")) 
# if a%2 == 0:
#     print("Even number")
# else:
#     print("Odd number")   


# question 7
# a = int(input("Enter input: "))
# if a>0:
#     print("Positive")
# elif a<0:
#     print("Negative") 
# else:
#     print("Zero")       


# question 8
# a = int(input("Enter age: "))
# if a>=18:
#     print("Eligible")
# else:
#     print("Not eligible")

# question 9
# a = int(input())
# b = int(input())
# c = int(input())
# print(f"Largest number: {max(a,b,c)}")


# question 10
# a = int(input("Enter input: "))
# if (a%4 == 0 and a%100 != 0) or a%400 == 0:
#     print("leap year")
# else:
#     print("Not a leap year")   


# Question 11
# a = 10
# for i in range(1,a+1):
#     print(i,end=" ")

# question 12
# a = 6
# sum = 0
# for i in range(1,a+1):
#     sum += i
# print(sum)    


# Question 13
# a = 4
# print(f"Table of {a}")
# for i in range(1,11):
#     print(f"{a}x{i}: {i*a}")

# question 14
# a = 5
# factorial = 1
# for i in range(1,a+1):
#     factorial *= i
# print(factorial)

# question 15
# for i in range(2,51,2):
#     print(i,end=" ")
# or
# for i in range(2,51):
#     if i%2!=0:
#         continue
#     else:
#         print(i,end=" ")  


# question 16
# m = input("Enter a string: ")
# n = m[::-1]
# if n == m:
#     print("Plaindrome")
# else:
#     print("Not palindrome") 


# question 17
# m = input("Enter a string: ")
# count = 0
# for i in m:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)


# question 18
# m = input("Enter a string: ")
# print(m[::-1])


# question 19
# a = input("Enter a string: ")
# if a == a.upper():
#     print("Upper case")  
# elif a == a.lower():
#     print("Lower case") 
# else:
#     print("Don't mix upper and lower case....")             


# question 20
# a = "Mukund thakur"
# b = a.replace(" ","_")
# print(b)

# Question 21
# a = ["Muku","is","best"]
# sum = ""
# for i in a:
#     sum += i
# print(sum)


# question 22
# a = [2,4,3,5]
# print(max(a))
# print(min(a))


# question 23
# a = [4,5,3,6,2]
# a.sort()
# print(a)

# question 24
# a = [2,3,4,4,2,3,6,7]
# b = set(a)
# b = list(b)
# print(b)

# or

# b = []
# for i in a:
#     if i in b:
#         continue
#     else:
#         b.append(i)
#         print(i,end = " ")


# question 25
# a = [2,3,4,3,3,3]
# print(a.count(3))


# question 26
# a = (2,3,4,5,6)
# b = list(a)
# print(type(b))
# print(b)


# question 27
# a = (2,3,4,5)
# print(len(a))


# question 28
# a = {"Name": "Mukund", "Age": 20}
# # a["City"] = "Gurugram"
# # print(a)
# # or
# a.update({"City":"Gurugram"})
# print(a)

# Question 29
# a_dict = {"name": "Mukund", "age": 22, "city": "Delhi"}
# print("Keys:",a_dict.keys())
# print("Values:",a_dict.values())
# or
# for key in a_dict:
#     print(f"Key: {key}, Value: {a_dict[key]}")


# question 30
# a_dict = {"x": 5, "y": 15, "z": 25}
# print(f"Sum of values: {sum(a_dict.values())}")



