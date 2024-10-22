from flask import Flask
from threading import Thread

# Creates a new Flask web app
app = Flask("")

# Defines a route for the root URL ("/") of the web server
@app.route("/")
def home():
   # Returns a simple message when accessed, indicating that the server is running
   return "Hello. I am alive!"

# Function to start the Flask web server
def run():
  # The server listens on all network interfaces (0.0.0.0) at port 8080
  app.run(host='0.0.0.0', port=8080)

# Starts the web server in a new thread, keeping it active in the background
def keep_alive():
   t = Thread(target=run)
   t.start()
