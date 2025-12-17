# Package Sorting System

A Python package classification system that sorts packages into three stacks: STANDARD, SPECIAL, and REJECTED based on their dimensions and weight.

## Classification Rules

### BULKY Package
A package is considered bulky if:
- Any dimension (width, height, or length) >= 150 cm
- Volume >= 1,000,000 cm³

### HEAVY Package
A package is considered heavy if:
- Mass >= 20 kg

### Stack Assignment
- STANDARD: Neither bulky nor heavy
- SPECIAL: Either bulky or heavy (but not both)
- REJECTED: Both bulky and heavy

## Usage

### Running the main program

```bash
python3 main.py
```

### Running tests

```bash
make test
```

### Running tests with verbose output

```bash
make test-verbose
```

### Cleaning up cache files

```bash
make clean
```

## Function API

```python
from main import sort

result = sort(width, height, length, mass)
```

**Parameters:**
- width (float): Package width in cm
- height (float): Package height in cm
- length (float): Package length in cm
- mass (float): Package mass in kg

**Returns:**
- str: 'standard', 'special', or 'rejected'

## Example

```python
sort(10, 150, 10, 21)  # Returns 'rejected' (bulky by height and heavy)
sort(100, 100, 100, 10)  # Returns 'special' (bulky by volume)
sort(10, 10, 10, 25)  # Returns 'special' (heavy only)
sort(50, 50, 50, 15)  # Returns 'standard' (normal package)
```

## Project Structure

```
.
├── main.py           # Main sorting function
├── enums.py          # Stack and PackageType enums
├── tests/            # Unit tests
│   └── test_sort.py
└── Makefile          # Test automation
```
