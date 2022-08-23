from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...symbols import ORTH, NORM
from ...util import update_exc

TOKENIZER_EXCEPTIONS = {
    "'sy": [{ORTH: "'s", NORM: "ayns"},{ORTH: "y", NORM: "yn"}],
    "kys": [{ORTH: "kys", NORM: "kanys"}],
    "t'ad": [{ORTH: "t'", NORM: "ta"},{ORTH: "ad"}],
    "t'ee": [{ORTH: "t'", NORM: "ta"},{ORTH: "ee"}],
    "t'eh": [{ORTH: "t'", NORM: "ta"},{ORTH: "eh"}],
    "t'ou": [{ORTH: "t'", NORM: "ta"},{ORTH: "ou", NORM: "oo"}],
    "t'": [{ORTH: "t'", NORM: "ta"}],
    "v'": [{ORTH: "v'", NORM: "va"}],
}