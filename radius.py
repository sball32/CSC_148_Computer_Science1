# This code allows a person to take an abitrary radius of a circle and make 
# many calculations such as diameter, circumference, area, volume, and 
# surface area. All these outputs are rounded to absolute numbers. 

##Sydney Ball
# CSC 148-001
# Assignment #3: Radius
# 7 February 2024

import math

# Function to calculate diameter 
def get_diameter(rad_value):
    return 2 * float(rad_value) 
# Function to calculate circumference
def get_circumference(rad_value):
    return 2 * math.pi * float(rad_value)
#Function to calculate area
def get_area(rad_value):
    return math.pi * float(rad_value)**2   
#Function to calculate volume 
def get_volume(rad_value):
    return (3/4) * math.pi * float(rad_value)**3
# Function to calculate surface area 
def get_surface_area(rad_value):
    return 4 * math.pi * float(rad_value)**2
    
# Main Function 
def main():
    rad_value = float(input("Enter the radius of a circle: "))  #radius input
      
    d1 = abs(get_diameter(rad_value)) #take absolute value from calculation
    d2 = round(d1, 4) #round the value
    diameter = str(d2) #turn value into a string to print 
    
    c1 = abs(get_circumference(rad_value)) #do above many times for each calc
    c2 = round(c1, 4)
    circumference = str(c2)
    
    a1 = abs(get_area(rad_value))
    a2 = round(a1, 4)   
    area = str(a2)
    
    v1 = abs(get_volume(rad_value))
    v2 = round(v1, 4)    
    volume = str(v2)

    sa1 = abs(get_surface_area(rad_value))
    sa2 = round(sa1, 4)  
    surfacearea = str(sa2)

    print("The diameter of a circle with radius", str(rad_value) 
      +"is", diameter + ".")
    print("The circumference of a circle with radius"
      + str(rad_value), "is", circumference + ".")
    print("The area of a circle with radius", str(rad_value), "is", area + ".")
    print("The volume of a circle with radius", str(rad_value), "is", volume + ".")
    print("The surface area of a circle with radius", str(rad_value), "is"
      + surfacearea + ".")

main() #make sure to retun the value to ask for input 

print()