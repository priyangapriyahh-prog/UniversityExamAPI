from flask import Flask, jsonify

app = Flask(__name__)

results = {
    "2026001": {
        "student_id": "2026001",
        "course": "Cloud Computing",
        "grade": "A"
    }
}

@app.route("/")
def home():
    return jsonify({
        "message": "University Examination Result API",
        "status": "Success"
    })

@app.route("/api/results/<student_id>")
def get_result(student_id):

    if student_id in results:
        return jsonify(results[student_id]), 200

    return jsonify({
        "error": "Student result not found"
    }), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)