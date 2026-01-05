

"""
    Problem Statement
        A company wants to send automated promotional messages to its customers.

    You are given:
        * A greeting message
        * A promotion text
        * The number of times the message should be displayed on a digital notice board

    Your task is to:
        1. Concatenate the greeting and promotion text with " - " between them.
        2. Repeat the complete message using the * operator based on the given number.
        3. Print the final output

    Real-World Use Case
        This simulates:
            * Automated message creation
            * Digital banner or LED board message repetition
            * Basic text processing used in marketing systems
"""


greeting = input("Greeting: ")
promotion = input("Promotion: ")
repeat = int(input("Times Repeat: "))

message = greeting + " - " + promotion + " | "
print(message * repeat)
