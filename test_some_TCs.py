from program_code import number_of_first_primary_numer_from_fib
import pytest

@pytest.mark.parametrize('n, lista', [
    (0, []),
    (1, [2]),
    (2, [2,3]),
    (3, [2,3,5]),
    (4, [2,3,5,13])
])
def test_returning_list_of_prime_number(n, lista):
    assert number_of_first_primary_numer_from_fib(n) == lista, "Program return wrong list of prime number"

def test_compare_the_same_value_provided():
    list1 = number_of_first_primary_numer_from_fib(4)
    list2 = number_of_first_primary_numer_from_fib(4)
    assert list1 == list2, "Both lists are not the same. Program has some problem"

def test_provided_parameter_is_lower_than_0_exception():
    with pytest.raises(Exception):
        assert number_of_first_primary_numer_from_fib(-1)

def test_provided_parameter_is_not_integer_exception():
    with pytest.raises(Exception):
        assert number_of_first_primary_numer_from_fib("4")

def test_not_provided_any_parameter_exception():
    with pytest.raises(TypeError):
        assert number_of_first_primary_numer_from_fib()