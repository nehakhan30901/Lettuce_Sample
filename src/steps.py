from lettuce import step, world
from hello_world import say_hello


@step('(\S+) addresses Alexa')
def address_with_a_name(step, name):
    world.name = name

@step('Alexa is addressed anonymously')
def address_anonymously(step):
    world.name = None
    world.expected_response = "Whatever"


@step('Alexa activates')
def invoke_alexa_greet_func(step):
    world.actual_response = say_hello(world.name)


@step('Alexa responds ([\s\S]+)')
def compare_response(step, expected_response):
        assert world.actual_response == expected_response, "Got {0} needed {1}".format(world.actual_response, expected_response)

