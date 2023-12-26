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
moon.archive()
```

### Custom Formatting:

```python
moon.set_log_format("[{name}] - [{levelname}]: {message}")
```

**Formats built into moon logger**:
- `CLang`
- `Json`
- `Csv`
- `Table`
- `Html`
- `Xml`
- `Markdown`
- `Yaml`
- `Syslog`
- `JsonIndented`
- `Logstash`
- `ShortJson`
- `ColoredConsole`
- `DelimiterSeparatedJson`
- `Traceback`
- `TracebackV2`

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
```python
from moon.logger import Moon, logging

# Define a custom log format string
custom_log_format = logging.Formatter(
    "[{levelname}] [{asctime}] - {message}",
    style="{"
)

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
```

- **Built-in log format**:

```python
from moon.logger import Moon
from moon.formats import Formats 


# Initialize the Moon logger with the built-in log format
logger = Moon(
    name=__name__,
    file_handler=False,
    stream_format=Formats.CLang() # You can choose any built-in log format
).base_logger()

# Log a message using the built-in log format
logger.info(
    msg="Custom log message"
)
```

- **Archiving a file**:

```python
from moon.logger import Moon
from moon.formats import Formats 

# Initialize the Moon logger with a file handler and JsonIndented format
moon = Moon(
    name=__name__,
    log_file="moon.json",
    file_handler=True,
    file_format=Formats.JsonIndented()
)

# Get the base logger from the Moon logger instance
logger = moon.base_logger()

# Log a custom message with an informational level
logger.info(
    msg="Custom log message"
)

# Archive log file
moon.archive()
```

- **Changing Log Format Dynamically**:
```python
from moon.logger import Moon

# Create an instance of Moon Logger with a file handler
logger = Moon(name="dynamic_format_logger", file_handler=True)

# Log an error message
logger.error(msg="An error occurred.")

# Change the log format
logger.edit_format("[{levelname}] {message} ({asctime})")

# Log another message with the updated format
logger.info(msg="Updated log format.")
```

- **Removing All Formatters**:
```python
from moon.logger import Moon

# Create an instance of Moon Logger with a file handler
logger = Moon(name="remove_all_formatters_logger", file_handler=True)

# Add two formatters
logger.add_formatter(Moon.formats.CLang())
logger.add_formatter(Moon.formats.JsonIndented())

# Remove all formatters
logger.del_formatters()

# Log a message with DEBUG level
logger.debug(msg="Logging after removing formatters.")
```

- **Removing a Specific Formatter**:
```python
from moon.logger import Moon
from moon.formats import Formats

# Create an instance of Moon Logger with a file handler
logger = Moon(name="remove_formatter_logger", file_handler=True)

# Add two formatters
formatter1 = Formats.Table()
formatter2 = Formats.Json()

logger.add_formatter(formatter1)
logger.add_formatter(formatter2)

# Remove one of the formatters
logger.del_formatter(formatter1)

# Log a message with INFO level
logger.info(msg="Logging after removing one formatter.")
```

- **Conditional Logging Based on Environment**:
```python
from moon.logger import Moon
from moon.formats import Formats
import os

# Create an instance of Moon Logger with conditional file handler
enable_file_logging = os.environ.get("ENABLE_FILE_LOGGING", "False").lower() == "true"
logger = Moon(
    name="conditional_logger",
    file_handler=enable_file_logging,
    file_format=Formats.JsonIndented() if enable_file_logging else None
).base_logger()

# Log a message with INFO level
logger.info(msg="Conditional log message.")
```
