from ...attrs import LIKE_NUM


_num_words = [
    "un",
    "dos",
    "tres",
    "trés",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    "ocho",
    "nueve",
    "diez",
    "once",
    "doce",
    "trece",
    "catorce",
    "quince",
    "dieciséis",
    "diecisiete",
    "dieciocho",
    "diecinueve",
    "venti",
    "ventiún",
    "ventidós",
    "ventitrés",
    "venticuatro",
    "venticinco",
    "ventiséis",
    "ventisiete",
    "ventiocho",
    "ventinueve",
    "trenta",
    "cuaranta",
    "cincuenta",
    "sesenta",
    "setanta",
    "ochenta",
    "noventa",
    "cien",
    "mil",
    "cincocientes",
    "cincocientos",
    "cuatrocientes",
    "cuatrocientos",
    "doscientes",
    "doscientos",
    "millones",
    "millón",
    "ochocientes",
    "ochocientos",
    "quinientes",
    "quinientos",
    "seiscientes",
    "seiscientos",
    "selce",
    "setecientes",
    "setecientos",
    "seyes",
    "trescientes",
    "trescientos",
    "trelce",
    "una",
    "unu",
    "cero",
]


_ordinal_words = [
    "primeru",
    "segundu",
    "terceru",
    "cuartu",
    "cinco",
    "sestu",
    "séptimu",
    "octavu",
    "novenu",
    "décimu",
    "decimoprimeru",
    "decimosegundu",
    "decimoterceru",
    "decimocuartu",
    "decimoquintu",
    "decimosestu",
    "decimoséptimu",
    "decimoctavu",
    "decimonovenu",
    "ventésimu",
    "trentésimu",
]


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "").replace("º", "").replace("ª", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    if text.lower() in _num_words:
        return True
    if text.lower() in _ordinal_words:
        return True
    return False


LEX_ATTRS = {LIKE_NUM: like_num}
