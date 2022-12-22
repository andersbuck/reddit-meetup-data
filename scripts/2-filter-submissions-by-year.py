import pandas as pd

submissions = pd.read_csv ('data/Brew-Crew-Submissions.csv')

JAN_FIRST_2022_UTC = 1640995200

submissionsFiltered = submissions[submissions.created_utc > JAN_FIRST_2022_UTC]

submissionsFiltered.to_csv("data/Brew-Crew-Submissions-2022.csv", index=True, index_label="index")

print(submissionsFiltered[['index', 'created_utc', 'title']])