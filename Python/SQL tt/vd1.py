import sqlite3
import pandas as pd
dbase = sqlite3.connect("HR.db")
sql = '''SELECT employee_id, first_name||' '||last_name AS Name, hire_date, salary FROM employees;'''
df = pd.read_sql_query(sql, dbase)
df.head()
print(df.head())
dbase.close() 