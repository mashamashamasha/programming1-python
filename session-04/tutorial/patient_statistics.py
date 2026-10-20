patients_per_day = [12, 18, 15, 21, 9, 25, 17, 20, 14, 19, 23, 11, 27, 16]

week_one = patients_per_day[:7]
week_two = patients_per_day[8:]
every_sunday = patients_per_day[0:14:7]
last_three_reversed = patients_per_day[-3:] 

print(f"Week one: {week_one}")
print(f"Week two: {week_two}")
print(f"Every Sunday: {every_sunday}")
print(f"Last three patients: {last_three_reversed}")

print(f"Sum week 1: {sum(week_one)}")
print(f"Sum week 2: {sum(week_two)}")
print(f"Average week 1: {sum(week_one)/len(week_one):.0f}")
print(f"Average week 2: {sum(week_two)/len(week_two):.0f}")

#for people in patients_per_day:            #for each variable "people"
    #print(f"A day: {people}")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for index, day in enumerate(days):
    every_day_patients = patients_per_day[index:14:7]
    print(f"Average {day}: {sum(every_day_patients)/len(every_day_patients)} patients")

    #Muster:
# for idx, day in enumerate(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]):
#     every_day = patients_per_day[idx::7]
#     print(f"Average {day}: {sum(every_day) / len(every_day)} patients")

# print(f"Total: {sum(patients_per_day)} patients")