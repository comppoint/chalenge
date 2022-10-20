# 1 . Write a program to insert a record in sql table via api 
# 2.  Write a program to update a record via api 
# 3 . Write a program to delete a record via api 
# 4 . Write a program to fetch a record via api
# 5 . All the above questions you have to answer for mongo db as well . 


from flask import request, jsonify, Flask
import mysql.connector as conn
# import pymongo
# import json
import sys


# function for running the mysql query
def run_query(query, database=None, host="localhost", user="root", password="Meena@123"):
    try:
        if database is None:
            db = conn.connect(host=host, user=user, password=password)
        else:
            db = conn.connect(host=host, user=user, password=password, database=database)
        cursor = db.cursor()
        cursor.execute(query)

        print(cursor.rowcount)
        if cursor.rowcount > 0:
            db.commit()
        else:
            result = cursor.fetchall()
            return result
    except conn.Error:
        _, b, _ = sys.exc_info()
        print(b)
    finally:
        db.close()


# create app
app = Flask(__name__)


# 1 . Write a program to insert a record in sql table via api
# My database contain dress database with Attribure table

@app.route('/mysql/insert_data', methods=['GET', 'POST'])
def inset_data_mysql():
    if request.method == 'POST':
        query = request.json["query"]
        host = request.json["host"]
        user = request.json["user"]
        password = request.json["password"]
        database = request.json["database"]
        run_query(query=query, host=host, user=user, password=password, database=database)
        return jsonify("Query run successfully")


# 2.  Write a program to update a record via api
@app.route('/mysql/update_data', methods=['GET', 'POST'])
def update_data_mysql():
    if request.method == 'POST':
        query = request.json["query"]
        host = request.json["host"]
        user = request.json["user"]
        password = request.json["password"]
        database = request.json["database"]
        run_query(query=query, host=host, user=user, password=password, database=database)
        return jsonify("Query run successfully")


# 3 . Write a program to delete a record via api
@app.route('/mysql/delete_data', methods=['GET', 'POST'])
def delete_data_mysql():
    if request.method == 'POST':
        query = request.json["query"]
        host = request.json["host"]
        user = request.json["user"]
        password = request.json["password"]
        database = request.json["database"]
        run_query(query=query, host=host, user=user, password=password, database=database)
        return jsonify("Query run successfully")


# 4 . Write a program to fetch a record via api
@app.route('/mysql/fetch_data', methods=['GET', 'POST'])
def fetch_data_mysql():
    if request.method == 'POST':
        query = request.json["query"]
        host = request.json["host"]
        user = request.json["user"]
        password = request.json["password"]
        database = request.json["database"]
        data = run_query(query=query, host=host, user=user, password=password, database=database)
        return str(data)


if __name__ == "__main__":
    app.run()
