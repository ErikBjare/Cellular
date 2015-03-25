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

def string_to_pattern(string):
    stringlist = string.split("\n")
    if stringlist[-1] == "":
        stringlist = stringlist[:-1]
    for row in stringlist[1:]:
        assert len(row) == len(stringlist[0])
    return _stringlist_to_pattern(stringlist)

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
def WIREWORLD_TRACK():
    return ["...........",
            "..1111111..",
            ".1.......1.",
            "..1111111..",
            "..........."]

@pattern
def WIREWORLD_DIODE():
    return ["............",
            ".....11.....",
            "111111.11111",
            ".....11.....",
            "............"]

@pattern
def HIGHLIFE_REPLICATOR():
    return [".......",
            "...xxx.",
            "..x..x.",
            ".x...x.",
            ".x..x..",
            ".xxx...",
            "......."]
