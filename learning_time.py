def getLearningTime(rate, target):
    months = 0
    knowledge = 0
    
    while knowledge < target:
        months += 1
        knowledge = knowledge + ((1-knowledge)*rate)
    return(months)

print(getLearningTime(0.1, 0.9))
