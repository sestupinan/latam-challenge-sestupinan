from typing import List, Tuple
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    
    # Dictionary to store the count of each mentioned user
    mentioned_users_dict = {}
    with open(file_path) as f:
            for jsonObj in f:
                tweetDict = json.loads(jsonObj)
                # We only need the mentioned users JSON part
                # ASSUMPTION: it is assumed that the mentioned users inside the quotedTweet part should not be counted for this
                # (In case that it is needed, we only need to add another for statement that will behave similarly to the one below)
                mentioned_users = tweetDict['mentionedUsers']
                if mentioned_users is not None:
                    for user in mentioned_users:
                        username = user['username']
                        
                        # Sums 1 to the quantity of appereances of the emoji if it already exists
                        if mentioned_users_dict.get(username) is not None:
                            mentioned_users_dict[username] = mentioned_users_dict[username] + 1
                            
                        # Adds the emoji to the dictionary and sets the value to 1 if it did not exist
                        else:
                            mentioned_users_dict[username] = 1


    # Sorts the dictionary by values in descending order
    mentioned_users_dict = sorted(mentioned_users_dict.items(), key=lambda x: x[1], reverse=True)

    # Extracts the top 10 values
    mentioned_users_dict = mentioned_users_dict[:10]
    return mentioned_users_dict