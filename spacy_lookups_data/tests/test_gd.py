import pytest

@pytest.mark.parametrize(
    "string,lemma",
    [
        ("abaidean", "abaid"),
        ("ghobhlaiche", "gobhlach"),
        ("spàrramaid", "spàrr"),
    ],
)
def test_gd_lemmatizer_lookup_assigns(gd_lookup_nlp, string, lemma):
    tokens = gd_lookup_nlp(string)
    assert tokens[0].lemma_ == lemma

