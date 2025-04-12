from flask import Blueprint, request, jsonify
import psycopg2
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="7M@n64",
    host="localhost",   
    port="3823"         
)
cur = conn.cursor()
createnew = Blueprint('signup', __name__, url_prefix='/signup')

@createnew.route('/', methods=['POST'])
def get_player():
    data = request.get_json()
    cur.execute("INSERT INTO test_accounts (username,password,wins) VALUES (%s,%s,%s)",(data["username"],data["password"],data["wins"]))
    conn.commit()
    return jsonify({"message":"saved to db"})