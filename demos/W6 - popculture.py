pop_dict = {"The Matrix":["Keanu Reeves", "Carrie-Anne Moss", "Hugo Weaving"],
            "Harry Potter":["Daniel Ratcliffe", "Emma Watson", "Rupert Grint"],
            "Friends":["Jennifer Aniston", "Courtney Cox", "Lisa Kudrow"],
            "The Office":["Steve Carell", "Rain Wilson", "John Krasinski"],
            "Jack Ryan": ["John Krasinski", "Abbie Cornish"],
            "DS: in MoM": ["Benedict Cumberback", "John Krasinski"]}

def get_cast(title):
    if title in pop_dict:
        return pop_dict[title]
    else:
        print(f"{title} is not part of the database")
        return  []

#t = input("What is the title of the movie you want to check? ")
#print(get_cast(t))

def add_title(title, cast):
    pop_dict[title] = cast

def count_actors():
    actors = dict()
    for cast_list in pop_dict.values():
        for actor in cast_list:
            if actor in actors:
                actors[actor] += 1
            else:
                actors[actor] = 1

    return actors
print(count_actors())



