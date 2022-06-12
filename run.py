import gspread
from google.oauth2.service_account import Credentials
# Links google sheet and keeps data confidential
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gym_tracker')

#Where user inputs data
def get_lifts_data():
    """
    Get lifts figures input from the user.
    """
    while True: #allows user to repeat entry until valid data is entered
        print("Please enter lifts data from your last gym session.")
        print("Data should be entered in order of the following lifts: Bench Press, Squat, Deadlift, Pull ups, Press ups, Shoulder Press")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
    
        lifts_data = data_str.split(",") #this removes commas from string
        validate_data(lifts_data)

        if validate_data(lifts_data):
            break

    return lifts_data

#validate data
def validate_data(values):
    """
    Inside the try, converts all string values into integers. Raises error if string cannot be converted into integer
    """
    try:
        [int(value) for value in values] #convert data from string to integer to do maths
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def update_lifts_worksheet(data):
    """
    Update lifts worksheet, add new row with the list data provided
    """
    print("Updating lifts worksheet...\n")
    lifts_worksheet = SHEET.worksheet("lifts")
    lifts_worksheet.append_row(data)
    print("Lifts worksheet updated successfully")



data = get_lifts_data()
lifts_data = [int(num) for num in data]
update_lifts_worksheet(lifts_data)