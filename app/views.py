from app.init import app


@app.route("/hello")
def hello():
    return "Hello, Flask!"
