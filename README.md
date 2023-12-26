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

## Archiving Logs:

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
