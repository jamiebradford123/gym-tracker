# Gym Tracker

The Gym Tracker is a tool that can be used for people that go to the gym to upload and track their lifts. Based on what they enter, targets will be set for them to help them push themselves and achieve their goals. Their results will also update a spreadsheet so they can look at historical data.

![How it will opperate](/images/project%20plan.png)

## Features 


### Existing Features

- __Input Data__

  - This first feature allows users to input data on 6 different exercise's: Bench Press, Deadlift, Squat, Push ups, Pull ups, and Shoulder Press. This data will also be validated so the correct number of data is enterented as well as only allowing numbers. This data will then stored on a google worksheet

![When correct data is entered](/images/correct-data-input.png)
![When incorrect data is entered](/images/Validate-data.png)

- __Storing data in a spreadsheet__

  - All the data entered is stored on a google spreadsheet. Three values for each lift will be stored. First is the values that the user enters from their most recent gym session. The second is a target value which is calculated for them based on their average last 5 sessions and adds 10% to encourage progression. The final value thats calculated and stored is the difference between the users results and the targets that have been set for them, allowing the user to see if they are hitting their targets 
![When incorrect data is entered](/images/target-worksheet.png)
![When incorrect data is entered](/images/difference-worksheet.png)
![When incorrect data is entered](/images/lifts-worksheet.png)

### Features Left to Implement

- Allow users to enter each lift type seperately rather than all in one go, as this will make it more user friendly and result in less errors by the user when entering their lifts.

## Testing 
The code for this project was tested continuously throughout, mainly through the use of print statements to ensure each stage was working as it should, and identify where errors where occuring. 

When inputing data, incorrect data was also entered intentionally in order to see if the data input was being validated correctly, and only 6 numbers were being accepted. Strings would also produce an error message.

Once the programme was working, the Problems picked up in the problems tab were addressed, but these were essentially just due to white space and lines of code being too long.

### Validator Testing 
This code was also put through the pep8 validator and passed with no issues. http://pep8online.com/

![Validator result](/images/validator.png)

## Deployment

This site was deployed onto Heroku.
- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

## Credits 
- The main structure of this code and the functionality was taken from the "Love Sandwiches" project from the Code Institute. 



