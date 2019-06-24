from flask_restplus import Api, Resource, fields
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
api = Api(app, version='1.0', title='GAN Generator', description='This app generates things with a GAN')
ns = api.namespace('facespace', description='Methodical methods for generating faces in place namespaces.')

single_parser = api.parser()

@ns.route('/')
class Index(Resource):
  ''' Main page.'''
  @api.doc(parser=single_parser, description='Go Head -- Test me!!')
  def get(self):
    return {"Who did it?": "YOU TESTED ME!"}

if __name__ == '__main__':
  PORT = int(os.environ.get('PORT', 8008))
  app.run(host='0.0.0.0', port=PORT)