Feature: Testing greeting behaviour of Alexa

    Scenario: Alexa identifies its master and greet accordingly
        Given  Neha addresses Alexa
        When   Alexa activates
        Then   Alexa responds Hello Master Neha


    Scenario: Alexa identifies friends and greet accordingly
        Given  Shubham addresses Alexa
        When   Alexa activates
        Then   Alexa responds Hello Friend Neha


    Scenario: Alexa greets a stranger
        Given  Tanushree addresses Alexa
        When   Alexa activates
        Then   Alexa responds Hello Stranger

    Scenario: Alexa is not nice to anonymous calls
        Given  Alexa is addressed anonymously
        When   Alexa activates
        Then   Alexa responds Whatever











