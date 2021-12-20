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
def add_resturants(scores):
    #ability to add a restaurant and rating 

    print("Please add a rating for your favorite resturant!")
    restaurant = input("restaurant name")
    rating = int(input("Rating>"))

    scores[restaurant] = rating 

def print_sorted_scores(scores):
    #print restaurants and rating sorted. 

    for restaurant, rating in sorted(scores.item()):
        print(f"{restaurant} is rated at {rating}." )


scores = restaurant_scores()

add_resturants(scores)

print_sorted_scores(scores)