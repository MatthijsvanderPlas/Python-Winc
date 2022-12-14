from helpers import get_countries
import string


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
def shortest_names(list_of_countries):
    """Filter and return the shortest names in a list of strings

    Args:
        countries (strings): list of countries

    Returns:
        list: list of countries with the shortest name
    """
    short_countries = []
    current_length = 20
    for country in list_of_countries:
        if len(country) < current_length:
            short_countries = [country]
            current_length = len(country)
        elif len(country) == current_length:
            short_countries.append(country)
        elif len(country) > current_length:
            continue
    return short_countries
    
def most_vowels(list_of_countries):
    vowels = ['a','e','i','o','u']
    result = []
    for country in list_of_countries:
        count = 0
        for char in country:
            if char.lower() in vowels:
                count += 1
        result.append((country, count))
        result = sorted(result, key=lambda x: x[1],reverse=True)[:3]
    return [result[0][0], result[1][0], result[2][0]]

def count_letter_of_alphabet(input_string, alphabet):
    count = 0
    for c in input_string:
        if c in alphabet:
            count += 1
    return count

def alphabet_set(list_of_countries):
    alphabet = list(string.ascii_lowercase)
    result = []
    all_countries = list_of_countries
    for i in range(len(list_of_countries)):
        sorted_list = sorted(all_countries, key=lambda x: count_letter_of_alphabet(x, alphabet), reverse=True)
        for character in sorted_list[0].lower():
            if character in alphabet:
                alphabet.pop(alphabet.index(character))
        result.append(sorted_list[0])
        all_countries.pop(all_countries.index(sorted_list[0]))
        if len(alphabet) == 0:
            break
    return result


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

    shortest_names = shortest_names(countries)

    most_vowels = most_vowels(countries)

    alphabet_set = alphabet_set(countries)
