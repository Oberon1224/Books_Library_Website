#Copyright 2024 Bushuev Dmitrii
from flask import Flask, request, render_template, abort, Response, session,redirect, json
import database as db
from blueprints import*

app = Flask(__name__, static_folder='./static', template_folder='./templates')

app.register_blueprint(style)
app.register_blueprint(change_state)
app.register_blueprint(select_books)
app.register_blueprint(select_books_state)
app.register_blueprint(search_filter)
app.register_blueprint(book_read)
app.register_blueprint(add_to_database)
app.register_blueprint(change_book_information)
app.register_blueprint(auth)

app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = b'fdgogtptreertkytytjvcmw'
app.config['UPLOAD_FOLDER'] ="../static/temp"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['DATABASE'] = 'dbe.db'
app.config['ABOUT'] = db.About(app.config['DATABASE'])
app.config['AUTHOR'] = db.Author(app.config['DATABASE'])
app.config['BOOK'] = db.Book(app.config['DATABASE'])
app.config['CATEGORY'] = db.Category(app.config['DATABASE'])
app.config['LANGUAGE'] = db.Language(app.config['DATABASE'])
app.config['LIST_AUTHORS'] = db.ListAuthors(app.config['DATABASE'])
app.config['LIST_NOTES'] = db.ListNotes(app.config['DATABASE'])
app.config['LIST_STATES'] = db.ListStates(app.config['DATABASE'])
app.config['LIST_TAGS'] = db.ListTags(app.config['DATABASE'])
app.config['NOTE'] = db.Note(app.config['DATABASE'])
app.config['STATE'] = db.State(app.config['DATABASE'])
app.config['TAG'] = db.Tag(app.config['DATABASE'])
app.config['YEAR'] = db.Year(app.config['DATABASE'])
app.config['USER'] = db.User(app.config['DATABASE'])
app.config['VIEW_ARTICLES'] = db.ViewArticles(app.config['DATABASE'])
app.config['VIEW_BOOKS'] = db.ViewBooks(app.config['DATABASE'])
app.config['VIEW_END_READ'] = db.ViewEndRead(app.config['DATABASE'])
app.config['VIEW_IN_READ'] = db.ViewInRead(app.config['DATABASE'])
app.config['VIEW_FAVORITES'] = db.ViewFavorites(app.config['DATABASE'])
app.config['VIEW_JOORNALS'] = db.ViewJoornals(app.config['DATABASE'])
app.config['VIEW_SEARCH'] = db.ViewSearch(app.config['DATABASE'])
app.config['VIEW_FILTER'] = db.ViewFilter(app.config['DATABASE'])
app.config['CREATE_DATABASE'] = db.CreateDataBase(app.config['DATABASE'])
app.config['SEARCH_TITLE'] = None
app.config['FILTER_YEAR'] = None
app.config['FILTER_TAG'] = None
app.config['FILTER_LANGUAGE'] = None
app.config['USER_LOGIN'] = None
app.config['STYLE'] = 'style5'

