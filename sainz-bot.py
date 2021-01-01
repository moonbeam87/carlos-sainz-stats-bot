#!/usr/bin/python
import praw
import time


userAgent = 'sainz-jr-stats-bot'
cID = ''
cSC= ''
userN = 'sainz-jr-stat-bot'
userP =''

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)
subreddit = reddit.subreddit('formula1') 
row1 = 'Best Quali Finish - P2\n\n'
row2 = 'Number of Poles - 0\n\n'
row3 = 'Best Driver Standings Finish - P6 (2020)\n\n'
row4 = 'Best Race Finish - P2\n\n'
row5 = 'Number of Podiums - 2\n\n'
row6 = 'Number of Track Records - 1\n\n'
row7 = 'Race Car Number - 55\n\n'
row8 = "I am a bot made to educate users on some common Sainz Jr Stats! Please give me feedback"
response = row1+row2+row3+row4+row5+row6+row7
bot_phrase = "You mentioned Sainz Jr. Here are some stats: \n\n"+response 
keywords = {'Carlos', 'Sainz', 'Sainz Jr', 'Carlando'} 

comments_replied_to = []
for comment in subreddit.comments(limit=1000):
    for i in keywords:
        if i in comment.body and comment.id not in comments_replied_to and comment.author != userN:
            print('Sainz-jr-stat-bot replying to: ') 
            print("---------------------------------")
            print('Bot saying: ', bot_phrase)
            print()
            comments_replied_to.append(comment.id)
            comment.reply(bot_phrase)
            time.sleep(1)
            

if numFound == 0:
    print()
    print("Sorry, didn't find any posts with those keywords, try again!")