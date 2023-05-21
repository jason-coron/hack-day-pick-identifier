# These are saved in chatGPT as commands.

GET_EVENTS_AND_PICKS_FROM_CONTENT = """Parse the article and extract the suggested bets with the following properties:
1. For each suggested bet:
   a. Identify the line type (moneyline, spread, total). It the side of the bet is over or under, the line type will be total.
   b. Determine the period type (game, quarter, half etc.), assuming "game" if not mentioned.
   c. Determine if the bet is a prop bet.
   d. Extract the specific bet type (strikeouts, outs recorded, Anytime Goalscorer etc.).
   e. Identify the side of the bet (over, under, home, away, etc.).
   f. Extract the numeric value associated with the bet.
   g. Identify the player if mentioned.
   h. Identify the team if mentioned.
   i. Group the bets under their respective events.

2. Identify the events mentioned in the article.
   a. Event name
   b. Teams including the city for each team (home and away) mentioned in the event.
   c. Event date as a string in YYYY-MM-DD format. If not able to determine, assume it is the next event involving the teams or players mentioned.
   d. Event time as a string in HH:MM:SS format. If not able to determine, assume it is the next event involving the teams or players mentioned.

3. Structure the output in JSON format with the following structure:
   {
     "events": [
       {
         "event_name": "<EVENT_NAME>",
         "teams": {
           "home": "<HOME>",
           "away": "<AWAY>"
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