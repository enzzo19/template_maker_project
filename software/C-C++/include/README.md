# Include Directory

The `include/` directory contains header files (.h or .hpp) that declare interfaces, classes, functions, and constants used by other source files in the project.

## Directory Structure

The `include/` directory is organized as follows:

```
include/
├── my_library/
│ ├── my_class.h
│ └── my_utility.h
└── project_config.h
```


- **my_library/**: This directory contains header files related to the custom library `my_library`.
  - **my_class.h**: Header file declaring the class `MyClass`.
  - **my_utility.h**: Header file declaring utility functions provided by `my_library`.
- **project_config.h**: Header file containing project-wide configuration settings, such as constants, macros, or global variables.

## Usage

Header files in the `include/` directory are included in source files using `#include` directives. For example:

```cpp
#include <my_library/my_class.h>
#include <my_library/my_utility.h>
#include "project_config.h"
```

Ensure that the necessary header files are included in source files to access the functionality provided by the corresponding modules or libraries.