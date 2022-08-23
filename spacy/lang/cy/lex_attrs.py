from ...attrs import LIKE_NUM


_num_words = [
    "un",
    "dau",
    "tri",
    "pedwar",
    "pump",
    "chwech",
    "saith",
    "wyth",
    "naw",
    "deg",
    "undeg un",
    "undeg dau",
    "undeg tri",
    "undeg pedwar",
    "undeg pump",
    "undeg chwech",
    "undeg saith",
    "undeg wyth",
    "undeg naw",
    "dauddeg",
    "trideg",
    "pedwardeg",
    "pumdeg",
    "chwedeg",
    "saithdeg",
    "wythdeg",
    "nawdeg",
    "cant",
    "mil",
    "miliwn",
    "biliwn",
]


_ordinal_words = [
    "gyntaf",
    "ail",
    "trydydd",
    "pedwerydd",
    "pumed",
    "chweched",
    "seithfed",
    "wythfed",
    "nawfed",
    "degfed",
    "unfed ar ddeg",
    "deuddegfed",
    "drydedd ar ddeg",
    "ddeg",
    "pymthegfed",
    "ar bymtheg",
    "ail ar bymtheg",
    "deunawfed",
    "bedwaredd ganrif ar bymtheg",
    "ugeinfed",
    "unwaith y",
    "ddwywaith",
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
