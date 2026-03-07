#!/usr/bin/python3
"""
This module develops a simple API using the Flask web framework.
"""
from flask import Flask, jsonify, request

# 1. INITIALIZE the app (Must be done before routes!)
app = Flask(__name__)

# 2. DEFINE your data (In-memory users)
users = {}

# 3. DEFINE your routes
@app.route("/")
def home():
    """Returns the root message."""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """Returns all usernames."""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Returns the status."""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Returns a specific user or 404."""
    user = users.get(username)
    if user:
        return jsonify(user)
    # Ensure this says "User not found" (typo fix from earlier)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user via JSON POST request."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# 4. RUN the app
if __name__ == "__main__":
    app.run()
