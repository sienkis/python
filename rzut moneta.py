import imp
import random
import time

print("1-orzeł")
print("2-reszka")
a= int(input("wybierz 1 lub 2:"))
b=random.randint(0,2)
time.sleep(0.5)
print("3...")
time.sleep(0.5)
print("2...")
time.sleep(0.5)
print("1...")
time.sleep(0.5)

if (a==b):
    print("wygrałeś")
else:

    print("przegrałeś")

