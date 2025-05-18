from flask import Flask, request, make_response
import csv
import io

app = Flask(__name__)

@app.route('/generate-report', methods=['POST'])
def generate_report():
    try:
        data = request.json
        users = data.get("users", [])

        # Validate expected keys
        if not all(isinstance(u, dict) and {"name", "email", "score"} <= u.keys() for u in users):
            return {"error": "Each user must have name, email, and score"}, 400

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=["name", "email", "score"])
        writer.writeheader()
        writer.writerows(users)

        response = make_response(output.getvalue())
        response.headers["Content-Disposition"] = "attachment; filename=report.csv"
        response.headers["Content-Type"] = "text/csv"
        return response

    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)