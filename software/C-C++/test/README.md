# Unit Tests (test/)

The `test/` directory contains unit tests for the project. Unit tests are automated tests designed to verify the correctness of individual components or units of code in isolation.

## Directory Structure

The `test/` directory is organized as follows:

```
test/
├── test_utility.cpp
└── test_my_class.cpp
```

- **test_utility.cpp**: This file contains unit tests for the utility functions provided by the `my_library`.
- **test_my_class.cpp**: This file contains unit tests for the `MyClass` class provided by the `my_library`.

## Running Tests

To run the unit tests, execute the following command in the project root directory:

`./run_tests.sh`


The `run_tests.sh` script compiles and executes all unit test files in the `test/` directory, generating a test report with the results.

## Additional Information

For more information on unit testing and testing frameworks, refer to the documentation of the specific testing framework used in the project.