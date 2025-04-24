from dash import Dash
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import your_dash_script_name  # replace with the name of your .py file without `.py`

app = FastAPI()
dash_app = your_dash_script_name.app  # the Dash instance from your script
app.mount("/", WSGIMiddleware(dash_app.server))
