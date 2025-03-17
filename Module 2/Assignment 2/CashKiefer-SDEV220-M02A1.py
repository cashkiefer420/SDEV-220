''' 
Author: Cash Kiefer
File Name: CashKiefer-SDEV220-M02A2.py
Description: This program accepts student names and GPAs, then determines if they qualify for the 
Dean's List or Honor Roll. The user can enter multiple students, and the program will stop when 'ZZZ'
 is entered as the last name.
'''

def main():
    while True:
        # Prompt for the last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()
        
        # Check if the user wants to quit
        if last_name.upper() == 'ZZZ':
            print("Exiting program. Have a great day!")
            break
        
        # Prompt for the first name
        first_name = input("Enter the student's first name: ").strip()
        
        # Prompt for the GPA and handle potential input errors
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid input. Please enter a numeric GPA.")
            continue  # Skip back to the start of the loop if input is invalid
        
        # Check if the student qualifies for the Dean's List or Honor Roll
        if gpa >= 3.5:
            print(f"Congratulations {first_name} {last_name}, you have made the Dean's List!")
        elif gpa >= 3.25:
            print(f"Great job {first_name} {last_name}, you have made the Honor Roll!")
        else:
            print(f"Keep up the hard work, {first_name} {last_name}!")
        
        print("-")  # Separator for readability

# Run the main function
if __name__ == "__main__":
    main()
