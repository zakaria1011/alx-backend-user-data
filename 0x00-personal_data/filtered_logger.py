#!/usr/bin/env python3
""" filter logger"""
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscate specified fields in a log message.
    """
    pattern = r"({})=([^{}]*)".format(
        '|'.join(re.escape(field) for field in fields), re.escape(separator)
    )
    return re.sub(pattern, lambda m: "{}={}".format(m.group(1), redaction),
                  message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize RedactingFormatter.

        Args:
            fields (List[str]): A list of field names to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record.

        Args:
            record (logging.LogRecord): The LogRecord to be formatted.

        Returns:
            str: The formatted log message.
        """
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)
