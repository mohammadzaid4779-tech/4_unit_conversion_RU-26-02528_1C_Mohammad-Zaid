print("===== UNIT CONVERSION SYSTEM =====")
print("1. Length")
print("2. Weight")
print("3. Temperature")
print("4. Time")

choice = input("Enter your choice (1-4): ")

print("You selected:", choice)
choice = input("Enter a number: ")

if choice == "1":
    print("You selected Length")

elif choice == "2":
    print("You selected Weight")

elif choice == "3":
    print("you selected temperature")

elif choice == "4":
    print("you selected time")
    choice = input("Enter your choice (1-4): ")

elif choice == "1":
    print("Length Converter")

elif choice == "2":
    print("Weight Converter")

elif choice == "3":
    print("Temperature Converter")

elif choice == "4":
    print("Time Converter")

else:
    print("Invalid choice. Select 1 to 4.")


def length_converter(value):
    miles = value * 0.621371
    return miles

result = length_converter(5)
print(f"5 km = {result:.2f} miles")

def weight_converter(value):
    grams = value * 1000
    return grams

result = weight_converter(2)
print(f"{result:.2f} g")

def temperature_converter(value):
    fahrenheit = (value * 9 / 5) + 32
    return fahrenheit

result = temperature_converter(0)
print(f"{result:.2f} F")

def time_converter(value):
    minutes = value * 60
    return minutes

result = time_converter(2)
print(f"{result:.2f} minutes")

try:
    value = float(input("Enter value: "))

except ValueError:
    print("Invalid value. Enter a number.")


def length_converter(value):
    miles = value * 0.621371
    return miles
result = length_converter(5)

print(f"5 km = {result:.2f} miles")

def weight_converter(value):
    grams = value * 1000
    return grams
result = weight_converter(2)
print(f"{result:.2f} g")

def temperature_converter(value):
    fahrenheit = (value * 9 / 5) + 32
    return fahrenheit
result = temperature_converter(0)
print(f"{result:.2f} F")

def time_converter(value):
    minutes = value * 60
    return minutes
result = time_converter(2)
print(f"{result:.2f} minutes")


print("===== UNIT CONVERSION SYSTEM =====")
print("1. Length (km to miles)")
print("2. Weight (kg to g)")
print("3. Temperature (C to F)")
print("4. Time (hours to minutes)")

choice = input("Enter your choice (1-4): ")

if choice not in ["1","2","3","4"]:
    print("Invalid choice. select 1 to 4.")

else:
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Invalid value. Enter a number.")
    else:
        if choice == "1":
            print(f"{value:g} km = {length_converter(value):.2f} miles")
        elif choice == "2":
            print(f"{value:g} kg = {weight_converter(value):.2f} g")
        elif choice == "3":
            print(f"{value:g} C = {temperature_converter(value):.2f} F")
        elif choice == "4":
            print(f"{value:g} hours = {time_converter(value):.2f} minutes")