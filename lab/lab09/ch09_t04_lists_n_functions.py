# Write your function below!
imp
def fizz_count(x:list[str]):
    count = 0
    for item in x:
        if item == "fizz":
            count += 1
    return count
    