def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    #TODO: Fill in the rest of the necessary code here
    maxHR = float(208 - 0.7*age)
    reserve =float(maxHR - restHR)
    print("Your hear rate reserve is :",reserve," bpm")
    print("Here is a breakdown of your training zones:")
    print("Zone 1:",round(reserve * 0.5 + 67,2)," to ",round(reserve * 0.6 + 67,2)," bpm")
    print("Zone 2:",round(reserve * 0.6 + 67,2)," to ",round(reserve * 0.7 + 67,2)," bpm")
    print("Zone 3:",round(reserve * 0.7 + 67,2)," to ",round(reserve * 0.8 + 67,2)," bpm")
    print("Zone 4:",round(reserve * 0.8 + 67,2)," to ",round(reserve * 0.93 + 67,2)," bpm")
    print("Zone 5:",round(reserve * 0.93 + 67,2)," to ",round(reserve + 67,2)," bpm")



    print("=======================================")

main()