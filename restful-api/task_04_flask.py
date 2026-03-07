#!/usr/bin/python3
"""
This module develops a simple API using the Flask web framework.
"""
from flask import Flask, jsonify, request

# 1. Instantiate the app FIRST
app = Flask(__name__)

# 2. Define your data
users = {}

# 3. THEN use the decorators
@app.route("/")
def home():
    return "Welcome to the Flask API!"
