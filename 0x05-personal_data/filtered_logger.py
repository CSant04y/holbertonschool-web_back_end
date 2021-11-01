#!/usr/bin/env python3
"""
This function returns a long message Obfiscated
"""


from typing import List
import re
import logging
from mysql.connector import connection 
from os import environ


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''This Method filters the fields in fields'''
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """[Filter_datum takes in a list of strings
        that have PII That needs to be obfiscated]
    """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_db() -> connection.MySQLConnection:
    """[Connects to Db]

    Returns:
        connection.MySQLConnection: [connector to db]
    """
    username = environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    password = environ.get('PERSONAL_DATA_DB_PASSWORD', "")
    db_host = environ.get('PERSONAL_DATA_DB_HOST', "localhost")
    db_name = environ.get('PERSONAL_DATA_DB_NAME')

    connector = connection.MySQLConnection(host=db_host, database=db_name, user=username, password=password)
    return connector


def get_logger() -> logging.Logger:
    """[This logs user Data]

    Returns:
        logging.Logger: [description]
    """
    '''Create Object first'''
    logger = logging.getLogger('user_data')
    '''Set the level of the object to logging.INFO'''
    logger.setLevel(logging.INFO)
    logger.propagate = False

    streamhandler = logging.StreamHandler()
    streamhandler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(streamhandler)
    return logger
