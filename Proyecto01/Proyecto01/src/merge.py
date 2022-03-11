

def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.append(json.load(infile))

    with open('counseling3.json', 'w') as output_file:
        json.dump(result, output_file)

