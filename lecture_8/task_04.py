import json
a = 'Hello world!'
b = {key: value for key, value in enumerate(a)}
print(b)
c = json.dumps(b, indent=3, separators=('; ', '= '))
print(c)