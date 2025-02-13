# Create a dictionary to simulate a switch statement
day_messages = {
    "monday": "Today is Monday.",
    "tuesday": "Today is Tuesday.",
    "wednesday": "Today is Wednesday.",
    "thursday": "Today is Thursday.",
    "friday": "Today is Friday.",
    "saturday": "Today is Saturday.",
    "sunday": "Today is Sunday."
}

# Get input from the user and normalize it
day = input("Enter a day of the week: ").strip().lower()

# Retrieve the message using the dictionary with a default value
message = day_messages.get(day, "Invalid day entered.")

# Use the ternary operator to determine if it's a weekend or a weekday
day_type = "Weekend" if day in ("saturday", "sunday") else "Weekday" if day in day_messages else "Unknown"

# Display the results
print(message)
print("It's a", day_type + "!")
