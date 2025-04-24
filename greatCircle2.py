#In this code we perform a calculation from inputed value of latitude and 
#longitude. With these values the equation allows us to determine the exact
#distance between the two cordinates by caclulating a large circle. 

##Sydney Ball
# CSC 148-001
# Assignment #2: Great Circle
# 1 February 2024

import math

print()
print(76*'*')

print("Welcome to the Great Circle calculator!")

print() 

#Enter the values for the cordinates for location 1
location1 = input("Enter the name of the first location: ")
## Distance 1:
lat1 = float(input("Enter the latitude (N) of the first location: "))
lat1_r = math.radians(lat1) #convert to radians 

long1 = float(input("Enter the longitude (E) of the first location: "))
long1_r = math.radians(long1)
           
print()

# Enter the values for the cordinates for location 2
location2 = input("Enter the name of the second location: ")
## Distance 2: 
lat2 = float(input("Enter the latitude (N) of the second location: "))
lat2_r = math.radians(lat2) #convert to radians 

long2 = float(input("Enter the longitude (E) of the second location: "))
long2_r = math.radians(long2)

#Breakdown the formula to ensure accuracy and use math from library 

E = (3959)
d1 = (math.sin(lat1_r)) #multiply
d2 = math.sin(lat2_r)  #add
d3 = math.cos(lat1_r) #multiply
d4 = math.cos(lat2_r) #multiply
d5 = math.cos(long1_r - long2_r) 

distance = E * math.acos(d1 * d2 + d3 * d4 * d5)
final_calc = round(distance, 2)

#Make the result a string to put in the final answer 
result = str(final_calc)

print("The distance in miles between", location1, "and",
location2, "is", result + ".")

print(76*'*')