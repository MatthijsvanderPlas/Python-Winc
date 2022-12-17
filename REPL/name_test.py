def initials(name):
    first, last = name.split(" ")
    f, l = first[0], last[0]
    return f"{f}. {l}."


def test_initials_common_name():
    assert initials("Daniel Radcliffe") == "D. R."


def test_intials_double_barrelled():
    assert initials("Helena Bonham Carter") == "H. B. C."
