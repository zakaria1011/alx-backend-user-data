#!/usr/bin/env python3
""" filter logger"""
import re
from typing import List


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
