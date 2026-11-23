#Menu Based Unit Conversion
def length_converter(value, from_unit):
    if from_unit == "km":
        return value * 0.621371        # km to miles
    else:
        return value / 0.621371        # miles to km

def weight_converter(value, from_unit):
    if from_unit == "kg":
        return value * 1000            # kg to g
    else:
        return value / 1000            # g to kg

def temperature_converter(value, from_unit):
    if from_unit == "C":
        return (value * 9 / 5) + 32    # C to F
    else:
        return (value - 32) * 5 / 9    # F to C

def time_converter(value, from_unit):
    if from_unit == "hours":
        return value * 60              # hours to minutes
    else:
        return value / 60              # minutes to hours

UNIT_PAIRS = {
    "1": [("km", "miles"), ("miles", "km")],
    "2": [("kg", "g"), ("g", "kg")],
    "3": [("C", "F"), ("F", "C")],
    "4": [("hours", "minutes"), ("minutes", "hours")],
}

while True:
    print("===== UNIT CONVERSION SYSTEM =====")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Time")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "5":
        print("Thank you!")
        break

    # Validate menu choice
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Select 1 to 4.")
        continue

    # Show the units of the chosen category
    print("Select conversion:")
    for number, pair in enumerate(UNIT_PAIRS[choice], start=1):
        print(f"{number}. {pair[0]} to {pair[1]}")

    direction = input("Enter your choice (1-2): ").strip()
    if direction not in ["1", "2"]:
        print("Invalid choice. Select 1 or 2.")
        continue

    from_unit, to_unit = UNIT_PAIRS[choice][int(direction) - 1]

    while True:
        try:
            value = float(input(f"Enter value in {from_unit}: "))
        except ValueError:
            print("Invalid value. Enter a number.")
        else:
            break

    if choice == "1":
        result = length_converter(value, from_unit)
    elif choice == "2":
        result = weight_converter(value, from_unit)
    elif choice == "3":
        result = temperature_converter(value, from_unit)
    else:
        result = time_converter(value, from_unit)

    print(f"{value:g} {from_unit} = {result:.2f} {to_unit}")