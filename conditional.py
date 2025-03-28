# problem solving in python

# # easy:
# # write a program to check if a given number is positive negative or neither zero
# num=int(input("enter the number"))
# if(num>0):
#     print("positive")
# else:
#    if(num<0):
#       print("negative number")  
#    else:
#       if(num==0):
#          print("niether positive nor negative")

# # determine a number is even or odd
# a=int(input("enter the number(even or odd)"))

# if a%2==0:
#     print("even number")
# else:
#     print("odd number")

# # 3.check the persion is eligible for vote or not(age>=18)
# age=int(input("enter the number of age"))
# if(age>=18):
#     print("eligible for vote")
# else:
#    print("not eligible for vote")   

# # write a  program to find the greates of two number
# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))
# if(num1>num2):
#    print("number is greater")
# else:
#    if(num2>num1):
#       print("number to is greater") 

# # print "pass" if a student scorea more than 40 marks

# Student_marks=int(input("enter the marks"))
# if(Student_marks>=40):
#    print("pass")
# else:
#    print("fail")      

# # write a program to display the workinday of the week based on a number input(1 for monday,2for ftuesday)
# day=int(input("enter the number"))
# if(day==1):
#     print("Monday")
# else:
#    if(day==2):
#       print("tuesday")
#    else:
#       if(day==3):
#          print("wednesday")
#       else:
#          if(day==4):
#             print("thurday")
#          else:
#             if(day==5):
#                print("friday")
#             else:
#                if(day==6):
#                   print("saturaday")

# #implement the a simple caluculator based on add mul div sub

# number_1=int(input("enter the number"))
# number_2=int(input("enter the second number"))
# symbol=str(input("enter the symbol"))
# if(symbol=="+"):
#     print(number_1 + number_2)
# else:
#     if(symbol=="-"):
#         print(number_1-number_2)
#     else:
#         if(symbol=="-"):
#             print(number_1*number_2)
#         else:
#             if(symbol=="*"):
#               print(number_1*number_2)
#             else:
#                if(symbol=="/"):
#                    print(number_1/number_2)

#                else:
#                    print("nothing")


# # write a program based on the months input we give the number 1,2 like output we get jan fev

# month=int(input("enter the month number"))
# if(month==1):
#     print("jan")
               
            
# else:
#     if(month==2):
#         print("feb")
#     else:
#         if(month==3):
#             print("mar")
#         else:
#             if(month==4):
#                 print("apirl")
#             else:
#                 if(month==5):
#                     print("may")
#                 else:
#                     if(month==6):
#                         print("jun")
#                     else:
#                         if(month==7):
#                             print("jul")
#                         else:
#                             if(month==8):
#                                 print("aug")
#                             else:
#                                 if(month==9):
#                                     print("sep")
#                                 else:
#                                     if(month==10):
#                                         print("oct")
#                                     else:
#                                         if(month==11):
#                                             print("nov")
#                                         else:
#                                             if(month==12):
#                                                 print("dec")
         
# # medium conditional statements



# #   check given year is leap year or not
# Year=int(input("enter the year"))
# if(Year%4==0):
#     print("given year is leap year")
# else:
#     print("is not leap year")  


# # check given character is vowel are consonant

# Character=input("enter the string").lower()
# Vowels=["a","e","i","o","u"]
# consonants = [
#   'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',  
#   'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
# ]

# if(len(Character)==1):
#     if(Character in Vowels):
#        print("given character is Vowel")
#     elif (Character in consonants):
#        print("given character is consonant")
#     else:
#         print("not a alaphabet") 

# # calculate the grade of a student based on the marks they 

# marks=int(input("enter the marks"))
# if(marks>90 and marks<=100):
#     print("A Grade")
# else:
#     if(marks>80 and marks<89):
#         print("B Grade")
#     else:
#         if(marks>70 and marks<79):
#             print("c grade")
#         else:
#             if(marks<70):
#                 print("fail")   

# # 5.write a program to check if three sides length form a valid triangle
# side1=int(input("enter the side1"))
# side2=int(input("enter the side2"))
# side3=int(input("enter the side3"))

# if(side1+side2>side3 and side1+side3>side2 and side2+side3>side1):
#     print("triangle")
# else:
#     print("not a triangle")


# #  5) write a program to check if three sides length form a valid triangle
# a=int(input("enter a value:"))
# b=int(input("enter a value:"))
# c=int(input("enter a value:"))
# if a==b==c:
#     print("equilateral triangle")
# elif a==b or a==c or b==c:
#     print("isoceless triangle")
# else:
#     print("scalene triangle")    











    
            










                  
        

