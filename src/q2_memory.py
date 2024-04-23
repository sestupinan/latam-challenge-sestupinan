from typing import List, Tuple
import re
import json
from collections import Counter
from memory_profiler import profile

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    
    # Regex pattern for emojis
    emoji_pattern = re.compile(r'[\U0001F300-\U0001F6FF\U0001F900-\U0001F9FF\u2600-\u26FF\u2700-\u27BF]', flags=re.UNICODE)

    emojis_dict = {}
    with open(file_path) as f:
            for jsonObj in f:
                tweetDict = json.loads(jsonObj)
                # Uses the regex previously created to find all the emojis in the tweet content
                emojis = emoji_pattern.findall(tweetDict['content'])
                for emoji in emojis:
                    # Sums 1 to the quantity of appereances of the emoji if it already exists
                    if emojis_dict.get(emoji) is not None:
                        emojis_dict[emoji] = emojis_dict[emoji] + 1
                    # Adds the emoji to the dictionary and sets the value to 1 if it did not exist
                    else:
                        emojis_dict[emoji] = 1


    # Sorts the dictionary by values in descending order
    emojis_dict = sorted(emojis_dict.items(), key=lambda x: x[1], reverse=True)

    # Extracts the top 10 emojis
    emojis_dict = emojis_dict[:10]
    return emojis_dict