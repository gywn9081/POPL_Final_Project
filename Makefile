
#	Henry Bloch (I got lazy!)

GRAMMAR_DIR ?= src/grammars
BUILD_DIR ?= build
TEST_DIR ?= tests
CURRENT_WORKING_DIR := $(CURDIR)


GRAMMAR_FILES := $(wildcard $(GRAMMAR_DIR)/*.g4)

# Find the test files there should not be many since there is only one per deliverable
TEST_FILES := $(wildcard $(TEST_DIR)/*.py)


# Stamp files mark successful ANTLR4 generation
STAMP_FILES := $(patsubst $(GRAMMAR_DIR)/%.g4,$(BUILD_DIR)/%.stamp,$(GRAMMAR_FILES))


# Default target
all: $(STAMP_FILES)

# Generate Python outputs
$(BUILD_DIR)/%.stamp: $(GRAMMAR_DIR)/%.g4 $(BUILD_DIR)/__init__.py | $(BUILD_DIR)
	@echo "Generating ANTLR4 Python files for $<"
	cd $(GRAMMAR_DIR) && antlr4 -Dlanguage=Python3 -o $(CURRENT_WORKING_DIR)/$(BUILD_DIR) $(notdir $<)
	@touch $@


# Ensure build dir exists
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# Make __init__.py file for Python imports
$(BUILD_DIR)/__init__.py: | $(BUILD_DIR)
	touch $(BUILD_DIR)/__init__.py


# Test all custom built tests in the tests dir
tests: all
	@if [ -z "$(TEST_FILES)" ]; then \
		echo "Error: no test files found."; \
		exit 1; \
	else \
		echo "Running tests: $(TEST_FILES)"; \
		pytest $(TEST_FILES); \
	fi

clean:
	rm -rf $(BUILD_DIR)

# Show which dir we are deleting
test-clean:
	echo $(BUILD_DIR)