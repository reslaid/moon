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
- [Contributing](#contributing)
- [License](#license)

## Installation

Install the Moon Logger using pip:

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

The Moon Logger supports the following log levels:

- `LogLevel.DEBUG`
- LogLevel.INFO
- LogLevel.WARNING
- LogLevel.ERROR
- LogLevel.CRITICAL

Handlers

Adding Stream Handler

moon.add_stream_handler()

Adding File Handler

moon.add_file_handler()

Archiving Logs

await moon.archive()

