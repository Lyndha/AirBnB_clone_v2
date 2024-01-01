from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route that displays "Hello, Flask!"
@app.route('/')
def hello_flask():
    return 'Hello, Flask!'

# Define a route that displays "HBNB"
@app.route('/')
def hbnb():
    return 'HBNB'

# Run the application if this script is executed
if __name__ == '__main__':
    # Use host='0.0.0.0' to make the app accessible from external devices
    # Use port=5000 as an example; you can choose a different port
    app.run(host='0.0.0.0', port=5000)

