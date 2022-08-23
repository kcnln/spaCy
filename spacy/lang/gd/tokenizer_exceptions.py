from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...symbols import ORTH, NORM
from ...util import update_exc

TOKENIZER_EXCEPTIONS = {
    "'s": [{ORTH: "'s", NORM: "is"}],
    "don": [{ORTH: "do"},{ORTH: "n", NORM: "an"}],
    "fon": [{ORTH: "fo"},{ORTH: "n", NORM: "an"}],
}