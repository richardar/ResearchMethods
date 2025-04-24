from dash import Dash
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import app  # replace with the name of your .py file without `.py`

app = FastAPI()
dash_app = app.app  # the Dash instance from your script
app.mount("/", WSGIMiddleware(dash_app.server))
