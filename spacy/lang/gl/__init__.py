from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS
from .syntax_iterators import SYNTAX_ITERATORS
from .punctuation import TOKENIZER_INFIXES, TOKENIZER_PREFIXES
from ...language import Language, BaseDefaults


class GalicianDefaults(BaseDefaults):
    tokenizer_exceptions = TOKENIZER_EXCEPTIONS
    infixes = TOKENIZER_INFIXES
    prefixes = TOKENIZER_PREFIXES
    lex_attr_getters = LEX_ATTRS
    syntax_iterators = SYNTAX_ITERATORS
    stop_words = STOP_WORDS


class Galician(Language):
    lang = "gl"
    Defaults = GalicianDefaults


__all__ = ["Galician"]
