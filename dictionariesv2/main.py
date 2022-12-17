# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
def get_country(nationality):
    list_of_countries = get_countries()
    if nationality in list_of_countries:
        idx = list_of_countries.index(nationality)
        return list_of_countries[idx]


def create_passport(name, date_of_birth, place_of_birth, height, nationality):

    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": get_country(nationality),
    }

    return passport


def add_stamp(passport, country):
    if "stamps" in passport:
        if country not in passport["stamps"]:
            if country != passport["nationality"]:
                passport["stamps"].append(country)
    else:
        if country != passport["nationality"]:
            passport["stamps"] = [country]
    return passport


def add_biometric_data(passport, biometric_type, value, date):
    if "biometric" not in passport:
        passport["biometric"] = {}
        passport["biometric"][biometric_type] = {"date": date, "value": value}
    else:
        passport["biometric"][biometric_type] = {"date": date, "value": value}
    return passport


omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
print(omari)

# Omari gets a new left eye because of an accident
omari = add_biometric_data(omari, "eye_color_left", "brown", "2022-01-10")
print(omari)

# Add fingerprints too: just another value, but this is also a dict.
fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}

omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
print(omari)
