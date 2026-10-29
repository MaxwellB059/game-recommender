import csv
import os
import json
from pathlib import Path
from collections import Counter
from datetime import date

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Display files
for file in DATA_DIR.iterdir():
    print(file.name)

# Define the CSV path
# The CSV is stored alongside this script in src; platforms.json is in processed data.
CSV_PATH = PROJECT_ROOT / "data" / "raw" / "backloggd-maxb059-2026-10-13.csv"
JSON_PATH = DATA_DIR / "platforms.json"

# Open the CSV file
with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    games = list(reader)    # print(reader.fieldnames)

    for index, row in enumerate(games, start = 1):
        print(index, row)
        

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
        if rating < 1 or rating > 10:
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

# Converts the start time value from a string to a date type
# From datetime library
converted_startdates = []
startdate_amount = 0
no_startdate_amount = 0
for game in games:
    startdate = game["Start Date"].strip()
    if startdate in ("0", ""):
        converted_startdates.append(None)
        no_startdate_amount += 1
    else:
        converted_startdates.append(date.fromisoformat(startdate))
        startdate_amount += 1

# Converts the finish time value from a string to a date type
# From datetime library
converted_finishdates = []
finishdate_amount = 0
no_finishdate_amount = 0
for game in games:
    finishdate = game["Finish Date"].strip()
    if finishdate in ("0", ""):
        converted_finishdates.append(None)
        no_finishdate_amount += 1
    else:
        converted_finishdates.append(date.fromisoformat(finishdate))
        finishdate_amount += 1

# move on from here

# From the data above, create dictionary entries for each

cleaned_games = []
for index, game in enumerate(games):
    cleaned_game = {
        "id": game["ID"],
        "name": game["Game Name"],
        "rating": converted_ratings[index],
        "played": converted_played[index],
        "currently_playing": converted_currently_playing[index],
        "in_backlog": converted_in_backlog[index],
        "start_date": converted_startdates[index],
        "finish_date": converted_finishdates[index]
    }
    cleaned_games.append(cleaned_game)

print("Total cleaned games:", len(cleaned_games))
print("First cleaned game:", cleaned_games[0])

# Define where processed data will be stored
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

# Create the folder if it doesn't exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Define the output file
CLEANED_GAMES_PATH = PROCESSED_DIR / "cleaned_games.json"

# Save cleaned games to JSON
with CLEANED_GAMES_PATH.open("w", encoding="utf-8") as file:
    json.dump(cleaned_games, file, indent=4, default=str)

print("Cleaned games saved successfully!")


# Filter the game collection
backlog_and_not_played = []
for game in cleaned_games:
    if game["in_backlog"] is True and game["played"] is False:
        backlog_and_not_played.append(game)
        print(game["name"])
print(len(backlog_and_not_played))

if JSON_PATH.exists():
    with JSON_PATH.open("r", encoding="utf-8") as file:
        platforms = json.load(file)
else:
    platforms = []
    print(f"Platforms file not found: {JSON_PATH}")

platform_lookup = {}

for platform in platforms:
    platform_id = platform.get("id", platform.get("ID"))
    platform_name = platform.get("name", platform.get("Name"))
    if platform_id is not None and platform_name is not None:
        platform_lookup[str(platform_id)] = platform_name

print("Total platforms:", len(platform_lookup))
print("Platform 5:", platform_lookup.get("5", "Unknown"))

# Load the platform IDs from the Backloggd game export.  The CSV does not
# contain the platform data reliably, so match records by game ID instead of
# by their position in the file.
# Load the original Backloggd JSON containing playthrough information
RAW_DIR = PROJECT_ROOT / "data" / "raw"

backloggd_files = list(RAW_DIR.glob("backloggd-*.json"))

# Check processed folder if the file isn't in raw
if not backloggd_files:
    backloggd_files = list(DATA_DIR.glob("backloggd-*.json"))

if not backloggd_files:
    raise FileNotFoundError("Backloggd JSON export not found.")

if len(backloggd_files) > 1:
    raise ValueError("Multiple Backloggd JSON exports found. Specify which file to use.")

with backloggd_files[0].open("r", encoding="utf-8") as file:
    backloggd_games = json.load(file)

print("Backloggd JSON games loaded:", len(backloggd_games))


# Create a dictionary matching game IDs to their played platform IDs
platform_ids_by_game_id = {}

for backloggd_game in backloggd_games:
    game_id = str(backloggd_game["id"])

    # Retrieve the game's playthroughs
    playthroughs = backloggd_game.get("playthroughs") or {}

    # Use a set to prevent duplicate platforms
    platform_ids = set()

    # Each playthrough may contain a platform ID
    for playthrough in playthroughs.values():
        platform_id = playthrough.get("platform")

        # Ignore playthroughs without recorded platforms
        if platform_id is not None:
            platform_ids.add(str(platform_id))

    # Associate the game ID with its platform IDs
    platform_ids_by_game_id[game_id] = platform_ids


# Attach platform information to our cleaned games
for cleaned_game in cleaned_games:
    game_id = str(cleaned_game["id"])

    # Retrieve the platform IDs for this game
    platform_ids = platform_ids_by_game_id.get(game_id, set())

    # Convert platform IDs to their corresponding IGDB names
    cleaned_game["played_on"] = [
        {
            "id": int(platform_id),
            "name": platform_lookup.get(platform_id, "Unknown")
        }
        for platform_id in sorted(platform_ids, key=int)
    ]


# Save the updated cleaned games JSON
with CLEANED_GAMES_PATH.open("w", encoding="utf-8") as file:
    json.dump(cleaned_games, file, indent=4, default=str)

print("Platforms attached and cleaned games saved successfully!")


# Verify platform information for Super Mario Galaxy 2
for game in cleaned_games:
    if game["id"] == "1078":
        print(game["name"])
        print(game["played_on"])
        break


# Count games with recorded platforms
games_with_platforms = sum(
    bool(game["played_on"]) for game in cleaned_games
)

print("Games with recorded platforms:", games_with_platforms)


## Your next programming challenge
## Write code that answers these questions:
##  1. How many games have at least one platform recorded in played_on?
##  2. How many games have an empty played_on list?
##  3. Are there any games with a platform named "Unknown"?
##  4. We still have exactly 611 games after combining the datasets?