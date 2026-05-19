import snowflake.connector

conn=snowflake.connector.connect(

user='username',

password='password',

account='account_id',

warehouse='COMPUTE_WH',

database='DEMO',

schema='PUBLIC'
)

cursor=conn.cursor()

cursor.execute("""

CREATE OR REPLACE TABLE customers(

customer_id INT,

name STRING,

city STRING,

spend FLOAT

)

""")

cursor.execute("""

COPY INTO customers

FROM @my_stage/customers.csv

FILE_FORMAT=(
TYPE=CSV
SKIP_HEADER=1
)

""")

print(
'loaded to snowflake'
)
