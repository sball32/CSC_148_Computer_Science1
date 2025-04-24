#EDITED AND FINAL SUBMISSION

#Triangle Solver asks for 6 coordinate inputs. It then provides you with the 
# inputs and firstly determines if the points are collinear or not. If the 
# points are not collinear then it moves on  then caclulate the length of each 
# side, angle measurement in both degrees and radians.

#Sydney Ball
#CSC 148-001
#Assignment 4
#27 February 2024

import math

def main():  
    
    # Introduce the main function 
    print()
    
    print(50 * '*')
    print("* Welcome to Triangle Solver! *")
    print(50 * '*') #bout *50
   
    # Enter the values: 6 values or 3 coordinate pairs
    print("Using the prompts below, enter the x and y values for the three", 
          "points of your triangle.")
    
    print()
    
    x1_n = input("Enter x1: ") #do not assign value yet to input 
    y1_n = input("Enter y1: ")
    x2_n = input("Enter x2: ")
    y2_n = input("Enter y2: ")
    x3_n = input("Enter x3: ")
    y3_n = input("Enter y3: ")
    
    print()
   
    # Assign numeric value
    x1 = float(x1_n)
    y1 = float(y1_n)
    x2 = float(x2_n)
    y2 = float(y2_n)
    x3 = float(x3_n)
    y3 = float(y3_n)    
    
    # Format as pairs
    point1 = (x1,y1)
    point2 = (x2,y2)
    point3 = (x3,y3)
    
    # Print the values back to the user in coordinate form
    print("The three points entered are:")
    print(point1, point2, point3) 
       
    # First check if the values are collinear or not
    if collinear_points(x1, y1, x2, y2, x3, y3):
        print()
        print("These points are collinear and cannot form a triangle.")
        return  #return if collinear and continue if not 
    
    print()
    
    # If not collinear, then move on to the distance calculation
    D1 = distance(x2, y2, x3, y3) #strugled with order for running code 
    D2 = distance(x3, y3, x1, y1)
    D3 = distance(x1, y1, x2, y2)
    
    print("The lengths of the sides are: ")
    print("Side a:", round(D1, 4)) #need to round to 4 decimals 
    print("Side b:", round(D2, 4))
    print("Side c:", round(D3, 4))
    
    print()
    
    # Add the angle calculation to the output
    cos_A, cos_B, cos_C = get_angles(D1, D2, D3)
       
    A1_r = math.acos(cos_A) #use math.acos
    A2_r = math.acos(cos_B)
    A3_r = math.acos(cos_C)
   
    A1_d = math.degrees(A1_r) #convert to degrees using math.degrees
    A2_d = math.degrees(A2_r)
    A3_d = math.degrees(A3_r)     
      
    print("The three angles are: ")
    print("Angle A is", round(A1_r, 4), "radians, which is",
          round(A1_d, 4), "degrees.")
    print("Angle B is", round(A2_r, 4), "radians, which is",
          round(A2_d, 4), "degrees.")
    print("Angle C is", round(A3_r, 4), "radians, which is",
          round(A3_d, 4), "degrees.")   #remember to round the decimals    


# Collinearity check. Parameters are the original 6 values.
def collinear_points(x1, y1, x2, y2, x3, y3):
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

# Distance calculation. Parameters are the coordinates of two points.
def distance(x1, y1, x2, y2): #any coordiante set will work 
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
             
def get_angles(s1, s2, s3):
    cos_A = (s2 ** 2 + s3 ** 2 - s1 ** 2) / (2 * s2 * s3)
    cos_B = (s3 ** 2 + s1 ** 2 - s2 ** 2) / (2 * s3 * s1)
    cos_C = (s1 ** 2 + s2 ** 2 - s3 ** 2) / (2 * s1 * s2)
    return cos_A, cos_B, cos_C #use the early return for all

main() #call the main at the very end 
