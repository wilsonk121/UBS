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

@app.route('/bugfixer/p2', methods=['POST'])
def bugfixer():

    data = request.json
    result=[]
    for entry in data:
        bugseq_list = entry.get('bugseq')
        print(bugseq_list)
        result.append(max_bugsfixed(bugseq_list,0,0))
    print(result)
    return jsonify(result)


def max_bugsfixed(lst,current_time,bug_fixed):
    bugfixed_list = []

    temp = lst.copy()
    for i in temp:
        if current_time + i[0] > i[1]:
            lst.remove(i)

    if not lst:
        return bug_fixed


    for each in lst:
        temp=lst.copy()
        temp.remove(each)
        bugfixed_list.append(max_bugsfixed(temp,current_time+each[0],bug_fixed+1))

    return max(bugfixed_list)



if __name__ == "__main__":
    app.run(debug=False)