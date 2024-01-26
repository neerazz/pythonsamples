import json
from collections import namedtuple
from typing import List


def namedtuple_from_mapping(fields, values, className: str):
    namedtuple_maker = namedtuple(className, fields)
    mapping = {fields[i]: values[i] for i in range(len(fields))}
    return namedtuple_maker(**mapping)


def toNamedtuple(obj, classNames: List[str] = None):
    if isinstance(obj, dict):
        className = "C" if classNames is None or len(classNames) == 0 else classNames.pop()
        fields, values = [], []
        for key, value in obj.items():
            fields.append(key)
            values.append(toNamedtuple(value, classNames))
        return namedtuple_from_mapping(fields, values, className)
    elif isinstance(obj, (list, set, tuple)):
        return [toNamedtuple(item, classNames) for item in obj]
    else:
        return obj


if __name__ == '__main__':
    file = open("sample.json")
    json_data = json.load(file)
    tuple_res = toNamedtuple(json_data)
    print(tuple_res)
