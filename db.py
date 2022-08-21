import mysql.connector
from mysql.connector import errorcode

print("Connect...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Erro user or password')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `skills`;")

cursor.execute("CREATE DATABASE `skills`;")

cursor.execute("USE `skills`;")

# criando skills
TABLES = {}
TABLES['skill_user'] = ('''
      CREATE TABLE `skill_user` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) NOT NULL,
      `experience` varchar(40) NOT NULL,
      `version` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['users'] = ('''
      CREATE TABLE `users` (
      `name` varchar(20) NOT NULL,
      `nickname` varchar(8) NOT NULL,
      `password` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for table_name in TABLES:
      tabela_sql = TABLES[table_name]
      try:
            print('Create table {}:'.format(table_name), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Table allready exist')
            else:
                  print(err.msg)
      else:
            print('OK')

# insert user
user_sql = 'INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)'
users = [
      ("Admin", "adm", "123456")
]
cursor.executemany(user_sql, users)

cursor.execute('select * from skills.users')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])

# insert skills
skill_sql = 'INSERT INTO skill_user (name, experience, version) VALUES (%s, %s, %s)'
skills = [
      ('Java', '5 years', '1.8'),
      ('Python', '2 years', '3')
]
cursor.executemany(skill_sql, skills)

cursor.execute('select * from skills.skill_user')
print(' -------------  skills:  -------------')
for skill in cursor.fetchall():
    print(skill[1])

# commit
conn.commit()

cursor.close()
conn.close()