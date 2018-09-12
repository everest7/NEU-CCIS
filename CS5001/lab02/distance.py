import math

def main():
        
    x1,y1 = map(float,input("Enter the coordinate of first point(x1 and y1):").split())
    x2,y2 = map(float,input("Enter the coordinate of second point(x2 and y2):").split())

    distance = float(math.sqrt((abs(x1 - x2)) ** 2 + (abs(y1 - y2)) ** 2))

    print("The euclidean distance between two points is",round(distance, 2))
main()