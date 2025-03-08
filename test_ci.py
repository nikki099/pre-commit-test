# test_ci.py


def greet(name: int) -> str:
    print("Hello, " + str(name) + "!")
    return "42"


if __name__ == "__main__":
    greet(2)
