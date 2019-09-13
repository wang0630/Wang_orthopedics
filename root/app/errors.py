from flask import render_template, request, redirect, url_for, Blueprint, current_app as app

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(Exception)
def globalError(error):
  app.logger.error(request.base_url)
  return 'smt is wrong', 500
