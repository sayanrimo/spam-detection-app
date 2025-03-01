from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load model
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        prediction = model.predict([text])[0]
        return f"Prediction: {'Spam' if prediction == 1 else 'Ham'}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
