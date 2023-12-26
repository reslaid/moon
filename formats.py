import logging
import datetime
import traceback
import json
import yaml
from prettytable import PrettyTable
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom


class Formats:
    class CLang(logging.Formatter):
        def format(self, record):
            levelname = record.levelname
            filename = record.filename
            lineno = record.lineno
            message = record.getMessage()

            if record.levelno == logging.DEBUG:
                levelname = 'D'
            elif record.levelno == logging.INFO:
                levelname = 'I'
            elif record.levelno == logging.WARNING:
                levelname = 'W'
            elif record.levelno == logging.ERROR:
                levelname = 'E'
            elif record.levelno == logging.CRITICAL:
                levelname = 'F'

            return f"{filename}:{lineno}: {levelname}: {message}"

    class Json(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }
            return json.dumps(log_data)

    class Csv(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }
            return ','.join(log_data.values())

    class Table(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }

            table = PrettyTable()
            table.field_names = log_data.keys()
            table.add_row(log_data.values())

            return str(table)

    class Html(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }

            html_log = f"""<p>{
                ', '.join(
                    f'<strong>{k}:</strong> {v}'
                    for k, v in log_data.items()
                    )
                }</p>"""
            return html_log

    class Xml(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }

            root = Element('log')
            for key, value in log_data.items():
                SubElement(root, key).text = str(value)

            return minidom.parseString(tostring(root)).toprettyxml(indent="  ")

    class Markdown(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }

            markdown_log = '\n'.join(
                [f"**{k}:** {v}" for k, v in log_data.items()]
            )
            return markdown_log

    class Yaml(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }
            return yaml.dump(log_data, default_flow_style=False)

    class Syslog(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }
            return (
                log_data['timestamp']
                + " "
                + log_data['level']
                + " "
                + log_data['message']
            )

    class JsonIndented(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }
            return json.dumps(log_data, indent=2)

    class Logstash(logging.Formatter):
        def format(self, record):
            log_data = {
                '@timestamp': datetime.datetime.utcnow().isoformat(),
                'loglevel': record.levelname,
                'message': record.getMessage(),
                'logger_name': record.name,
                'path': record.pathname,
                'line_number': record.lineno
            }
            return json.dumps(log_data)

    class ShortJson(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }
            return json.dumps(log_data, separators=(',', ':'))

    class ColoredConsole(logging.Formatter):
        COLORS = {
            'INFO': '\033[92m',
            'WARNING': '\033[93m',
            'ERROR': '\033[91m'
        }
        RESET = '\033[0m'

        def format(self, record):
            log_message = super().format(record)
            return (
                f"{self.COLORS.get(record.levelname, '')}"
                f"{log_message}"
                f"{self.RESET}"
            )

    class DelimiterSeparatedJson(logging.Formatter):
        def format(self, record):
            log_data = {
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'level': record.levelname,
                'message': record.getMessage()
            }
            return json.dumps(log_data, separators=(',', ':'))
        
    class Traceback(logging.Formatter):
        def __init__(self, fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt=None, context=3):
            super().__init__(fmt, datefmt)
            self.context = context

        def format(self, record):
            formatted_record = super().format(record)
            record.message = f"{record.levelname}: {record.getMessage()}" 
            return formatted_record
        
    class TracebackV2(logging.Formatter):
        def __init__(self, fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt=None, context=3):
            super().__init__(fmt, datefmt)
            self.context = context

        def format(self, record):
            formatted_record = super().format(record)
            record.message = f"{record.levelname}: {record.getMessage()}"

            frames = traceback.extract_tb(record.stack_info)
            frames = frames[-self.context:]

            frames_str = ""
            frames_str += f"\n    at {record.filename}:{record.lineno} in {record.funcName}\n"

            formatted_record += frames_str
            return formatted_record
