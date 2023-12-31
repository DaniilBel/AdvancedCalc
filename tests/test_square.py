from main import expression_check


def test_valid_expression():
    assert expression_check("3 + 2 * (4 - 1)") == (True,)
    assert expression_check("(5.5 / 2) * -1") == (True,)
    assert expression_check("10^2 + 5%3") == (True,)


def test_invalid_symbols():
    assert expression_check("3 + 2 * (4 @ 1)") == (False, "There are unsupported symbols in request!")
    assert expression_check("(5.5 / 2) * #1") == (False, "There are unsupported symbols in request!")


def test_invalid_combinations():
    assert expression_check("3 + 2 *-- (4 - 1)") == (False, "There are unsupported combinations of symbols in request!")
    assert expression_check("(5.5 / 2) +++ -1") == (False, "There are unsupported combinations of symbols in request!")


def test_invalid_expression():
    assert expression_check("3 + 2 * (4 - 1a)") == (False, "There are unsupported symbols in request!")


def test_valid_expression_with_special_characters():
    assert expression_check("3.14159 * 2^(-2) % 7") == (True,)


def test_valid_expression_with_double_minus():
    assert expression_check("5 * --3") == (False, "There are unsupported combinations of symbols in request!")


def test_valid_expression_with_triple_plus():
    assert expression_check("4 +++ 2") == (False, "There are unsupported combinations of symbols in request!")


def test_valid_expression_with_double_braces():
    assert expression_check("()()") == (False, "There are unsupported combinations of symbols in request!")


def test_valid_expression_with_inverted_double_braces():
    assert expression_check(")(") == (False, "There are unsupported combinations of symbols in request!")


def test_valid_expression_with_slashes():
    assert expression_check("////") == (False, "There are unsupported combinations of symbols in request!")
