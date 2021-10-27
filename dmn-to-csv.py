import xmltodict
from json import dumps
import csv
from sys import argv


def nullToDash(input:str):
    if input is None:
        return "-"
    else:
        return input

def generateCsv(input_file_name:str):
    with open(input_file_name,'r') as f:
        dmnxml:str = f.read()
        dmndict_full:dict = xmltodict.parse(dmnxml)

    # this writes the result as a json file. Uncomment if you need it.
    # json_file_name = "results.json"
    # with open(json_file_name, 'w') as results:
    #     results.write(dumps(dmndict_full, indent=4))

    # Build the csv
    dmndict = dmndict_full["definitions"]["decision"]["decisionTable"]
    csv_header = []
    csv_rules = [] 

    # Populate header
    for input in dmndict["input"]:
        csv_header.append("input: " + input["inputExpression"]["text"])

    for output in dmndict["output"]:
        csv_header.append("output: " + output["@name"])


    # Populate rules
    # Phis part assumes that rules in the dictionary will be in the same order as in the original dmn file.
    rules_counter = 0
    for rule in dmndict["rule"]:
        csv_rules.append([])
        
        # inputs
        for inputEntry in rule["inputEntry"]:
            csv_rules[rules_counter].append(nullToDash(inputEntry["text"]))
        
        # outputs
        for outputEntry in rule["outputEntry"]:
            csv_rules[rules_counter].append(nullToDash(outputEntry["text"]))

        rules_counter += 1

    # Write the CSV file
    with open("rules.csv", 'w') as rules_csv_file:
        file_writer = csv.writer(rules_csv_file, delimiter='|', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(csv_header)
        file_writer.writerows(csv_rules)

if __name__ == "__main__":
    
    input_file_name = "rules.dmn"
    if len(argv)==2:
        input_file_name = argv[1]
    
    generateCsv(input_file_name)