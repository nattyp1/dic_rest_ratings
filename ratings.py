"""Restaurant rating lister."""


# put your code here
def restaurant_scores():
    # read scores file
    score_info = open('scores.txt')

    scores = {}
    
    # return dictorionary of {restaurnat-name: score

    for line in score_info :
        line = line.rstrip() 
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)

    return scores 

