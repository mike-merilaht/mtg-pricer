# "Over The Top" Fizz Buzz

This is "Over The Top" fizz buzz. A project created to learn python using simple logic.

Run with 
```cmd
python fizzbuzz.py "rules" [--min MIN] [--max MAX]
```

## Rules Argument

The rules argument is a JSON string that defines a word and a number pairing. The word will be replaced using the number and the rules of [FizzBuzz](https://en.m.wikipedia.org/wiki/Fizz_buzz).

### Example

This is a prettied version of the JSON rules used in the examples later in this read me

```JSON
{
  "fizz": 3,
  "buzz": 5
}
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
