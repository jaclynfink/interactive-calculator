# Interactive Calculator

Command-line interactive calculator with unit tests.

Features
- Addition, subtraction, multiplication, division
- Input parsing that returns an integer when the value is a whole number and a float otherwise
- Pytest testing covering calculations and parsing

Setup
- Python 3.8 or newer
- `pytest` for running tests

Usage

1. Run the interactive calculator:

```bash
python main.py
```

2. Run the tests:

```bash
pytest -q
```

Files
- `main.py`: main program and helper functions (`get_number`, `parse_number`, `calculate`, `main`)
- `test_main.py`: pytest tests for `calculate` and `parse_number`

Examples
- `calculate("+", 3, 3) -> 6`
- `calculate("/", 5, 2) -> 2.5`
- `parse_number("5.0") -> 5`
