"""Error classes for PostgreSQL error codes
"""

from psycopg2._psycopg import (  # noqa
    Error, Warning, DataError, DatabaseError, ProgrammingError, IntegrityError,
    InterfaceError, InternalError, NotSupportedError, OperationalError,
    QueryCanceledError, TransactionRollbackError)


_by_sqlstate = {}


class ClassSyntaxErrorOrAccessRuleViolation(Error):
    pass

_by_sqlstate['42'] = ClassSyntaxErrorOrAccessRuleViolation


class UndefinedColumn(ClassSyntaxErrorOrAccessRuleViolation, ProgrammingError):
    pass

_by_sqlstate['42703'] = UndefinedColumn
