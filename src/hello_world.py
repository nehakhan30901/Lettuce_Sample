ACQANTAINCES = ["Shruthi", "Shubham"]
MASTER = "Neha"


def say_hello(name=None):
    if name:
        if name in ACQANTAINCES:
            return "Hello Friend {0}".format(name)
        if name in MASTER:
            return "Hello Master {0}".format(name)
        return "Hello Stranger"
    return "Whatever"

