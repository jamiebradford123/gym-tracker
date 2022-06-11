import gspread
from google.oauth2.service_account import Credentials
#Links google sheet and keeps data confidential
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
    print("Please enter lifts data from your last gym session.")
    print("Data should be entered in order of the following lifts: Bench Press, Squat, Deadlift, Pull ups, Press ups, Shoulder Press")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_lifts_data()