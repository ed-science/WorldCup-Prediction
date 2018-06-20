import datetime
import pickle

from match_predictor.main import predict_proba
from match_predictor.mean_stats import get_average_goals
from scraping import get_next_day_matches

date = datetime.date.today()

matches = []
for match in get_next_day_matches(int(date.day - 14)+3):
    probs = predict_proba(
        match.home,
        match.away
    )
    avg_goals = get_average_goals(match.home, match.away, 2018, ignore_sides=True)

    match.prob_home = round(probs[1]*100, 2)
    match.prob_away = round(probs[2]*100, 2)
    match.prob_draw = round(probs[0]*100, 2)

    if avg_goals != 0:
        match.avg_goals_home = round(avg_goals[0], 2)
        match.avg_goals_away = round(avg_goals[1], 2)
    else:
        match.avg_goals_home = 0.0
        match.avg_goals_away = 0.0

    matches.append(match)

with open("matches.b", "wb") as f:
    pickle.dump(matches, f)