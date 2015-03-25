def _char_to_cell(char):
    if char == ".":
        return 0
    elif char == "x":
        return 1
    elif char in "0123456789":
        return int(char)
    else:
        raise Exception("Unknown cell value")

def _stringlist_to_pattern(stringlist):
    pattern = []
    for row in stringlist:
        pattern.append([])
        for char in row:
            pattern[-1].append(_char_to_cell(char))
    return pattern

def pattern(f, *args, **kwargs):
    """Pattern decorator"""
    return _stringlist_to_pattern(f(*args, **kwargs))

@pattern
def GLIDER():
    return [".x.",
            "x..",
            "xxx"]
            
@pattern
def GLIDER_GUN():
    return ["..........................................",
            "...........................x..............",
            ".........................x.x..............",
            "...............xx......xx............xx...",
            "..............x...x....xx............xx...",
            "...xx........x.....x...xx.................",
            "...xx........x...x.xx....x.x..............",
            ".............x.....x.......x..............",
            "..............x...x.......................",
            "...............xx.........................",
            "..........................................",
            "..........................................",
            "..........................................",
            "..........................................",
            "..........................................",
            "..........................................",
            ".........................................."]

@pattern
def CIRCUIT_TRACK():
    return ["...........",
            ".111111111.",
            ".1.......1.",
            ".111111111.",
            "..........."]

@pattern
def HIGHLIFE_REPLICATOR():
    return [".......",
            "...xxx.",
            "..x..x.",
            ".x...x.",
            ".x..x..",
            ".xxx...",
            "......."]
