# The `json` Module

Reference: https://docs.python.org/3/library/json.html.

Use `json.dumps()` to convert a dictionary to JSON:

```python
import json

person = {
    "first": "Santa",
    "last": "Claus",
    "message": "Ho Ho Ho",
    "stops": ["New York", "Denver", "San Francisco"]
}

json.dumps(person)
```

... or vice-versa using `json.loads()` to convert a JSON string into a dictionary.
