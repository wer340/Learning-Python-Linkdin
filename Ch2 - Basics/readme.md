

# switch case

```python
   # new in Python 3.10
    # the match-case construct can be used for multiple comparisons
    value = "three"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3, 4)
        case _:
            result = -1
    print(result)
 ```
