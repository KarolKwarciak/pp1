def f(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
a = int()
    



#def is_prime(number):
 #   if number <= 1:
  #      return False
   # for i in range(2, int(number**0.5) + 1):
    #    if number % i == 0:
     #       return False
    #return True

#N = int(input("Enter the number of prime numbers you want to find: "))

#count = 0
#number = 2

#print("Prime numbers:")
#while count < N:
 #   if is_prime(number):
  #      print(number, end=" ")
   #     count += 1
    #number += 1

#print()
