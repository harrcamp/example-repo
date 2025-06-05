import os
os.system('cls' if os.name == 'nt' else 'clear')

# Calculate the total cost of a holiday trip with flights,
# hotel room, and rental car. 

city_flight = str.lower(input(
    "Choose which city you are traveling to:""\n"
    "A) New York""\n"
    "B) Los Angeles""\n"
    "C) Chicago""\n"
    ))

num_nights = int(input(
    "How many nights are you travelling for?: "
    ))

rental_days = int(input(
    "How many days are you renting a car for?: "
    ))

def hotel_cost(num_nights):
    h_c = 1475 * num_nights
    return h_c

def plane_cost(city):
    if city == "a":
        return 890
    elif city == "b":
        return 780
    elif city == "c":
        return 1050
    else:
        return 0


def car_rental(rental_days):
    r_c = rental_days * 455
    return r_c

def holiday_cost(num_nights, city_flight, rental_days):
    h_c = hotel_cost(num_nights) 
    f_c = plane_cost(city_flight) 
    r_c = car_rental(rental_days)
    total = h_c + f_c + r_c
    return total

total_cost = holiday_cost(
    num_nights, city_flight, rental_days
    )


print(f"The flight cost for your hoiday is ${plane_cost(city_flight)}.""\n")

print(
     f"The cost to stay in a hotel on holiday is ${hotel_cost(num_nights)}.""\n"
     )

print(
     f"The rental car cost for your holiday is ${car_rental(rental_days)}.""\n"
     )

print(f"The total cost of your holiday trip is ${total_cost}.")