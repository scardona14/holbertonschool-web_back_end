#!/usr/bin/env python3
"""
Personal date module
"""
import re
import logging
import os import environ
import mysql.connector
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(rf"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """
    Returns a logging object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("{'user_data': %(message)s}")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to the database
    """
    connector = mysql.connector.connect(
        user=environ.get('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=environ.get('PERSONAL_DATA_DB_PASSWORD', ''),
        host=environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=environ.get('PERSONAL_DATA_DB_NAME')
    )
    return connector


class RedactingFormatter(logging.Formatter):
    """
    Redacting formatter class
    """
    REDACTION = '***'
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ';'


def __init__(self, fields: List[str]):
    """
    Constructor
    """
    super(RedactingFormatter, self).__init__(self.FORMAT)
    self.fields = fields


def format(self, record: logging.LogRecord) -> str:
    """
    Filters values in incoming log records using filter_datum
    """
    record.msg = filter_datum(self.fields, self.REDACTION,
                record.getMessage(), self.SEPARATOR)
    return super(RedactingFormatter, self).format(record)


def main():
    """
    Main function
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    field_names = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        message = '; '.join(f'{field_names[i]}={str(row[i])}'
                            for i in range(len(row)))
        logger.info(message)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
