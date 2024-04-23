from typing import List, Tuple
from datetime import datetime
import json
from datetime import datetime
from collections import defaultdict
from memory_profiler import profile

# Function to calculate the username with most posts in each of the top 10 days with the most posts (optimizing memory)
@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Dictionaries to store the information
    date_list = defaultdict(int) # Dict with number of posts on that day
    user_date_list = defaultdict(int) # Dict with number of posts per user on that day
    
    # Date format to use
    format = '%Y-%m-%d'
    with open(file_path) as f:
        for jsonObj in f:
            # To optimize memory, we are only storing in permanent variables the two fields we need (date and username)
            tweetDict = json.loads(jsonObj)
            formatted_date = datetime.strptime(tweetDict['date'].split('T')[0], format).date()
            username = tweetDict['user']['username']
            date_list[formatted_date] +=1
            user_date_list[(formatted_date, username)]+=1

    # Sorts the dictionary by values in descending order
    date_list = sorted(date_list.items(), key=lambda x: x[1], reverse=True)

    # Extracts the top 10 dates
    date_list = date_list[:10]
            
    listed = []
    
    # Computes top user per day
    for date, n in date_list:
        max_tweets = 0
        max_user = ''
        for (tweet_date, username), count in user_date_list.items():        
            if tweet_date == date and count > max_tweets:  
                max_tweets = count
                max_user = username
        listed.append((date, max_user))
    return listed
