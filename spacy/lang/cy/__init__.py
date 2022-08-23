from typing import Optional, Callable

from thinc.api import Model

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS
from .punctuation import TOKENIZER_INFIXES
from .lemmatizer import WelshLemmatizer
from ...language import Language, BaseDefaults


class WelshDefaults(BaseDefaults):
    tokenizer_exceptions = TOKENIZER_EXCEPTIONS
    infixes = TOKENIZER_INFIXES
    lex_attr_getters = LEX_ATTRS
    stop_words = STOP_WORDS


class Welsh(Language):
    lang = "cy"
    Defaults = WelshDefaults


@Welsh.factory(
    "lemmatizer",
    assigns=["token.lemma"],
    default_config={
        "model": None,
        "mode": "rule",
        "overwrite": False,
        "scorer": {"@scorers": "spacy.lemmatizer_scorer.v1"},
    },
    default_score_weights={"lemma_acc": 1.0},
)
def make_lemmatizer(
    nlp: Language,
    model: Optional[Model],
    name: str,
    mode: str,
    overwrite: bool,
    scorer: Optional[Callable],
):
    return WelshLemmatizer(
        nlp.vocab, model, name, mode=mode, overwrite=overwrite, scorer=scorer
    )


__all__ = ["Welsh"]
