from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/paneer_butter_masala")
def paneer_butter_masala():
    return render_template("paneer_butter_masala.html")

@app.route("/jalebi")
def jalebi():
    return render_template("jalebi.html")
    
if __name__ == "__main__":
    app.run(debug=True)
