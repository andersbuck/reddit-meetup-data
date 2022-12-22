import pandas as pd
import RedditReadonlyService
import pprint

submissionsDataFrame = pd.read_csv ('data/Brew-Crew-Submissions-User-2022.csv')

redditReadOnly = RedditReadonlyService.getRedditReadOnly()

commentsDict = {
    "_submission_id": [],
    "author": [],
    "author_fullname": [],
    "body": [],
    "body_html": [],
    "controversiality": [],
    "created_utc": [],
    "depth": [],
    "id": [],
    "score": [],
    "permalink": []
}


def recursiveLoadComments(comments, submissionId):
    for comment in comments:

        if hasattr(comment, 'author_fullname'):
            commentsDict["author_fullname"].append(comment.author_fullname)
            commentsDict["author"].append(comment.author)
            commentsDict["_submission_id"].append(submission.id)
            commentsDict["body"].append(comment.body)
            commentsDict["body_html"].append(comment.body_html)
            commentsDict["controversiality"].append(comment.controversiality)
            commentsDict["created_utc"].append(comment.created_utc)
            commentsDict["depth"].append(comment.depth)
            commentsDict["id"].append(comment.id)
            commentsDict["score"].append(comment.score)
            commentsDict["permalink"].append(comment.permalink)

        if hasattr(comment, 'replies'):
            recursiveLoadComments(comment.replies, submissionId)

for index, row in submissionsDataFrame.iterrows():
    submission = redditReadOnly.submission(row['id'])
    print(submission.title)
    recursiveLoadComments(submission.comments, submission.id)

# Saving the data in a pandas dataframe
commentsDataFrame = pd.DataFrame(commentsDict)

# Save data frame to csv
commentsDataFrame.to_csv("data/Brew-Crew-Comments-2022.csv", index=True, index_label="index")