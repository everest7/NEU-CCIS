import os


def main():
    file_name = input("Please enter the file name: ")
    try:
        with open(file_name, "r") as f:  # Open the txt file in read-only mode
            # Initialize variables
            sum_watt = 0
            minutes = 0
            running_minutes = 0
            minutes_data1, minutes_data2 = 0, 0
            # Record when the pump runs for at least 120 minutes in a row
            continuous_minute = 0
            print("Information on water softener recharges:")
            for line in f:  # Read every line of data in txt file
                num = int(line.rstrip('\n'))  # Strip the new line character
                minutes += 1  # Increment by 1 when reading a new line of data
                # 500 is the treshold determining whether the pump was running
                if num < 500:
                    # Report when pump runs for at least 120 minutes in a row
                    if continuous_minute >= 120:
                        print(continuous_minute, 'minutes started at', minutes
                              - continuous_minute)
                        continuous_minute = 0
                    continuous_minute = 0
                else:
                    continuous_minute += 1
                    running_minutes += 1

                sum_watt += num  # Calculate total watt comsumed

                # Calculate minutes of data to reach a certain quantity of
                # water
                if (running_minutes == (7 + 1) // 2):
                    minutes_data1 = minutes
                if (running_minutes == (4000 + 1) // 2):
                    minutes_data2 = minutes
            hour = minutes / 60
        # Report the duration of the data file in both hours and days
        print("Data covers a total of", hour, "hours")
        print("That's", hour/24, "days")
        # Report both the total number of gallons produced and the average
        # daily consum_wattption.
        print("Pump was running for", running_minutes, "minutes, producing",
              running_minutes * 2, "gallons")
        print("That's", running_minutes * 2 / 60, "per day")
        # Report the total power used by the pump.
        print("Pump requires a total of", sum_watt, "watt minutes of power")
        print("That's", sum_watt / 60 / 1000, "kWh of power")
        # Report how long it took to reach a certain quantity of water.
        print("It took", minutes_data1 if minutes_data1 != 0 else -1,
              "minutes of data to reach 7 gallons")
        print("It took", minutes_data2 if minutes_data2 != 0 else -1,
              "minutes of data to reach 4000 gallons")
    except FileNotFoundError:
        print("Unable to open", file_name)
    return


main()
