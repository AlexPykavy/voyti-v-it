def greeting(person=None):
    return f"Hello, {person or 'World'}!"


if __name__ == "__main__":
    print(greeting())
    print(greeting("John"))
