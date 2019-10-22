# ott-fizz-buzz

This is "Over The Top" fizz buzz. A project created to learn python using simple logic.

Run with 
```cmd
python fizzbuzz.py "rules" [--min MIN] [--max MAX]
```

## Examples

Run basic fizzbuzz over the range 1 - 100 (inclusive)
```cmd
python fizzbuzz.py "{ \"fizz\": 3, \"buzz\": 5 }"
```

Run basic fizzbuzz over the range 1 - 500 (inclusive)
```cmd
python fizzbuzz.py "{ \"fizz\": 3, \"buzz\": 5 }" --max 500
```

Run a modified fizzbuzz over the range 25 - 75 (inclusive)
```cmd
python fizzbuzz.py "{ \"fizz\": 4, \"buzz\": 7 }" --min 25 --max 75
```
