from typing import List, Tuple
from datetime import datetime
import pandas as pd

# Function to calculate the username with most posts in each of the top 10 days with the most posts (optimizing time)
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    # Data loading
    df = pd.read_json(file_path, lines=True)
    
    # Create a date column using the datetime provided
    df['date_t'] = pd.to_datetime(df['date']).dt.date
    
    # Compute the top 10 days with the most posts
    max_days = df.groupby("date_t").size().nlargest(10)
    
    # Compute the top 10 days with the most posts
    df_usernames = pd.concat([df[['date_t']], df['user'].str['username']], axis = 1)
    
    # Compute the top users with the most posts per day
    max_users = df_usernames.groupby(["date_t","user"]).size()
    
    # Extract the top users only for the top 10 days
    most_repeated_users_per_day = []
    for date in max_days.index:
        most_repeated_users_per_day.append((date, max_users[date].idxmax())) 
    return most_repeated_users_per_day