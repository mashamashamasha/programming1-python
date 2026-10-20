import random

number_of_mosquitoes = 100
number_of_waterholes = 10
breed_rate = 1.2
kill_rate = 0.2
waterhole_destroy_rate = 0.5
new_waterholes_per_rain_event = 3
rain_event_probability = 0.6

list = []
max_mosquitoes = number_of_mosquitoes
max_waterholes = number_of_waterholes

for day in range (1, 357):
    #random() for random number from import random (library) => from 0 to 1
    if random.random() < rain_event_probability:   
        number_of_waterholes = int(number_of_waterholes + new_waterholes_per_rain_event)

#inr for rounded numbers 
    number_of_waterholes = int (number_of_waterholes * (1 - waterhole_destroy_rate))
    number_of_mosquitoes = int(number_of_mosquitoes * (breed_rate ** number_of_waterholes))
    number_of_mosquitoes = int(number_of_mosquitoes * (1 - kill_rate))

    print(f"Day {day}: Mosquitoes: {number_of_mosquitoes}, Waterholes {number_of_waterholes} (at the end of the day)") 
    # print(number_of_waterholes)
    # print(number_of_mosquitoes)
    if max_mosquitoes < number_of_mosquitoes:
        max_mosquitoes = number_of_mosquitoes

    if max_waterholes < number_of_waterholes:
        max_waterholes = number_of_waterholes
#no space cause it will be counted for every loop = for every day
print (f"Highest mosquito count: {max_mosquitoes}")
print(f"Higest waterholes count: {max_waterholes}")


