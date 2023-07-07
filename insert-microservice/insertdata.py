import oracledb
import os
from flask import Flask, request
# Fetch and process data from the database
app = Flask(__name__)
@app.route('/insert', methods=['POST'])
def insert_data():
        data = request.get_json()
        # Oracle DB connection details
        db_username = os.environ.get('db_user')
        db_password = os.environ.get('db_pass')
        db_host = os.environ.get('db_host')
        db_port = '1521'
        db_service = os.environ.get('db_service')
        print('Connecting to Oracle database...')
        # Establish a connection to the Oracle database
        connection = oracledb.connect(
        user=db_username,
        password=db_password,
        dsn=f'{db_host}:{db_port}/{db_service}',
        mode=oracledb.SYSDBA
        )
        print("Successfully connected to Oracle Database")
        # Create a cursor
        cursor = connection.cursor()
        #below code is to create table named hm which need to run only once to create the table
        # query = "create table hm(name varchar2(250),id number)"
        # cursor.execute(query)
        entries = data.get('entries')
        for entry in entries:
                employee_id = entry.get('id')
                name = entry.get('name')
                cursor.execute("INSERT INTO hm (id, name) VALUES (:employee_id, :name)",
                       {'employee_id': employee_id, 'name': name})
        connection.commit()
        print('Data inserted successfully')
        # Close the cursor and connection
        cursor.close()
        connection.close()
        print('Connection to Oracle database closed')
        return 'completed!'
# Usage example
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
