#!/usr/bin/env python3
"""
This function returns a long message Obfiscated
"""


from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """[Filter_datum takes in a list of strings
        that have PII That needs to be obfiscated]
    """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message
