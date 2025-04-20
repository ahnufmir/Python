Strings
string = "Hello World HOW ARE YOU  "
print(string.count(" "))

#List Practises
list = []
n = 4

sum = 0

for i in range(n):
    elements = int(input(f"Enter the name of marks {i+1}: "))
    list.append(elements)

for i in list:
    sum += i

avg = sum/len(list)    
# list.sort()
print ("List: ", avg)    

#Tuples
a = (7, 0, 8, 0, 0, 9)
check = 0
for i in a:
    if i==0 :
        check +=1
print(check)

# Another way
zeros = a.count(0)
print(check)


#sets
s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(len(s))

r = {}
print(type(r))

#Can you change the values inside a list which is contained in set S?
d = {
    "ahnuf" : "british english",
    "hassan" : "urdu",
    "saim" :  "punjabi",
    "ali" : "urdu"
}

print(d)

# LOOPS
n = int(input("Which number of table you want to be printed: "))
for i in range(0,10):
    print(n, " x ", i+1, " = ", n*(i+1) )


num = int(input("Write a number: "))
for i in range(2,num):
    if(num%i == 0 and (num != 0 and num != 1 and num != 2)):
        print("Composite")
        break
    else:
        print("Prime")
        break

number = int(input("Write a number: "))
i = 0
sum=0
while(i<= number):
    sum += i
    i +=1

print(sum)    


nums = int(input("Write a number: "))
factorial = 1
for i in range(1,nums+1):
    factorial *= i

print(factorial)   