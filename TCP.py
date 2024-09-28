# Input data
input_data = \
[
    {
        'dictionary': ['ixnjjomf', 'ybrguwex', 'wvkdbtpf', 'gcjzdkdq', 'fdlbwvlf', 'dqgionus', 'wuiizajo', 'uofvpbxe', 'cyleofmx', 'wtbrvzcz'],
        'mistypes': ['gwjzdkdq', 'wuiszajo', 'fdlbwvpf', 'ixnjjomn', 'cbleofmx']
    }
    ,
    {
        'dictionary': ['ztcil', 'crtds', 'uqkcz', 'kewmt', 'sbvyv', 'xmbss', 'awwet', 'vvtxh', 'bkvfj', 'ccrxs', 'luiut', 'nphrk', 'pbtcc', 'tthca', 'jgyeg', 'jrybu', 'hjbsw', 'txyzw', 'tgjyl', 'qibew', 'ekcnc', 'fekzq', 'xonxw', 'bdldy', 'lirur', 'ntqjb', 'ijzyf', 'egipi', 'tpwgb', 'ajiwb', 'qecfr', 'wntfl', 'rdsob', 'obobd', 'covle', 'lfzzb', 'vlyou', 'enlct', 'tsywn', 'pzlhy', 'nirax', 'bzfov', 'wugny', 'kqeru', 'opepc', 'ynvvb', 'mcmrj', 'kjzlc', 'mdnqu', 'omgew'],
        'mistypes': ['txyzn', 'wugnj', 'rqkcz', 'mdnru', 'vdsob', 'kjzrc', 'tvtxh', 'tsyws', 'awweq', 'aliwb']
    }
]


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

# Call the function with input data
output_data = find_corrections(input_data)

# Output the result
print(output_data)

