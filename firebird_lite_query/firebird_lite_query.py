import os
import threading

import clr
current_path = os.path.dirname(os.path.abspath(__file__))
clr.AddReference(f'{current_path}//FirebirdLiteQuery.dll')
import FirebirdLiteQuery

lock = threading.Lock()

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


def lock_execute(function, sql, parameters: dict = None):
    m_type = function.__name__
    result = None
    with lock:
        result = []
        if m_type == 'execute_reader':
            for r in function(sql):
                result.append(r)
        elif m_type == 'execute_non_query':
            result = function(sql, parameters)
    return result

