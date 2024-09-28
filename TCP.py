def find_corrections(input_data):
    corrections_list = []

    for data in input_data:
        correct_words = []
        for word in data['dictionary']:
            for mistyped_word in data['mistypes']:
                if len(word) == len(mistyped_word):
                    diff_count = sum(1 for c1, c2 in zip(word, mistyped_word) if c1 != c2)
                    if diff_count == 1:
                        correct_words.append(word)
                        break

        corrections_list.append({"corrections": correct_words})

    return corrections_list


# Input data
input_data = [
    {
        "dictionary": ["purple", "rocket", "silver", "gadget", "window", "dragon"],
        "mistypes": ["purqle", "gadgat", "socket", "salver"],
    }
]

# Call the function with input data
output_data = find_corrections(input_data)

# Output the result
print(output_data)

