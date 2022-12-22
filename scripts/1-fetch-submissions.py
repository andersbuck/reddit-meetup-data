import praw
import pandas as pd
from pmaw import PushshiftAPI

api = PushshiftAPI()
submissions = api.search_submissions(subreddit="charlotte", limit=1000)
submissionList = [sub for sub in submissions]

# Dictionary to store all submission data
submissionsDict = {
    "author": [],
    "author_fullname": [],
    "created_utc": [],
    "id": [],
    "num_comments": [],
    "permalink": [],
    "score": [],
    "selftext": [],
    "subreddit": [],
    "title": [],
    "upvote_ratio": [],
    "url": []
}

#Scrape the Charlotte subreddit for the Brew Crew posts
for submission in submissionList:
    if (submission["title"].__contains__('Brew Crew')):
        print(submission["title"], submission["id"], submission["created_utc"])
        submissionsDict["author"].append(submission["author"])
        submissionsDict["author_fullname"].append(submission["author_fullname"])
        submissionsDict["created_utc"].append(submission["created_utc"])
        submissionsDict["id"].append(submission["id"])
        submissionsDict["num_comments"].append(submission["num_comments"])
        submissionsDict["permalink"].append(submission["permalink"])
        submissionsDict["score"].append(submission["score"])
        submissionsDict["selftext"].append(submission["selftext"])
        submissionsDict["subreddit"].append(submission["subreddit"])
        submissionsDict["title"].append(submission["title"])
        submissionsDict["upvote_ratio"].append(submission["upvote_ratio"])
        submissionsDict["url"].append(submission["url"])

# Saving the data in a pandas dataframe
submissionsDataFrame = pd.DataFrame(submissionsDict)

# Save data frame to csv
submissionsDataFrame.to_csv("data/Brew-Crew-Submissions.csv", index=True, index_label="index")