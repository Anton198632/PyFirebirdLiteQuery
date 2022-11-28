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


def execute_non_query(sql: str, parameters: dict = None) -> str:
    if parameters is None:
        return FirebirdLiteQuery.Executor.ExecuteNonQuery(sql)
    else:
        parameters_dict = FirebirdLiteQuery.Executor.CreateParameters()
        for key in parameters:
            parameters_dict.Add(key, parameters.get(key))
        return FirebirdLiteQuery.Executor.ExecuteNonQuery(sql, parameters_dict)

