from typing import List, Tuple
import re
import json

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    
    emoji_pattern = re.compile(r'[\U0001F300-\U0001F6FF\U0001F900-\U0001F9FF\u2600-\u26FF\u2700-\u27BF]', flags=re.UNICODE)

    emojis_dict = {}
    with open(file_path) as f:
            for jsonObj in f:
                tweetDict = json.loads(jsonObj)
                emojis = emoji_pattern.findall(tweetDict['content'])
                for emoji in emojis:
                    if emojis_dict.get(emoji) is not None:
                        emojis_dict[emoji] = emojis_dict[emoji] + 1
                    else:
                        emojis_dict[emoji] = 1


    # Sort the dictionary by values in descending order
    emojis_dict = sorted(emojis_dict.items(), key=lambda x: x[1], reverse=True)

    # Extract the top 10 values
    emojis_dict = emojis_dict[:10]
    return emojis_dict