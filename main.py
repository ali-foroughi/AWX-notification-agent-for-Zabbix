from flask import Flask, request, jsonify
import subprocess
import json
import os

app = Flask(__name__)

ZABBIX_SERVER = os.getenv('ZABBIX_SERVER')
ZABBIX_HOST = os.getenv('ZABBIX_HOST')
ITEM_KEY = os.getenv('ITEM_KEY')

@app.route('/awx/notifications', methods=['POST'])
def awx_notifications():
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON payload received"}), 400

        # Convert the JSON payload to a string
        json_payload = json.dumps(data)
        print(json_payload)
        json_payload = str(json_payload)

        # Create the zabbix_sender command
        command = [
            "zabbix_sender",
            "-z", ZABBIX_SERVER,
            "-s", ZABBIX_HOST,
            "-k", ITEM_KEY,
            "-o", json_payload

        ]
        #print(command)
        # Execute the zabbix_sender command
        result = subprocess.run(command, capture_output=True, text=True)
        #print(result)

        # Check the result of the command
        if result.returncode != 0:
            return jsonify({
                "error": "Failed to send data to Zabbix",
                "details": result.stderr
            }), 500

        return jsonify({"message": "Data successfully sent to Zabbix"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application on port 5000
    app.run(host='0.0.0.0', port=5000)
