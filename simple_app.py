from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    greeting = ""
    
    if request.method == "POST":
        name = request.form["name"]  # Get the name from the form
        greeting = f"Hello, {name}!"  # Create a greeting message

    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)
