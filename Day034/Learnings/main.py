name: str
is_legal: bool


'''Type hints (or type annotations) are a way to add optional type information to your code. 
They are part of a movement toward "gradual typing" that aims to combine the flexibility of 
dynamic typing with the safety of static typing. '''


def can_drive(age: int) -> bool:  # int represents the type of age and bool represents the return type of the function
    if age < 18:
        return False
    else:
        return True


if can_drive(12):
    print("You can drive!")
else:
    print("Pay the fine!")