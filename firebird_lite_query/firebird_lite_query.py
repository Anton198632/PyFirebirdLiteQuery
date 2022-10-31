import os

import clr
current_path = os.path.dirname(os.path.abspath(__file__))
clr.AddReference(f'{current_path}//FirebirdLiteQuery.dll')
import FirebirdLiteQuery


def connect(server, db_path, username = None, pasword = None):
    FirebirdLiteQuery.Connector.Connect(server, db_path, username, pasword)


def execute_reader(sql: str) -> str:
    for response in FirebirdLiteQuery.Executor.ExecuteReader(sql):
        yield response


def execute_non_query(sql: str) -> str:
    return FirebirdLiteQuery.Executor.ExecuteNonQuery(sql)
