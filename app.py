from flask import Flask
from flask import request
import json
import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def helloworld():
    return 'Hello World'


@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma():
    data = request.json

    results = []
    for entry in data:
        monsters = entry.get('monsters')
        efficiency = calculate_efficiency(monsters, 0, 0)
        results.append({"efficiency": efficiency})
    print(results)
    return jsonify(results)


def calculate_efficiency(monsters, gold, stage):
    if not monsters:
        return gold

    if stage == 0:
        return max(
            calculate_efficiency(monsters[1:], gold - monsters[0], 1),
            calculate_efficiency(monsters[1:], gold, 0)
        )
    elif stage == 1:
        return max(
            calculate_efficiency(monsters[1:], gold + monsters[0], 2),
            calculate_efficiency(monsters[1:], gold, 1)
        )
    elif stage == 2:
        return calculate_efficiency(monsters[1:], gold, 0)
    else:
        return gold

if __name__ == "__main__":
    app.run(debug=False)