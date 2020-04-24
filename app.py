from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.product.product_routes import initialize_product_routes


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

# Route
initialize_product_routes(api)

if __name__ == "__main__":
    app.run(debug=False)
