import string_sum


def test_from_readme():
    assert string_sum.sum_as_string(5, 20) == "25"


def test_42():
    assert string_sum.sum_as_string(21, 21) == "42"
