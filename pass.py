#pass by value example

num1=100
num2=num1
num1=num1+100
print(num1,num2)
print("\n")

#pass by reference
list1=[1,2,3]
list2=list1
list1.append(3)
print(list1,list2)