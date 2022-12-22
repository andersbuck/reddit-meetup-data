import pandas as pd

submissions = pd.read_csv ('data/Brew-Crew-Submissions-User-2022.csv')

print('In 2022 we had ' + str(len(submissions)) + ' meetups!')

maxScoreSubmission=submissions.loc[submissions['score'].idxmax()]

print('We also had lots of variety going to 23 unique breweries!')

print('Our most visted breweries this year (All tied at 3 visits) were:')
print('  * Birdsong')
print('  * Devils Logic')
print('  * Hopfly')
print('  * Resident Culture')
print('  * Town')

print('Our highest upvoted meetup was "' + maxScoreSubmission.title + '" with a score of ' + str(maxScoreSubmission.score) + ' upvotes ' + maxScoreSubmission.url)

comments = pd.read_csv ('data/Brew-Crew-Comments-2022.csv')

print('This year we had a lot of comments! ' + str(len(comments)) + ' to be exact!')

print('And in all those comments we had ' + str(len(pd.unique(comments['author']))) + ' participate!')

comments['comment_count'] = comments.groupby(['author'])['index'].transform('count')

comments = comments.sort_values(by=['comment_count'], ascending=False)

comments.to_csv("output/comments_count.csv", index=True, index_label="index")

print('These users were the shining stars posting the most comments:')

print('  * shesinanothercastle - 53')
print('  * MakeMeYourLeader - 31')
print('  * CasualAffair - 25')
print('  * HipsterMustache - 18')
print('  * bs_horse - 11')
print('  * cowley10 - 11')

print('Out of all the comments these were highest voted!:')

print(' * Emergency-Ad-7423 - Score 24 - "Well if you start to get really frustrated with parking you can go to the railyard garage..." /r/Charlotte/comments/wpslff/brew_crew_meetup_816_charlotte_beer_garden_630_pm/ikidam0/')
print(' * HipsterMustache - Score 19 - "If there\'s any time to bust out the Patagucci, tonight\'s the night boyz" /r/Charlotte/comments/wpslff/brew_crew_meetup_816_charlotte_beer_garden_630_pm/ikijjwu/')
print(' * Indjk - Score 18 - "Well hey there! Name\'s Jake and I\'m one of your bartenders tonight..." /r/Charlotte/comments/wk1t10/brew_crew_meetup_89_divine_barrel_630_pm/ijn5mvt/')
print(' * CasualAffair - Score 14 - "Its always the same time every Tuesday" /r/Charlotte/comments/ze56rp/brew_crew_meetup_126_omb_630_pm/iz55iuh/')
print(' * LurkerSurprise - Score 14 - "Tripled vaxed, masked and ready to drink responsibly and relax." /r/Charlotte/comments/scdvm9/brew_crew_meetup_125_630_pm_at_midnight_mulligan/hu5xq8a/')

comments = pd.read_csv ('data/Brew-Crew-Comments-2022.csv')

comments['depth_count'] = comments.groupby(['author', 'depth'])['index'].transform('count')

comments.to_csv("output/depth_count.csv", index=True, index_label="index")

print('Starting the conversation is critical and these users did that the most:')

print('  * HipsterMustache - 15')
print('  * MakeMeYourLeader - 13')
print('  * shesinanothercastle - 10')
print('  * CasualAffair - 9')
print('  * cowley10 - 5')
print('  * Emergency-Ad-7423 - 5')

print('And these users were the best at keeping the conversation going, nice job!:')

print('  * shesinanothercastle - 43')
print('  * MakeMeYourLeader - 18')
print('  * CasualAffair - 16')
print('  * bs_horse - 8')
print('  * cowley10 - 6 ')
print('  * Shirleyfunke483 - 3')

print('Great work everyone! And a big thank you to shesinanothercastle for hosting!')