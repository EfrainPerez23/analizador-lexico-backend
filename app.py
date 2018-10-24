
from flask import Flask, jsonify
from flask_restful import Api

# Resources
from Resources.AnalizadorLexico import AnalizadorLexico
app = Flask(__name__)


# Load config File
app.secret_key = 'analizador-lexico'

# Init Rest API endpoints
api = Api(app)
api.add_resource(AnalizadorLexico, '/analizador-lexico')

# Main function
if __name__ == '__main__':
    app.run()