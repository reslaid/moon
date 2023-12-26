Moon Logger

The Moon Logger is a Python logging utility with customizable features for handling both stream and file logging.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Initializing Moon](#initializing-moon)
  - [Log Levels](#log-levels)
  - [Handlers](#handlers)
  - [Archiving Logs](#archiving-logs)
  - [Custom Formatting](#custom-formatting)
  - [Logger Methods](#logger-methods)
- [Examples](#examples)

## Installation

**Install the Moon Logger using git**:

```bash
git clone https://github.com/reslaid/moon.git
```

## Usage

### Initializing Moon

```python
from moon.logger import Moon
from moon.formats import Formats
from moon._types import LogLevel

moon = Moon(
    name=__name__,
    log_file='moon.json',
    stream_handler=True,
    file_handler=True,
    disabled=False,
    stream_level=LogLevel.DEBUG,
    file_level=LogLevel.DEBUG,
    stream_format=Formats.CLang(),
    file_format=Formats.JsonIndented()
)
```

### Log Levels

**The Moon Logger supports the following log levels**:

- `LogLevel.DEBUG`
- `LogLevel.INFO`
- `LogLevel.WARNING`
- `LogLevel.ERROR`
- `LogLevel.CRITICAL`

### Handlers

-  **Adding Stream Handler**:
  
  ```python
  moon.add_stream_handler()
  ```
  
-  **Adding File Handler**:
  
  ```python
  moon.add_file_handler()
  ```

### Archiving Logs:

```python
await moon.archive()
```

### Custom Formatting:

```python
moon.set_log_format("[{name}] - [{levelname}]: {message}")
```

### Logger Methods:

- `moon.set_formatter(formatter)`: Set a custom formatter for the logger.
- `moon.add_formatter(formatter)`: Add a formatter to the logger.
- `moon.del_formatters()`: Remove all formatters from the logger.
- `moon.del_formatter(formatter)`: Remove a specific formatter from the logger.
- `moon.edit_format(new_log_format)`: Edit the log format, ensuring required placeholders are present.
- `moon.reset_format()`: Reset the log format to the default.
- `moon.base_logger()`: Getting the base logger.

## Examples

- **Logging Message**:

```python
# Import the Moon logger and Formats module
from moon.logger import Moon
from moon.formats import Formats

# Initialize the Moon logger
logger = Moon(
    name=__name__,
    file_handler=False,  # Disable file handler
    stream_format=Formats.CLang()  # Use CLang format for stream handler
).base_logger()

# Log a debug message
logger.debug(
    msg="message"
)

# Log an informational message
logger.info(
    msg="message"
)

# Log a warning message
logger.warning(
    msg="message"
)

# Log an error message
logger.error(
    msg="message"
)

# Log a critical message
logger.critical(
    msg="message"
)

# Log a fatal message
logger.fatal(
    msg="message"
)
```

- **Custom log format**:
- from moon.logger import Moon

# Define a custom log format string
custom_log_format = "[{levelname}] [{asctime}] - {message}"

# Initialize the Moon logger with the custom log format
logger = Moon(
    name=__name__,
    file_handler=False,
    stream_format=custom_log_format
).base_logger()

# Log a message using the custom format
logger.info(
    msg="Custom log message"
)
