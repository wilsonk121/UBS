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
    print(data)
    for entry in data:
        bugseq_list = entry.get('bugseq')
        print(bugseq_list)
        result.append(max_bugsfixed(bugseq_list,0,0))
    print("result is")
    print(result)
    return jsonify(result)


def max_bugsfixed(lst, current_time=0, bug_fixed=0, memo=None):
    if memo is None:
        memo = {}

    # Create a key for the memoization dictionary
    key = (current_time, bug_fixed)
    if key in memo:
        return memo[key]

    # Filter valid bugs
    valid_bugs = [(time_needed, deadline) for time_needed, deadline in lst if current_time + time_needed <= deadline]

    if not valid_bugs:
        return bug_fixed

    max_fixed = bug_fixed
    for i, (time_needed, deadline) in enumerate(valid_bugs):
        # Recurse without the current bug
        new_bugs = valid_bugs[:i] + valid_bugs[i + 1:]
        max_fixed = max(max_fixed, max_bugsfixed(new_bugs, current_time + time_needed, bug_fixed + 1, memo))

    # Store the result in the memoization dictionary
    memo[key] = max_fixed
    return max_fixed


@app.route('/the-clumsy-programmer', methods=['POST'])
def TCP():
    data = request.json
    print(data)
    return jsonify(find_corrections(data))


def find_corrections(input_data):
    corrections_list = []

    for data in input_data:
        correct_words = []

        # Group dictionary words by their lengths
        length_dict = {}
        for word in data['dictionary']:
            word_len = len(word)
            if word_len not in length_dict:
                length_dict[word_len] = []
            length_dict[word_len].append(word)

        for mistyped_word in data['mistypes']:
            mistyped_len = len(mistyped_word)

            # Only check words of the same length
            if mistyped_len in length_dict:
                for word in length_dict[mistyped_len]:
                    diff_count = sum(1 for c1, c2 in zip(word, mistyped_word) if c1 != c2)
                    if diff_count == 1:
                        correct_words.append(word)
                        break  # Found a correction, no need to check further

        corrections_list.append({"corrections": correct_words})

    return corrections_list



if __name__ == "__main__":
    app.run(debug=False)