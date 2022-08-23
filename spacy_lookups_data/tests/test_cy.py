import pytest

@pytest.mark.parametrize(
    "string,lemma",
    [
        ("abadaethau", "abadaeth"),
        ("gweithlenni", "gweithlen"),
        ("poblogeiddiff", "poblogeiddio"),
    ],
)
def test_cy_lemmatizer_lookup_assigns(cy_lookup_nlp, string, lemma):
    tokens = cy_lookup_nlp(string)
    assert tokens[0].lemma_ == lemma

