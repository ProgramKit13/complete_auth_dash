import dash
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

import sqlite3
import warnings
import os

from dash import html, dcc
from dash.dependencies import Input, Output, State

from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from werkzeug.security import generate_password_hash, check_password_hash

conn = sqlite3.connect('data.sqlite')
engine = create_engine('sqlite:///data.sqlite')
db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))


Users_table = Table('users', Users.metadata)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])
server = app.server
app.config.suppress_callback_exceptions = True

server.config.update(
    SECRET_KEY = os.urandom(12),
    SQLALCHEMY_DATABASE_URI ='sqlite:///data.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False 
)

db.init_app(server)

class Users(UserMixin, Users):
    pass
