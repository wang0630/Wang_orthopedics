from flask import render_template, request, redirect, url_for, Blueprint
from . import app

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(Exception)
def globalError(error):
  print(error)
  return 'smt is wrong', 500
