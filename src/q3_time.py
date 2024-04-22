from typing import List, Tuple
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mentioned_users_dict = {}
    with open(file_path) as f:
            for jsonObj in f:
                tweetDict = json.loads(jsonObj)
                mentioned_users = tweetDict['mentionedUsers']
                if mentioned_users is not None:
                    for user in mentioned_users:
                        username = user['username']
                        if mentioned_users_dict.get(username) is not None:
                            mentioned_users_dict[username] = mentioned_users_dict[username] + 1
                        else:
                            mentioned_users_dict[username] = 1


    # Sorts the dictionary by values in descending order
    mentioned_users_dict = sorted(mentioned_users_dict.items(), key=lambda x: x[1], reverse=True)

    # Extracts the top 10 values
    mentioned_users_dict = mentioned_users_dict[:10]
    return mentioned_users_dict