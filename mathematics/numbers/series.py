def sum(list = None):
    added = 0
    for lists in list:
        added += lists
    return added

def average(list = None):
    return sum(list) / len(list)