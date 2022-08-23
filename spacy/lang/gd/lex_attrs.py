from ...attrs import LIKE_NUM


_num_words = [
    "aon",
    "dhà",
    "trì",
    "ceithir",
    "còig",
    "sia",
    "seachd",
    "ochd",
    "naoi",
    "deich",
    "h-aon deug",
    "dhà dheug",
    "trì deug",
    "ceithir deug",
    "còig deug",
    "sia deug",
    "seachd deug",
    "ochd deug",
    "naoi deug",
    "fichead",
    "trìthead",
    "ceathrad",
    "caogad",
    "seasgad",
    "seachdad",
    "ochdad",
    "naochad",
    "ceud",
    "mile",
    "millean",
    "billean",
]


_ordinal_words = [
    "a chiad",
    "an dàrna",
    "an treas",
    "an ceathramh",
    "an còigeamh",
    "an siathamh",
    "an seachdamh",
    "an t-ochdamh",
    "an naoitheamh",
    "an deaicheamh",
    "billeanamh",
    "ceathramh",
    "ceud",
    "ceudamh",
    "ciad",
    "còigeamh",
    "dàrna",
    "deicheamh",
    "ficheadamh",
    "mìleamh",
    "milleanamh",
    "naodhamh",
    "naoidheamh",
    "naoitheamh",
    "ochdamh",
    "seachdamh",
    "siathamh",
    "treas",
    "treasamh",
    "trìtheamh",
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
