# Write your function below!
from typing import list
def fizz_count(x:list[str]):
    count = 0
    for item in x:
        if item == "fizz":
            count += 1
    return count
    