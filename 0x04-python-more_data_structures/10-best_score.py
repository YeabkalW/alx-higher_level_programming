#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None
    else:
        max_score = max(a_dictionary.values())
        for k, v in a_dictionary.items():
            if v is max_score:
                return k
