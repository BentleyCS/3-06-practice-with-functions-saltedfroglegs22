#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(a, b, c):
    pass
    perimeter = (a + b + c)/2
    return perimeter

#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(a, b, c, d):
    pass
    x=(a*(a-b)*(a-c)*(a-d))
    return x

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a, b, c):
    pass
    s = semiPerimeter(a,b,c)
    area = math.sqrt(multiplyDifferences(s, a, b, c))
    return area


#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(x):
    pass
    n = x * 2
    return n

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(a, b):
    pass
    n1 = a * (-1)
    x = n1 + b
    y = n1 - b
    return x, y


#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a, b, c):
    pass
    return (b*b)-((a*c)*4)

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a, b, c):
    pass
    numeratorpos = (-b) + math.sqrt((b*b)-(4*a*c))
    numeratormin = (-b) - math.sqrt((b*b)-(4*a*c))
    bottom = 2*a
    q1 = numeratorpos/bottom
    q2 = numeratormin/bottom
    return q1, q2

