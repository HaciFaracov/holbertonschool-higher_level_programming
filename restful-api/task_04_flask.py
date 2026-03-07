@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    # The fix is adding "not" to the error message below
    return jsonify({"error": "User not found"}), 404
