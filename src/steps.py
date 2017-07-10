from lettuce import step, world
from hello_world import say_hello, ACQANTAINCES, MASTER


def _get_expected_response(name):
    if name:
        if name in ACQANTAINCES:
            return "Hello Friend {0}".format(name)
        if name in MASTER:
            return "Hello Master {0}".format(name)
        return "Hello Stranger"


@step('(\S+) addresses Alexa')
def address_with_a_name(step, name):
    world.name = name
    world.expected_response = _get_expected_response(name)


@step('Alexa is addressed anonymously')
def address_anonymously(step):
    world.name = None
    world.expected_response = "Whatever"


@step('Alexa activates')
def invoke_alexa_greet_func(step):
    world.actual_response = say_hello(world.name)


@step('Alexa responds (\S+)')
def compare_response(step, *args):
    return world.expected_response == world.actual_response




