def short_pattern():
    pattern = {"sequence" :"101", "occurences": 5}
    return pattern

def medium_pattern():
    pattern = {"sequence": "111000", "occurences": 25}
    return pattern

def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurences":50}
    return pattern

def pattern(s,o):
    return {"sequence": s, "occurences": o}


def run():
    print("Analysing patterns....")
    d = {"short pattern":short_pattern(), "medium_pattern":medium_pattern(), "long_pattern":long_pattern()}
    for k,v in d.items():
        print(f"{k}:{v}")

run()
