import setuptools


setuptools.setup(
    name='PyFirebirdLiteQuery',
    version='0.0.1',
    author='Anton Rudenko',
    author_email='antonbryansk1986@gmail.com',
    description='The library is a wrapper for api access to the database on the Firebird DBMS platform (Interbase)',
    long_description="The library is a wrapper for api access to the database on the Firebird DBMS platform (Interbase), which returns the query result in JSON format. You just need to specify the path to the database, user access data (optional) and form an SQL query.",
    long_description_content_type="text/markdown",
    url='https://github.com/Anton198632/PyFirebirdLiteQuery',
    package_data={
    'firebird_lite_query': ['FirebirdLiteQuery.dll', 'FirebirdSql.Data.FirebirdClient.dll', 'Newtonsoft.Json.dll'],
    },
    include_package_data=True,
    license='MIT',
    packages=['firebird_lite_query'],
    install_requires=['requests'],
)