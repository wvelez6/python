calculate_unit = 24
unit_name = "hours"


def days_to_hours(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} are {num_of_days * calculate_unit} {unit_name}"
    else:
        return "You entered an invalid number."


user_input = input("Please enter the amount of days you want converted to hours.\n")
user_input_number = int(user_input)
return_data = days_to_hours(user_input_number)

print(return_data)
