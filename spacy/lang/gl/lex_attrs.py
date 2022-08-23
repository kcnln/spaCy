from ...attrs import LIKE_NUM


_num_words = [
    "un",
    "dous",
    "tres",
    "catro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "once",
    "doce",
    "trece",
    "catorce",
    "quince",
    "dezaseis",
    "dezasete",
    "dezaoito",
    "dezanove",
    "vinte",
    "cen",
    "mil",
    "millón",
]


_ordinal_words = [
    "primeiro",
    "segundo",
    "terceiro",
    "cuarto",
    "quinto",
    "sexto",
    "sétimo",
    "oitavo",
    "noveno",
    "décimo",
    "décimo primeiro",
    "duodécimo",
    "décimo terceiro",
    "décimo cuarto",
    "décimo quinto",
    "décimo sexto",
    "décimo sétimo",
    "décimo oitavo",
    "décimo noveno",
    "vixésimo",
    "unha vez",
    "dúas veces",
    "millón",
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
