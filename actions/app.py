from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Read from the JSON file
try:
    with open('new.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: JSON file not found.")
    data = []


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/courses', methods=['POST'])
def handle_courses():
    if request.method == 'POST':
        if data:
            courses_data = request.json.get('courses', [])
            return jsonify({"courses": courses_data})
        else:
            return jsonify({"error": "Data not available"}), 404
    else:
        return jsonify({"error": "Invalid request method"}), 400

        
@app.route('/certificates', methods=['POST'])
def handle_certificates():
    if request.method == 'POST':
        return jsonify({data[1].get('certificates', [])})
    else:
        return jsonify({"error": "Invalid request method"}), 400


@app.route('/language_trips', methods=['POST'])
def handle_language_trips():
    if request.method == 'POST':
        return jsonify({data[2].get('languageTrips', [])})
    else:
        return jsonify({"error": "Invalid request method"}), 400


@app.route('/tandem_programme', methods=['POST'])
def handle_tandem_programme():
    if request.method == 'POST':
        return jsonify({data[3].get('tandemProgramme', {})})
    else:
        return jsonify({"error": "Invalid request method"}), 400


@app.route('/theatre', methods=['POST'])
def handle_theatre():
    if request.method == 'POST':
        return jsonify({data[3].get('theatre', {})})
    else:
        return jsonify({"error": "Invalid request method"}), 400


@app.route('/language_courses_external', methods=['POST'])
def handle_language_courses_for_external_participants():
    if request.method == 'POST':
        return jsonify({data[4].get('languageCoursesForExternalParticipants', {})})
    else:
        return jsonify({"error": "Invalid request method"}), 400


if __name__ == '__main__':
    app.run(debug=True)
