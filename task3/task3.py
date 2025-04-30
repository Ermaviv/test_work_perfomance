import json
import pandas

with (open("report.json", 'w') as report_file):

    tests = pandas.read_json("tests.json").to_dict()
    dic_values = pandas.read_json("values.json").to_dict()

    id_value = {}

    for test in dic_values["values"].values():
        id_value[test['id']] = test['value']

    def recursive_call(data):
        for tmp in data:
            if isinstance(tmp, dict) and 'value' in tmp.keys():
                tmp["value"] = id_value[tmp["id"]]
            if 'values' in tmp.keys():
                recursive_call(tmp['values'])


    tests_values = tests['tests'].values()
    recursive_call(tests_values)

    json.dump(tests, report_file, indent=2)
