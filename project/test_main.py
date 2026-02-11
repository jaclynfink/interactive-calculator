import pytest
from unittest.mock import patch
import runpy
import sys
import os

from main import calculate, parse_number, get_number, main


# --------------------------
# Parameterized calculation tests
# --------------------------

@pytest.mark.parametrize(
    "operation,num1,num2,expected",
    [
        ("+", 3, 3, 6),
        ("-", 10, 3, 7),
        ("*", 10, 3, 30),
        ("/", 6, 3, 2),
        ("/", 5, 2, 2.5),
        ("-", 5.0, 2.5, 2.5),
        ("+", 9.0, 1, 10),
        ("+", 9.0, 1.0, 10.0),
        ("+", -1, 1, 0),
        ("*", 0, 10, 0),
    ],
)
def test_calculate_valid(operation, num1, num2, expected):
    assert calculate(operation, num1, num2) == expected


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("/", 20, 0)


def test_invalid_operation():
    with pytest.raises(ValueError):
        calculate("%", 5, 2)


# --------------------------
# Parameterized parse_number tests
# --------------------------

@pytest.mark.parametrize(
    "input_value,expected",
    [
        ("5", 5),
        ("5.0", 5),
        ("5.5", 5.5),
        ("-3", -3),
        ("-3.2", -3.2),
    ],
)
def test_parse_number_valid(input_value, expected):
    assert parse_number(input_value) == expected


def test_parse_number_invalid():
    with pytest.raises(ValueError):
        parse_number("abc")


# --------------------------
# get_number tests
# --------------------------

@patch("builtins.input")
def test_get_number_int(mock_input):
    mock_input.return_value = "5"
    assert get_number("Enter number: ") == 5


@patch("builtins.input")
def test_get_number_float(mock_input):
    mock_input.return_value = "5.5"
    assert get_number("Enter number: ") == 5.5


@patch("builtins.input")
def test_get_number_with_whitespace(mock_input):
    mock_input.return_value = "  10  "
    assert get_number("Enter number: ") == 10


@patch("builtins.input")
@patch("builtins.print")
def test_get_number_invalid_then_valid(mock_print, mock_input):
    mock_input.side_effect = ["abc", "5"]
    result = get_number("Enter number: ")
    assert result == 5
    mock_print.assert_called_with("ERROR: Invalid number.")


# --------------------------
# main function tests
# --------------------------

@patch("builtins.input")
@patch("builtins.print")
def test_main_quit(mock_print, mock_input):
    mock_input.return_value = "q"
    main()
    assert any("Interactive Calculator" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("builtins.print")
def test_main_addition(mock_print, mock_input):
    mock_input.side_effect = ["+", "3", "3", "q"]
    main()
    assert any("6" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("builtins.print")
def test_main_division(mock_print, mock_input):
    mock_input.side_effect = ["/", "5", "2", "q"]
    main()
    assert any("2.5" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("builtins.print")
def test_main_subtraction(mock_print, mock_input):
    mock_input.side_effect = ["-", "10", "3", "q"]
    main()
    assert any("7" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("builtins.print")
def test_main_multiplication(mock_print, mock_input):
    mock_input.side_effect = ["*", "4", "5", "q"]
    main()
    assert any("20" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("builtins.print")
def test_main_invalid_operation(mock_print, mock_input):
    mock_input.side_effect = ["%", "q"]
    main()
    assert any("Invalid operation" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("builtins.print")
def test_main_division_by_zero(mock_print, mock_input):
    mock_input.side_effect = ["/", "10", "0", "q"]
    main()
    assert any("Cannot divide by zero" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("main.calculate", side_effect=RuntimeError("Unexpected error"))
@patch("builtins.print")
def test_main_unexpected_error(mock_print, mock_calculate, mock_input):
    mock_input.side_effect = ["+", "1", "1", "q"]
    main()
    assert any("ERROR" in str(call) for call in mock_print.call_args_list)


# --------------------------
# Script execution test (covers if __name__ == "__main__":)
# --------------------------

@patch("builtins.input")
@patch("builtins.print")
def test_main_script_execution(mock_print, mock_input):
    mock_input.return_value = "q"
    test_dir = os.path.dirname(os.path.abspath(__file__))
    main_py = os.path.join(test_dir, "main.py")
    runpy.run_path(main_py, run_name="__main__")
    assert any("Interactive Calculator" in str(call) for call in mock_print.call_args_list)
