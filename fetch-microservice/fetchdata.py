from flask import Flask, jsonify
import oracledb
import csv
import os
app = Flask(__name__)
@app.route('/fetch', methods=['GET'])
def fetch_data():
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
        # Fetch data from the database
        # Execute the query
        cursor.execute("SELECT id, name FROM hm")

        # Fetch all rows
        rows = cursor.fetchall()

        # Prepare the TSV file path
        tsv_file_path = "tsv/employee_details.tsv"

        # Write employee details to the TSV file
        with open(tsv_file_path, 'w', newline='') as tsv_file:
            writer = csv.writer(tsv_file, delimiter='\t')

            # Write header row
            writer.writerow(["ID", "Name"])

            # Write data rows
            for row in rows:
                writer.writerow(row)

        print(f"Employee details saved to {tsv_file_path}")
        
        # Close the cursor
        cursor.close()
        return 'complete!'
fetch_data()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
