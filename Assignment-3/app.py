from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML Template for UI
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Flask App</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        form { margin: 20px; }
        input[type="text"] { padding: 8px; font-size: 16px; }
        input[type="submit"] { padding: 8px 16px; font-size: 16px; }
        .message { margin-top: 20px; font-size: 18px; color: #333; }
    </style>
</head>
<body>
    <h1>Welcome to the Simple Flask App!</h1>
    <form method="POST">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <input type="submit" value="Submit">
    </form>
    {% if message %}
        <div class="message">{{ message }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        message = f"Hello, {name}! Welcome to the Flask App."
    return render_template_string(html_template, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
