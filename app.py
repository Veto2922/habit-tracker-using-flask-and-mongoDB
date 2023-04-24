import os
from flask import Flask,request
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.get_default_database() 

    app.register_blueprint(pages)

    # print(pages.before_request)
    
    return app.run(debug=True)





create_app()





