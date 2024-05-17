Feature: Product Persistence
  In order to manage Instances of Product
  As a user
  I want to be able to perform persist Operations on Instances

  Scenario: Create Instance
    Given an instance
    When saving the instance
    Then the instance is saved in the DB

#   Scenario: Read Instance
#     Given I have two numbers 10 and 5
#     When I subtract the second number from the first number
#     Then the result should be 5

#   Scenario: Update Instance
#     Given I have two numbers 10 and 5
#     When I multiply them together
#     Then the result should be 50

#   Scenario: Delete Instance
#     Given I have two numbers 10 and 5
#     When I divide the first number by the second number
#     Then the result should be 2