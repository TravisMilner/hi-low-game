import random

numbers = [1,2,3,4,5,6,7,8,9,10]

player = int(input(f"Choose a number: {numbers}"))
computer = random.choice(numbers)

def hi_low(p, c):
    
    
    if p == c:
        print(f"Tie: {p} equals {c}")
        return p and c
    
    if p > c:
        print(f"Winner: {p} is better than {c}")
        return p

    if c > p:
        print(f"Loser: {c} is greater than {p}")
        return c


hi_low(player, computer)


