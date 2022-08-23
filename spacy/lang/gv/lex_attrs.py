from ...attrs import LIKE_NUM


_num_words = [
    "neunhee",
    "nane",
    "unnane",
    "un",
    "jees",
    "daa",
    "tree",
    "kiare",
    "queig",
    "shey",
    "shiaght",
    "hoght",
    "nuy",
    "jeih",
    "nane-jeig",
    "unnane-jeig",
    "daa-yeig",
    "tree-jeig",
    "kiare-jeig",
    "queig-jeig",
    "shey-jeig",
    "shiaght-jeig",
    "hoght-jeig",
    "nuy-jeig",
    "feed",
    "nane as feed",
    "jees as feed",
    "tree as feed",
    "kiare as feed",
    "queig as feed",
    "shey as feed",
    "shiaght as feed",
    "hoght as feed",
    "nuy as feed",
    "jeih as feed",
    "nane-jeig as feed",
    "daa-yeig as feed",
    "tree-jeig as feed",
    "kiare-jeig as feed",
    "queig-jeig as feed",
    "shey-jeig as feed",
    "shiaght-jeig as feed",
    "hoght-jeig as feed",
    "nuy-jeig as feed",
    "daeed",
    "lieh cheead",
    "jeih as daeed",
    "queigad",
    "tree feed",
    "tree feed as jeih",
    "kiare feed",
    "kiare feed as jeih",
    "keead",
    "milley",
    "jeih keead"
]


_ordinal_words = [
    "yn chied",
    "yn nah",
    "yn trass",
    "yn chiarroo",
    "yn wheiggoo",
    "yn çheyoo",
    "yn çhiaghtoo",
    "yn hoghtoo",
    "yn nuyoo",
    "yn jeihoo"
]


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    text_lower = text.lower()
    if text_lower in _num_words:
        return True
    # Check ordinal number
    if text_lower in _ordinal_words:
        return True
    return False


LEX_ATTRS = {LIKE_NUM: like_num}
