from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...symbols import ORTH, NORM
from ...util import update_exc

TOKENIZER_EXCEPTIONS = {
    "sgen": [{ORTH: "s", NORM: "oes"},{ORTH: "gen"}],
    "i'r": [{ORTH: "i"},{ORTH: "'r", NORM: "yr"}],
    "o'r": [{ORTH: "o"},{ORTH: "'r", NORM: "yr"}],
    "mae'r": [{ORTH: "mae"},{ORTH: "'r", NORM: "yr"}],
    "cadw'r": [{ORTH: "cadw"},{ORTH: "'r", NORM: "yr"}]
}