import os
import pandas as pd
import numpy as np
import random
import json

# Obtain the number of twitter followers
def getFollowers(username):
    os.system("snscrape --jsonl --max-results {} twitter-search 'from:{}'> data/example-tweets.json".format(1, username))
    
    followers = pd.read_json('data/example-tweets.json'.format(username), lines=True).to_numpy()[0][6]['followersCount']
    return [username, followers]

def scrape(username, tweet_count = 1000000):
    # Reference: https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af
    # Using OS library to call CLI commands in Python
    os.system("snscrape --jsonl --max-results {} twitter-search 'from:{}'> data/user-{}-tweets.json".format(tweet_count, username, username))

def cleanData(data, username):
    parseDate = lambda x: [x.week, x.month, x.year]
    
    # Extract user, date, content, replyCount, retweetCount, and likeCount
    data = data.loc[:, ['user', 'date', 'content', 'replyCount', 'retweetCount', 'likeCount']]

    # Extract username from user
    username = data['user'][0]['username']
    data['user'] = username

    # Convert date: [week, month, year]
    data['date'] = data['date'].apply(np.vectorize(parseDate))
    
    data.to_csv('data/user-{}-tweets-cleaned.csv'.format(username), index = False)

def generateChoroplethData(usernames):
    df_states = pd.read_csv('state-survey-responses-fa21.csv')
    states = df_states['state_name'].to_numpy()

    finalDict = {}
    # Populate each state with an empty dictionary
    for state in states:
        finalDict[state] = {}
    
    for username in usernames:
        print(username)
        tweets_df = pd.read_csv('cleaned-data/user-{}-tweets-cleaned.csv'.format(username), lineterminator='\n')

        for state in states:
            stateLower = state.lower()
            count = 0

            for val in tweets_df.loc[:,'content']:
                if (stateLower in str(val).lower()):
                    count += 1

            finalDict[state][username] = count
    
    return finalDict
    
def addTotalFollowers(finalDict, usernames):
    finalDict['Num_Tweets'] = {}
    for username in usernames:
        print(username)
        if username == 'ariannahuff':
            tweets_df = pd.read_csv('cleaned-data/user-{}-tweets-cleaned.csv'.format(username), lineterminator='\n')
        else:
            tweets_df = pd.read_csv('cleaned-data/user-{}-tweets-cleaned.csv'.format(username))
        numTweets = tweets_df.loc[:,'content'].to_numpy().shape[0]
        finalDict['Num_Tweets'][username] = numTweets
    
    return finalDict

def addTotalTweets(finalDict, usernames):
    finalDict['total'] = {}

    for username in usernames:
        count = 0
        for state in finalDict:
            if state != 'total' and state != 'Num_Tweets':
                count += finalDict[state][username]
        finalDict['total'][username] = count
    
    return finalDict

def saveData(data, fileName):
    with open(fileName,'w') as f:
        json.dump(datat, f)

def updateWordMentions(new_data, usernames, words):
    for username in usernames:
        data = pd.read_json('data/user-{}-tweets.json'.format(username), lines=True)['content'].to_numpy()

        for word in words:
            count = 0
            for tweet in data:
                if word in tweet.lower():
                    count += 1
            new_data[username][word] = count
   
    return new_data

