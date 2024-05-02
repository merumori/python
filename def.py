# def arith(a,b):
# 	add=a+b
# 	sub=a-b
# 	mut=a*b
# 	div=a/b
# 	print(add)
# 	print(sub)
# 	print(mut)
# 	print(div)  
# #colling function
# num=int(input('enter the first number:-'))
# num1=int(input('enter the second number:-'))
# arith(num,num1)

#factoryal number
# def factoriyal(num):
# 	if num==0:
# 		return 1
# 	else:
# 		return num*factoriyal(num-1)
# num=int(input("enter non negitev number"))
# result=factoriyal(num)
# print(result)


#palindrom number
# function which return reverse of a string

# def isPalindrome(s):
# 	return s == s[::-1]


# s = input("enter the string")
# ans = isPalindrome(s)

# if ans:
# 	print("Yes")
# else:
# 	print("No")
	    
# #prime number
# import math

# def is_prime(n):
#     if n < 2:
#         return False
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True

# print(is_prime(11))  # True
# print(is_prime(1))   # False

# #duck number
# def is_duck_number(number):
#     """Check if a number is a duck number."""
#     num_str = str(number)
#     if '0' in num_str[1:]:
#         return True
#     else:
#         return False

# # Example usage:
# number = 1023
# if is_duck_number(number):
#     print(number, "is a duck number.")
# else:
#     print(number, "is not a duck number.")


#buzz number
# Python program to check whether the 
# given number is Buzz Number or not. 

# function to check BUzz number. 
# def isBuzz(num) : 
# 	return (num % 10 == 7 or num % 7 == 0)  
# i = 67

# if (isBuzz(i)) : 
# 	print ("Buzz Number") 
# else : 
# 	print ("Not a Buzz Number") 
 
#armstrong number
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
