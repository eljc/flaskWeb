SECRET_KEY = 'teste'

SQL_ALCHEMY_DATABASE_URI = \
    '{SGDB}://{user}:{pwd}@{server}/{database}'.format(
        SGDB = 'mysql+myqslconnector',
        user = 'root',
        pwd = 'eljc102030',
        server = '127.0.0.1',
        database = 'skills'
    )