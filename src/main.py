import csv
import os
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "raw"

# Display files
for file in DATA_DIR.iterdir():
    print(file.name)

# Define the CSV path
CSV_PATH = DATA_DIR / "backloggd-maxb059-2026-10-13.csv"

# Open the CSV file
with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    games = list(reader)
    # print(reader.fieldnames)

    # for index, row in enumerate(games, start = 1):
    #     print(index, row)
        

# Challenge 1 -- Count rated games
#   Count how many records have a nonempty "Rating" field

# Challenge 2 -- Counting backlog games
#   Count how many records have "In Backlog" set to "true"
total_games = 0
rated_games = 0
in_backlog = 0
for game in games:
    if (game["Rating"] not in ('0', '')):
       rated_games += 1
    total_games += 1
    if (game["In Backlog"] == 'true'):
        in_backlog += 1

print(f"Total games: {total_games}")
print(f"Rated games: {rated_games}")
print(f"In backlog: {in_backlog}")

# Challenge 3 -- Check for duplicate IDs
#   Determine whether any records share the same "ID"
game_ids = []
for game in games:
    game_ids.append(game["ID"])
unique_ids = set(game_ids)
## print(unique_ids)
if (len(game_ids) == len(unique_ids)):
    duplicate_ids = False
else:
    duplicate_ids = True
print(duplicate_ids)


# Counts how many entries there are for each rating number
ratings = []
for game in games:
    ratings.append(game["Rating"])
    ## print(game["Rating"] + " ")
rating_counts = Counter(ratings)
for rating, count in rating_counts.items():
    print(f"Rating {rating!r}: {count} games")

print("Total records:", len(games))
unrated_games = rating_counts['0'] + rating_counts['']
rated_games = len(games) - unrated_games


# Converts the ratings in string form to numbers
converted_ratings = []
for game in games:
    raw_rating = game["Rating"].strip()

    if raw_rating in ("0", ""):
        converted_ratings.append(None)
    else:
        converted_ratings.append((int)(raw_rating))

# Checks for invalid ratings
invalid_ratings = []
for rating in converted_ratings:
    if rating is not None:
        if rating <= 10 or rating < 1:
            continue
        else:
            invalid_ratings.append(rating)

print("Invalid ratings:", invalid_ratings)

# Converts the played value from a string to a boolean
converted_played = []
played_games = 0
unplayed_games = 0
for game in games:
    is_played = game["Played"].strip().lower() == "true"
    if is_played:
        played_games += 1
    else:
        unplayed_games += 1
    converted_played.append(is_played)
print("Played games:", played_games)
print("Unplayed games:", unplayed_games)

# Converts the currently playing value from a string to a boolean
converted_currently_playing = []
currently_playing_games = 0
not_currently_playing_games = 0
for game in games:
    currently_being_played = game["Currently Playing"].strip().lower() == "true"
    if currently_being_played:
        currently_playing_games += 1
    else:
        not_currently_playing_games += 1
    converted_currently_playing.append(currently_being_played)
print("Games currently being played:", currently_playing_games)
print("Games not currently being played:", not_currently_playing_games)

# Converts the in backlog value from a string to a boolean
converted_in_backlog = []
currently_in_backlog = 0
not_currently_in_backlog = 0

for game in games:
    is_in_backlog = game["In Backlog"].strip().lower() == "true"
    if is_in_backlog:
        currently_in_backlog += 1
    else:
        not_currently_in_backlog += 1
    converted_in_backlog.append(is_in_backlog)
print("Games currently in backlog:", currently_in_backlog)
print("Games not currently in backlog:", not_currently_in_backlog)

# Converts the in wishlist value from a string to a boolean
converted_in_wishlist = []
currently_in_wishlist = 0
not_currently_in_wishlist = 0

for game in games:
    is_in_wishlist = game["In Wishlist"].strip().lower() == "true"
    if is_in_wishlist:
        currently_in_wishlist += 1
    else:
        not_currently_in_wishlist += 1
    converted_in_wishlist.append(is_in_wishlist)
print("Games currently in wishlist:", currently_in_wishlist)
print("Games not currently in wishlist:", not_currently_in_wishlist)

# Converts the liked value from a string to a boolean
converted_liked = []
liked_amount = 0
not_liked_amount = 0

for game in games:
    is_liked = game["Liked"].strip().lower() == "true"
    if is_liked:
        liked_amount += 1
    else:
        not_liked_amount += 1
    converted_liked.append(is_liked)
print("Liked games:", liked_amount)
print("Not liked games:", not_liked_amount)

# Converts the mastered value from a string to a boolean
converted_mastered = []
mastered_amount = 0
not_mastered_amount = 0

for game in games:
    is_mastered = game["Mastered"].strip().lower() == "true"
    if is_mastered:
        mastered_amount += 1
    else:
        not_mastered_amount += 1
    converted_mastered.append(is_mastered)
print("Mastered games:", mastered_amount)
print("Not mastered games:", not_mastered_amount)

# Converts the replay value from a string to a boolean
converted_replay = []
replay_amount = 0
not_replay_amount = 0

for game in games:
    is_replayed = game["Replay"].strip().lower() == "true"
    if is_replayed:
        replay_amount += 1
    else:
        not_replay_amount += 1
    converted_replay.append(is_replayed)
print("Replayed games:", replay_amount)
print("Not replayed games:", not_replay_amount)