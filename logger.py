from ._types import LogLevel

import logging
import os
import inspect
import zipfile
import asyncio
import aiofiles


class Moon:
    def __init__(
        self,
        name: str = __name__,
        log_file: str = 'moon.log',
        stream_handler: bool = True,
        file_handler: bool = True,
        disabled: bool = False,
        stream_level: int = LogLevel.DEBUG,
        file_level: int = LogLevel.DEBUG,
        stream_format: logging.Formatter | None = None,
        file_format: logging.Formatter | None = None
    ):
        self._name = name
        self._log_file = log_file

        self._file_level = file_level
        self._stream_level = stream_level

        self._logger = logging.getLogger(self._name)
        self._logger.setLevel(level=self._stream_level)
        self._logger.disabled = disabled

        self._default_formatter = logging.Formatter(
            "[{name}] [{asctime}] - [{levelname}]: {message}",
            style='{'
        )

        self._stream_format = stream_format or self._default_formatter
        self._file_format = file_format or self._default_formatter

        self.add_stream_handler() if stream_handler else None
        self.add_file_handler() if file_handler else None

    def add_stream_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self._stream_level)
        stream_handler.setFormatter(self._stream_format)
        self._logger.addHandler(stream_handler)

    def add_file_handler(self, level=logging.DEBUG):
        file_handler = logging.FileHandler(self._log_file)
        file_handler.setLevel(self._file_level)
        file_handler.setFormatter(self._file_format)
        self._logger.addHandler(file_handler)

    async def archive(self):
        archive_path = f"{self._log_file}.zip"

        with open(self._log_file, 'rb') as file:
           self._zip_log(archive_path, file)

        os.remove(self._log_file)

        return self

    def _zip_log(self, archive_path, file):
        with open(archive_path, 'wb') as zipf:
            with zipfile.ZipFile(zipf, 'w') as zip_file:
                zip_file.writestr(
                    os.path.basename(self._log_file),
                    file.read()
                )

    def set_log_format(self, log_format):
        self._default_formatter = logging.Formatter(log_format, style='{')

        for handler in self._logger.handlers:
            handler.setFormatter(self._default_formatter)

    def add_formatter(self, formatter):
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def del_formatters(self):
        for handler in self._logger.handlers:
            self._logger.removeHandler(handler)

    def del_formatter(self, formatter):
        if formatter in self._logger.handlers:
            self._logger.removeHandler(formatter)

    def set_formatter(self, formatter):
        self._del_formatters()
        self._add_formatter(formatter=formatter)

    def edit_format(self, new_log_format: str) -> None:
        required_placeholders = ["{message}"]
        if all(ph in new_log_format for ph in required_placeholders):
            self.set_log_format(new_log_format)
        else:
            self._logger.error("Invalid log format")

    def reset_format(self) -> None:
        self.set_log_format(self._default_formatter)

    def base_logger(self) -> logging.Logger:
        return self._logger
