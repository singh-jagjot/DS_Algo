from typing import List


def tournament_winner(competetions:List[List], results:List):
    curBestTeam = ""
    scores = {curBestTeam: 0}
    for idx, competetion in enumerate(competetions):
        result = results[idx]
        homeTeam, awayteam = competetion
        winningTeam = homeTeam if result == 1 else awayteam
        
        if winningTeam not in scores:
            scores[winningTeam] = 0
        scores[winningTeam] += 3
        
        if scores[winningTeam] > scores[curBestTeam]:
            curBestTeam = winningTeam
    
    return curBestTeam