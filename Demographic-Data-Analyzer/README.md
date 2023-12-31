In this project an analysis is carried out on demographic data extracted from the 1994 Census database using Pandas. Below is a sample of the data
|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

The code answers the following questions when run:

* How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (`race` column)

* What is the average age of men?

* What is the percentage of people who have a Bachelor's degree?

* What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

* What percentage of people without advanced education make more than 50K?

* What is the minimum number of hours a person works per week?

* What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

* What country has the highest percentage of people that earn >50K and what is that percentage?

* Identify the most popular occupation for those who earn >50K in India.
