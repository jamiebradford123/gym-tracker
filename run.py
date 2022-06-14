import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gym_tracker')


def get_lifts_data():
    """
    Get lifts figures input from the user.
    """
    while True:
        print("Please enter lifts data from your last gym session.")
        print("Data should be in order of the following lifts: Bench Press")
        print("Squat, Deadlift, Pull ups, Press ups, Shoulder Press")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here:\n")
        lifts_data = data_str.split(",")
        validate_data(lifts_data)

        if validate_data(lifts_data):
            print("Data is valid!")
            break

    return lifts_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers. Raises error if
    strings cannot be converted into integer
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as value_error:
        print(f"Invalid data: {value_error}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_diff_data(lifts_row):
    """
    Compares the actual lifts with th target lift for each lift type.
    The difference is calculated by the following calculation:
    - lifts - target lift
    - Positive number indicates that the person has lifted above target
    - Negative number indicates they have lifted below their target
    """
    print("Calculating surplus data...\n")
    target = SHEET.worksheet("target").get_all_values()
    target_row = target[-1]

    diff_data = []
    for target, lifts in zip(target_row, lifts_row):
        diff = lifts - int(target)
        diff_data.append(diff)

    return diff_data


def get_last_5_entries_lifts():
    """
    Collects collumns of data drom the lifts worksheet, collecting the last 5
    entries of each lift which will be used to calculate the target lift
    """
    lifts = SHEET.worksheet("lifts")
    columns = []
    for ind in range(1, 7):
        column = lifts.col_values(ind)
        columns.append(column[-5:])
    return columns


def calculate_target_data(data):
    """
    Calculate the average lift for each lift type, and add 10%
    """
    print("Calculating target data...\n")
    new_target_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        target_num = average * 1.1
        new_target_data.append(round(target_num))

    return new_target_data


def main():
    """
    Run all program functions
    """
    data = get_lifts_data()
    lifts_data = [int(num) for num in data]
    update_worksheet(lifts_data, "lifts")
    new_diff_data = calculate_diff_data(lifts_data)
    update_worksheet(new_diff_data, "diff")
    lifts_columns = get_last_5_entries_lifts()
    target_data = calculate_target_data(lifts_columns)
    update_worksheet((target_data), "target")


print("Welcome to the Lifting Tracker!")
main()
