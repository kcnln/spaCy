import pytest

@pytest.mark.parametrize(
    "string,lemma",
    [
        ("chouyrit", "couyr"),
        ("ngreddanaghyn", "greddaney"),
        ("aachiangleys", "aachiangle"),
    ],
)
def test_gv_lemmatizer_lookup_assigns(gv_lookup_nlp, string, lemma):
    tokens = gv_lookup_nlp(string)
    assert tokens[0].lemma_ == lemma

