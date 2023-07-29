from typing import List

# O(n) time | O(k) (k is number of teams)
def tournament_winner(competitions: List[List], results: List):
    cur_best_team = ""
    scores = {cur_best_team: 0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition
        winning_team = home_team if result == 1 else away_team

        if winning_team not in scores:
            scores[winning_team] = 0
        scores[winning_team] += 3

        if scores[winning_team] > scores[cur_best_team]:
            cur_best_team = winning_team

    return cur_best_team
