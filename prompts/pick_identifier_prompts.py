# These are saved in chatGPT as commands.

GET_EVENTS_AND_PICKS = """Parse the article and extract the suggested bets with the following properties:
1. For each suggested bet:
   a. Identify the line type (moneyline, spread, total).
   b. Determine the period type (game, quarter, half etc.), assuming "game" if not mentioned.
   c. Determine if the bet is a prop bet.
   d. Extract the specific bet type (strikeouts, outs recorded, etc.).
   e. Identify the side of the bet (over, under, home, away, etc.).
   f. Extract the numeric value associated with the bet.
   g. Identify the player if mentioned.
   h. Identify the team if mentioned.
   i. Group the bets under their respective events.

2. Identify the events mentioned in the article.
   a. Event name
   b. City for each team (home and away) mentioned in the event.
   c. Event date
   d. Event time

3. Structure the output in JSON format with the following structure:
   {
     "events": [
       {
         "event_name": "<EVENT_NAME>",
         "city": {
           "home": "<HOME_CITY>",
           "away": "<AWAY_CITY>"
         },
         "time": "<EVENT_TIME>",
         "bets": [
           {
             "line_type": "<LINE_TYPE>",
             "period_type": "<PERIOD_TYPE>",
             "is_prop": <IS_PROP>,
             "bet_type": "<BET_TYPE>",
             "side": "<SIDE>",
             "player": "<PLAYER>",
             "team": "<TEAM>",
             "value": <VALUE>
           },
           ...
         ]
       },
       ...
     ]
   }
Provide the json object as the final result."""