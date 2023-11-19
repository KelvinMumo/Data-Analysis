# Medical Data Visualizer

This project focuses on visualizing and making calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations. The challenge is to use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

# Data description
The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. The data is provided in the medical_examination.csv file.
 
 | Feature Variable | Type | Variable Value | Type |
|---|---|---|---|
| Age | Objective | age | int (days) |
| Height | Objective | height | int (cm) |
| Weight | Objective | weight | float (kg) |
| Gender | Objective | gender | categorical |
| Systolic blood pressure | Examination | ap_hi | int |
| Diastolic blood pressure | Examination | ap_lo | int |
| Cholesterol | Examination | cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination | gluc | 1: normal, 2: above normal, 3: well above normal |
| Smoking | Subjective | smoke | binary |
| Alcohol intake | Subjective | alco | binary |
| Physical activity | Subjective | active | binary |
| Presence or absence of cardiovascular disease | Target Variable | cardio | binary |



# Tasks
* Create a chart to show the counts of good and bad outcomes for the `cholesterol`, `gluc`, `alco`, `active`, and `smoke` variables for patients with cardio=1 and cardio=0 in different panels.
* Add an `overweight` column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
* Normalize the data by making 0 always good and 1 always bad. If the value of `cholesterol` or `gluc` is 1, make the value 0. If the value is more than 1, make the value 1.
* Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's `catplot()`. The dataset should be split by `'Cardio'` so there is one chart for each cardio value.
* Clean the data. Filter out the following patient segments that represent incorrect data:
diastolic pressure is higher than systolic (Keep the correct data with (`df['ap_lo'] <= df['ap_hi'])`)
  * height is less than the 2.5th percentile (Keep the correct data with (`df['height'] >= df['height'].quantile(0.025))`)
  * height is more than the 97.5th percentile
  * weight is less than the 2.5th percentile
  * weight is more than the 97.5th percentile
* Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's `heatmap()`. Mask the upper triangle.
