from flask import Flask, render_template
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recomd.db'
db = SQLAlchemy(application)

class RECMDLIST(db.Model):
    #searchword = request.args.get('keyword', '')

    ID = db.Column(db.Integer, primary_key=True)
    TARGET_PERSON = db.Column(db.Unicode)
    PERSON1 = db.Column(db.Unicode)
    PERSON2 = db.Column(db.Unicode)
    PERSON3 = db.Column(db.Unicode)
    PERSON4 = db.Column(db.Unicode)
    PERSON5 = db.Column(db.Unicode)
    PERSON6 = db.Column(db.Unicode)
    PERSON7 = db.Column(db.Unicode)
    PERSON8 = db.Column(db.Unicode)
    PERSON9 = db.Column(db.Unicode)
    PERSON10 = db.Column(db.Unicode)


db.create_all()

@application.route('/', methods=['GET'])
def index():
    return render_template('recomd.html')

api_manager = APIManager(application, flask_sqlalchemy_db=db)
api_manager.create_api(RECMDLIST, methods=['GET'])

if __name__ == "__main__":
    application.run()
    application.debug = True
# import os
# import os.path

# from flask import Flask, render_template
# from flask.ext.restless import APIManager
# from flask.ext.sqlalchemy import SQLAlchemy

# # Step 0: the database in this example is at './test.sqlite'.
# DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
#                         'test.sqlite')
# if os.path.exists(DATABASE):
#     os.unlink(DATABASE)

# # Step 1: setup the Flask application.
# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['TESTING'] = True
# app.config['SECRET_KEY'] = os.urandom(24)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % DATABASE

# # Step 2: initialize extensions.
# db = SQLAlchemy(app)
# api_manager = APIManager(app, flask_sqlalchemy_db=db)


# # Step 3: create the database model.
# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Unicode)


# # Step 4: create the database and add some test people.
# db.create_all()
# for i in range(1, 10):
#     person = Person(name=u'person' + unicode(i))
#     db.session.add(person)
# db.session.commit()
# print Person.query.all()

# # Step 5: create endpoints for the application.
# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')

# # Step 6: create the API endpoints.
# api_manager.create_api(Person, methods=['GET'])

# # Step 7: run the application.
# app.run()