.PHONY: test test-verbose clean help

# Default Python interpreter
PYTHON = python3

# Test directory
TEST_DIR = tests

help:
	@echo "Available commands:"
	@echo "  make test          - Run all unit tests"
	@echo "  make test-verbose  - Run tests with verbose output"
	@echo "  make clean         - Remove Python cache files"
	@echo "  make help          - Show this help message"

test:
	@echo "Running unit tests..."
	@$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "test_*.py"

test-verbose:
	@echo "Running unit tests (verbose mode)..."
	@$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "test_*.py" -v

clean:
	@echo "Cleaning up Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@echo "Clean complete!"
