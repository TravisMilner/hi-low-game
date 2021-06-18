def hi_low(player, computer):
    if player == computer:
        return "Tie"
    
    if player > computer:
        return "Winner"

    if computer > player:
        return "Loser"

        

