# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
def alphabetical_order(input_list):
    return sorted(input_list)

def won_golden_globe(film):
    golden_globe_winners = ['jaws', 'star wars: episode iv - a new hope', 'e.t. the extra-terrestrial', 'memoirs of a geisha']
    return film.lower() in golden_globe_winners

def remove_toto_albums(album_list):
    albums_to_remove = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New']
    return [album for album in album_list if album not in albums_to_remove]