import pandas as pd
import RedditReadonlyService

clientId = ""                  # your bots client id
clientSecret = ""      # your bots client secret
userAgent = ""  # your bots user agent

redditReadOnly = RedditReadonlyService.getRedditReadOnly()

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
for submission in redditReadOnly.redditor("shesinanothercastle").submissions.new(limit=1000):
    if (submission.title.__contains__('Brew Crew')):
        submissionsDict["author"].append(submission.author)
        submissionsDict["author_fullname"].append(submission.author_fullname)
        submissionsDict["created_utc"].append(submission.created_utc)
        submissionsDict["id"].append(submission.id)
        submissionsDict["num_comments"].append(submission.num_comments)
        submissionsDict["permalink"].append(submission.permalink)
        submissionsDict["score"].append(submission.score)
        submissionsDict["selftext"].append(submission.selftext)
        submissionsDict["subreddit"].append(submission.subreddit)
        submissionsDict["title"].append(submission.title)
        submissionsDict["upvote_ratio"].append(submission.upvote_ratio)
        submissionsDict["url"].append(submission.url)

# Saving the data in a pandas dataframe
submissionsDataFrame = pd.DataFrame(submissionsDict)

# Save data frame to csv
submissionsDataFrame.to_csv("data/Brew-Crew-Submissions-User-2022.csv", index=True, index_label="index")