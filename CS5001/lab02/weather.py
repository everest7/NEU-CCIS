
highest = float(input("Enter the highest tempterature in 10-day forecast:"))
lowest = float(input("Enter the lowest tempterature in 10-day forecast:"))
print("Input the tempterature at noon from day1 to day10")

day1 = float(input("day1: "))
day2 = float(input("day2: "))
day3 = float(input("day3: "))
day4 = float(input("day4: "))
day5 = float(input("day5: "))
day6 = float(input("day6: "))
day7 = float(input("day7: "))
day8 = float(input("day8: "))
day9 = float(input("day9: "))
day10 = float(input("day10: "))


# Enter the highest temperature in Celsius in 10-day forecast
highest_10day = float(input("Enter the highest temprature in 10-day forecaset in Celsius:"))

BASE = 32
COVERSION_FACTOR = 9.0 / 5.0
FahTemp = (float(highest_10day) * COVERSION_FACTOR + BASE)

print("The difference between highest and lowest temperature in 10-day forecast is ",highest - lowest)
print("Average temperature at noon predicted for the 10 day forecast is",
    (day1 + day2 + day3 + day4 + day5 + day6 + day7 + day8 + day9 + day10)/10,"degrees")
print("Highest temperature from Celsius to Fahrenheit would be", round(FahTemp, 2),"degrees" )