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
pip install moon-logger
```

## Usage

### Initializing Moon

```python
from moon_logger import Moon, LogLevel

moon = Moon(
    name='my_logger',
    log_file='moon.log',
    stream_handler=True,
    file_handler=True,
    disabled=False,
    stream_level=LogLevel.DEBUG,
    file_level=LogLevel.DEBUG
)```

