import json
import sys

values_name_file = sys.argv[1]
tests_name_file = sys.argv[2]
report_name_file = sys.argv[3]

with (
    open(values_name_file, 'r') as values_file,
    open(tests_name_file, 'r') as tests_file,
    open(report_name_file, 'w') as report_file,
):
    tests = json.load(tests_file)
    dic_values = json.load(values_file)

    id_value = {}

    for test in dic_values["values"]:
        id_value[test['id']] = test['value']


    def recursive_call(data):
        for tmp in data:
            if isinstance(tmp, dict) and 'value' in tmp.keys():
                tmp["value"] = id_value[tmp["id"]]
            if 'values' in tmp.keys():
                recursive_call(tmp['values'])

    tests_values = tests['tests']
    recursive_call(tests_values)

    json.dump(tests, report_file, indent=2)
