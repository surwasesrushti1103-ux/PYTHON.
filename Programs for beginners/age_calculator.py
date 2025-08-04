from datetime import date

# Get today's date
today = date.today()

try:
    # Take user input
    birth_year = int(input("Enter your birth year (e.g. 2000): "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))

    # Create a date object for birth date
    birth_date = date(birth_year, birth_month, birth_day)

    # Calculate age
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    print(f"You are {age} years old.")

except ValueError:
    print("⚠️ Please enter valid numbers only.")
except Exception as e:
    print("❌ Error:", e)
