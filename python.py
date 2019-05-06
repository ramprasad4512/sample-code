

friends=['e','x','s']
for x in friends:
    print("happy new",x)
print("done")

while True:
    line=input("ram:-")
    if line=="done":
        break
while False:
    if line=="prasad":
        continue
print("line")
print("done")


x=[10,20,30,40]
it=iter(x)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
for p in x:
    print("iterations are",p)
#inheritance
class x:
    def m1(self):
        print("bahubali")
class y(x):
    def m2(self):
        print("kabali")
class z(x):
    def m3(self):
        print("robo2.0")
y1=y()
p=y1.__hash__()
print(p)
y1.m1()
y1.m2()
z1=z()
q=z1.__hash__()
print(q)
z1.m3()
z1.m1()
#polymorphism
#methodoverloading
class x:
    def m1(self):
        print("no movies")
    def m1(self,a):
        print("yes movies")
    def m1(self,a,b):
        print("movies")
x1=x()
x1.m1(1000,2000)
#method overriding
class x:
    def m1(self):
        print("narasaraopet")
    def m2(self):
        print("prakashnagar")
class y(x):
    def m2(self):
        print("guntur")
    def m3(self):
        print("andhrapradesh")
    def display(self):
        self.m1()
        self.m2()
        self.m3()
y1=y()
y1.display()
x1=x()
x1.m2()

#abstratcion
class x:
    __a=1000
    def __init__(self):
        self.b=2000
    def __init__(self):
        print("ramprasad")
    def display(self):
        print(x.__a)
        print(self.__b)
        
x1=x()
x1.display()
print(x.__a)
print(x.__b)

while True:
    line=input("ramprasadreddy:-")
    if line=="ramprasadreddy":
        continue
    elif line=="done":
        break

x="shutdownsopasufasorrow"
x=x.split('s')
print(x)


num=[12,151,54,65,54,54,5458,45,48,4,61,4,543,48,45,4]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))

for p in range(1,11):
    print(p,"*2=",p*2 )
    
    


friends=['a','v','c']
for x in friends:
    print("have teachers higherland",x)
  
    n = input("enter value")
x=int(n)
fact = 1
  
for i in range(1,1+x): 
    fact = fact * i 
      
print ("The factorial is : ",end="")
print (fact)




num = int(input("enter a number: "))
 
for i in range(2,num):
	if num % i  == 0:
		print("not prime number")
		break
else:
	print("prime number")


	
i=input("enter fno")
j=input("enter sno")
try:
    
   x=int(i)
   y=int(j)
   z=x/y
   print(z)
except:
    print("error occur")
    print("end")
x=input("enter a number:")
num=int(x)
for i in range (2,num):
    if num % i == 0:
        print("not a prime")
        break
else:
 print("prime")


nums=[10,15,23,20,24,65,60,82,85,92]
for num in nums:
    if num % 5== 0:
        print(num)
        break

def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c)
        
fib(12)














