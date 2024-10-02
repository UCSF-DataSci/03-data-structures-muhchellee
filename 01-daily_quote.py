#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    "Nothing is impossible in this world. - Himmel",
    "Well done is better than well said. - Benjamin Franklin",
    "Don't ruin a good day because of a bad yesterday. - Irene Bae",
    "Be yourself; everyone else is already taken. - Oscar Wilde",
    "All that we are is the result of what we have thought. - Buddha",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "The lesson you need to learn right now can't be taught with words, only with action. - Levi Ackerman",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
]

def get_quote_of_the_day(quotes):
    todays_quote = None

    random.seed(date.today().toordinal())
    
    todays_quote = random.choice(quotes)

    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt