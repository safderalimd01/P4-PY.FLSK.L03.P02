from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS

from resources.utility.config import app
from resources.auth.auth_routes import initialize_auth_routes
from resources.product.product_routes import initialize_product_routes
from resources.client.client_routes import initialize_client_routes


CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

# Route
initialize_auth_routes(api)
initialize_product_routes(api)
initialize_client_routes(api)

if __name__ == "__main__":
    load_dotenv()
    app.run(debug=False)
