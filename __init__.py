import os
from flask import Flask

def app(config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
      SECRET_KEY='dev',
      DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
  )

  if config:
    app.config.from_mapping(config)
  else:
    app.config.from_pyfile('config.py', silent=True)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  @app.route('/hello')
  def hello():
    return 'hello world'

  return app
