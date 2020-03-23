import json
from flask import Flask, jsonify, request
import autobot_logic as al

app = Flask(__name__)


@app.route('/collect', methods=['POST'])
def collect():
    memory = json.loads(request.form.get('Memory'))
    answers = memory['twilio']['collected_data']['collect_api_request']['answers']

    input_string = answers['main_topic']['answer']
    message = al.answers(input_string)

    return jsonify(actions=[{'say': {'speech': message}}])


if __name__ == '__main__':
    app.run()
