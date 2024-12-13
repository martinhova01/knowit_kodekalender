
base_salary = 100
teams = {
    "FCB": 0.01,
    "J": 0.02,
    "NT": 0.01,
    "NF": 0.01,
    "RC": 0.03,
    "SP": 0.02,
    "VM": 0.03
}
salary = 0
loss_multiplier = 0.0
for match in open("salary.txt").read().rstrip().split(",\n"):
    multiplier = 1.0
    stats = match.split("/")
    play_time = int(stats[1])
    where = stats[2]
    score = stats[3]
    home, away = [int(x) for x in score.split("-")]
    
    # goal bonuses
    if where == "H":
        multiplier += 0.05 * home - 0.05 * away
    else:
        multiplier += 0.05 * away - 0.05 * home
    
    # action bonuses(score, assist, player of the match)
    for action in stats[4]:
        if action == "S" or action == "B":
            multiplier += 0.02
        else:
            multiplier += 0.01
            
    if (where == "H" and home > away) or (where == "B" and away > home):
        # win
        multiplier += teams[stats[0]]  
         
        multiplier += loss_multiplier
        loss_multiplier = 0
        
    elif home == away:
        # draw
        pass
    
    else:
        # loss
        multiplier -= teams[stats[0]]  
        
        if loss_multiplier == 0:
            loss_multiplier = 0.03
        else:  
            loss_multiplier += 0.01
    
    salary += play_time * base_salary * multiplier

print(salary)