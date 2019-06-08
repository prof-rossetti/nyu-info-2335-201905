# The `json` Module

Reference: https://docs.python.org/3/library/json.html.

Use `json.dumps()` to convert a dictionary to JSON:

```python
import json

person = {
    "first_name": "Ophelia",
    "last_name": "Clarke",
    "message": "Hi, thanks for the ice cream!",
    "fav_flavors": ["Vanilla Bean", "Mocha", "Strawberry"]
}

json.dumps(person)
```

... or vice-versa using `json.loads()` to convert a JSON string into a dictionary.
