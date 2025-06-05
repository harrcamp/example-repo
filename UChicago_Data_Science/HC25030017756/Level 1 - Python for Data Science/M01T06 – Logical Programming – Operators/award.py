import os
os.system('cls' if os.name == 'nt' else 'clear')

# determines the award a person is receiving for competing in a triathlon

# take user inputs for all events in the triathlong and store as variables
swimming_time = int(input("What was your qualifying time for swimming?: "))
cycling_time = int(input("What was your qualifying time for cycling?:"))
running_time = int(input("What was your qualifying time for running?:"))

# sum to find total qualifying time
total_time = swimming_time + cycling_time + running_time

# print the sum for reference
print(f"Total time taken for the triathlon: {total_time}")

# determine which award the participant will receive based on their qualifying time

if total_time >= 111:
    award = "No Award"
elif (total_time >= 106) and (total_time <= 110):
    award = "Provincial scroll"
elif (total_time >= 101) and (total_time <= 105):
    award = "Provincial half colours"
elif (total_time <= 100):
    award = "Provincial colours"

print(f"Your award for finishing in {total_time} minutes is {award}.")