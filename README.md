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
git clone https://github.com/reslaid/moon-logger.git
```

## Usage

### Initializing Moon

```python
from moon.logger import Moon
from moon.formats import Formats
from moon._types import LogLevel

moon = Moon(
    name='my_logger',
    log_file='moon.log',
    stream_handler=True,
    file_handler=True,
    disabled=False,
    stream_level=LogLevel.DEBUG,
    file_level=LogLevel.DEBUG
)
```

