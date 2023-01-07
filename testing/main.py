def get_none(_a, _b):
    return None


def flatten_dict(inputVar):
    newList = []

    if isinstance(inputVar, dict):
        for _, val in inputVar.items():
            res = flatten_dict(val)
            for val in res:
                newList.append(val)
    elif isinstance(inputVar, list):
        for value in inputVar:
            res = flatten_dict(value)
            for val in res:
                newList.append(val)
    else:
        newList.append(inputVar)

    return newList
