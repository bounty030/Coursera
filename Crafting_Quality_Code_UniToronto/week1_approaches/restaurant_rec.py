# Learn to Program: Crafting Quality Code
# Week 1 - Restaurant Recommendation

# The first step to solving the restaurant recommendations problem is 
# choosing data structures to store the information on restaurant prices, 
# ratings, and cuisines.

# For the data see text file 'restaurant_small.txt'

"""
# dict of {str: int}
name_to_rating = {  'Georgie Porgie': 87,
                    'Queen St. Cafe': 82,
                    'Dumplings R Us': 71,
                    'Mexican Grill': 85,
                    'Deep Fried Everything': 52} 

# dict of {str: list of str}
price_to_names = {  '$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
                    '$$': ['Mexican Grill'],
                    '$$$': ['Georgie Porgie'],
                    '$$$$': []} 

# dict of {str: list of str}
cuisine_to_names = { 'Canadian': ['Georgie Porgie'],
                    'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
                    'Malaysian': ['Queen St. Cafe'],
                    'Thai': ['Queen St. Cafe'],
                    'Chinese': ['Dumplings R Us'],
                    'Mexican': ['Mexican Grill']} 

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    # First the price and then the restaurant name because when the nested lists are sorted by the first value.
    # In this case price.
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of list of str

    Find restaurant in file that are priced according to price and that are
    tagged with any of the items in cuisines_list. Return a list of lists of 
    the form [ratings, restaurant name], sorted by ratings.
    """

    # Read the file and build the data structures.
    name_to_rating, price_to_names, cuisine_to_names = read_restaurant(file)


    # Look up the restaurant names for the requested price.
    names_matching_price = price_to_names[price]


    # Now we have a list of restaurants in the right price range.
    # Get new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisines(names_matching_price, cuisine_to_names, cuisines_list)


    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    return result


def build_rating_list(name_to_rating, names_final):
    """(dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {  'Georgie Porgie': 87,
                    'Queen St. Cafe': 82,
                    'Dumplings R Us': 71,
                    'Mexican Grill': 85,
                    'Deep Fried Everything': 52}
    >>> names_final = ['Queen St. Cafe', 'Dumplings R Us']
    >>> build_rating_list(name_to_rating, names_final)
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

    result = list()

    # Go through final restaurant names and select rating from other dict.
    # Create list of lists with restaurant name and rating.
    for name in names_final:
        rating = name_to_rating[name]
        name_and_ratings = list()
        name_and_ratings.append([rating, name])
        result.append(name_and_ratings)

    result.sort(reverse=True)

    return result


def filter_by_cuisines(names_matching_price, cuisine_to_names, cuisines_list):
    """(list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names_matching_price = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuisine_to_names = { 'Canadian': ['Georgie Porgie'],
                    'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
                    'Malaysian': ['Queen St. Cafe'],
                    'Thai': ['Queen St. Cafe'],
                    'Chinese': ['Dumplings R Us'],
                    'Mexican': ['Mexican Grill']} 
    >>> cuisines_list = ['Chinese', 'Thai']
    >>> filter_by_cuisines(names_matching_price, cuisine_to_names, cuisines_list)
    ['Queen St. Cafe', 'Dumplings R Us']
    """

    # List for restaurants which serve cuisines
    names_final = list()

    # Go through the cuisines you want to eat.
    for cuisine in cuisines_list:
        # Look for restaurants which serve the cuisines
        for name in cuisine_to_names[cuisine]:
            # If restaurant serves the cuisines add it the list
            if name in names_matching_price:
                names_final.append(name)


    return names_final


def read_restaurant(file):
    """(file open for reading) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:
    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    # Every 5 lines the restaurant changes in the text file.
    lines = 5

    # Read the whole text file.
    file_list = file.readlines()

    # Loop through the text file and read all data about one restaurant
    # Every 5 lines the data about one restaurant is done
    for i in range(len(file_list) // lines):
        name = file_list[i*lines].rstrip()
        rating = file_list[i*lines + 1].rstrip()
        price = file_list[i*lines + 2].rstrip()
        cuisine = file_list[i*lines + 3].rstrip()

        # Put data into dictionaries
        name_to_rating[name] = rating
        price_to_names[price].append(name)

        # Split the string of cuisines if restaurant servers more than one cuisine
        if cuisine.find(',') > 0:
            cuisine.replace(" ", "")
            cuisines_list = cuisine.split(',')
        else:
            cuisines_list = [cuisine]

        # Loop through all cuisines and create seperate entry in dict for every cuisine
        for cuisine in cuisines_list:
            # If dictionary key does not exist yet create an empty list
            if cuisine not in cuisine_to_names: 
                cuisine_to_names[cuisine] = list()

            cuisine_to_names[cuisine].append(name)


    return (name_to_rating, price_to_names, cuisine_to_names)

if __name__ == '__main__':

    # Path to file filename
    path = '/home/tbfk/Documents/VSC/Git/Coursera/Crafting_Quality_Code_UniToronto/week1/'

    # The file containing the restaurant data.
    FILENAME = 'restaurant_small.txt'
    
    # Open file and close it once done
    with open(path + FILENAME, 'r') as f:

        # Get restaurant recommendation based on price and cuisines. 
        result = recommend(f, '$', ['Chinese', 'Thai'])


    print(result)