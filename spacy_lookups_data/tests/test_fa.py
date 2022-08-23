import pytest

@pytest.mark.parametrize(
    "string,lemma",
    [
        ("مي‌آزمود", "آزمود"),
    ],
)
def test_tizer_lookup_assigns(fa_lookup_nlp, string, lemma):
    tokens = fa_lookup_nlp(string)
    assert tokens[0].lemma_ == lemma

