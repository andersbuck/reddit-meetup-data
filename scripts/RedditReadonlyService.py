import praw

clientId = ""                  # your bots client id
clientSecret = ""      # your bots client secret
userAgent = ""  # your bots user agent

def getRedditReadOnly():
    # Read-only instance
    return praw.Reddit(client_id=clientId,         
                                client_secret=clientSecret,      
                                user_agent=userAgent)  