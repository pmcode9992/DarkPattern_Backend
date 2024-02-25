from flask import Flask, request, jsonify
from flask_cors import CORS
from Termsfinder import websScrape

app = Flask(__name__)
CORS(app, resources={r"/darkpattern": {"origins": "*"}})  # Allow requests to the '/darkpattern' endpoint from all origins

@app.route('/darkpattern', methods=['POST'])
def post_endpoint():
    if request.method == 'POST':
        # Get the JSON data from the request
        data = request.json

        # Process the data (example: just echoing back the data)
        response_data = {'received_data': data}
        url = data.get('url','')
        op = websScrape(url)
        # Return a JSON response
        return op, 200

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
