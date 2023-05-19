"""
`Decimals`

A class that is able to represent and perform arithmetic operations- \n
using decimal numbers to arbitrary precision.

#TODO: Overload more operators
#TODO: Add support for native `decimal` module
#TODO: Add support for negative numbers

#? If multiple decimal separators are in a number, keep the first and pop the rest to preserve the number? Or throw an exception? (Latter as of now.)
"""

#import os
#os.system("cls||clear")

import re
#import numpy as np
import warnings
#import functools


# The class stores numbers as strings,
# and performs its arithmetic using integer numbers.
# This means the results are valid decimal numbers, while the calculations do not use them.
# Float type numbers are prone to calculation errors due to the way the digits are stored in binary format, this class sees to circumvent that.
# It is not recommended to use float type numbers as arguments for this class.
class Decimals:
    """
    Decimals class for floating-point operations. \n
    Implement as `dec = Decimals("3.4")` \n
    Operate as `newdec = dec + otherdec` \n
    Prefer to use `str` or `int` as argument instead of `float`
    """

    allowed_separators = ('.', ',')
    separator = ','

    @classmethod
    def set_separator(cls, sep:str):
        """Set the symbol that separates the wholes from the decimals, default is ','"""
        if sep in cls.allowed_separators:
            cls.separator = sep
        else:
            raise ValueError(f"set_separator() - Invalid separator '{sep}'")


    def __init__(self, n):

        # Set the number its string value
        n = self.instantiate_number(n)

        # Check using regex if the pattern is a valid one
        n = self.validate_regex(n)

        self.value = n


    #* Magic methods
    #? Mainly for operator overloading

    def __add__(self, other):
        return Decimals(self.additionDecimals(other))

    def __sub__(self, other):
        return Decimals(self.subtractionDecimals(other))

    def __mul__(self, other):
        return Decimals(self.multiplicationDecimals(other))

    def __div__(self, other):
        return Decimals(self.divisionDecimals(other))

    def __str__(self):
        return self.value


    #* Supplementary methods
    #? Validators and helpers

    # Value instantiation method
    # Used during __init__, Checks if input is valid, formats the number and returns a string
    def instantiate_number(self, number) -> str:
        "Returns the string of n (and catches types?)."

        # Raise exception if n is falsy
        if not number:
            raise ValueError("instantiate_number() - n is falsy")

        # Check if already Decimals
        if isinstance(number, Decimals):
            return number.value

        # Check for safe types and return a string
        elif isinstance(number, int) or isinstance(number, str):
            return str(number)

        # Check for unsafe types
        elif isinstance(number, float):
            warnings.warn(f"instantiate_number() - Precision warning: float type number ({number})")
            return str(number)

        else:
            raise TypeError(f"instantiate_number() - Couldn't instantiate \"{number}\" (type: {type(number)})")

    # Number validation method
    # Uses regex to check whether or not given numbers are valid
    # Assumes string input
    def validate_regex(self, number:str):
        "Checks if a given number has a valid numerical pattern using regex."

        # Remove one false period at the end of the number
        if number[-1] in ('.', ','):
            number = number[:-1]

        # Insert '0' at the beginning of the number if the first index is a period
        if number[0] in ('.', ','):
            _ = '0'
            _ += number
            number = _

        # Regex to check if the numbers given are valid. If not, raise an exception
        # Capture pattern => [numbers at the beginning], (none or one separator in the middle), [numbers at the end]
        pattern = re.compile(r'^[0-9]*([.,]?)[0-9]*$')
        match = pattern.fullmatch(number)

        if not match:
            raise ValueError("validate_regex() - Pattern doesn't match on n")

        return number


    #* Numeric conversion functions
    #? Crunches the numbers. Assumes numbers use the valid string format

    def additionDecimals(self, other):

        # Turn numbers into lists, each index holding a digit
        s = [*self.value]
        o = [*other.value]

        # Find index of periods if present. Periods and commas are treated as the same, the first one found will default to the dot used
        # `si` and `oi` keep the indices of the dots found
        si = False
        oi = False

        for i, digit in enumerate(s):
            if digit in Decimals.allowed_separators:
                s[i] = ','
                si = i
                break

        for i, digit in enumerate(o):
            if digit in Decimals.allowed_separators:
                o[i] = ','
                oi = i
                break

        # Normal addition if the numbers aren't decimal
        if not si and not oi:
            print("Short circuit to normal addition")
            short_circuit = str( int("".join(s)) + int("".join(o)) )
            return short_circuit

        # Create two separate lists, one for pre-dot and one for post-dot numbers
        valuesdot = []
        dotvalues = []

        # Add numbers to the corresponding lists
        if si:
            valuesdot.append(s[:si])
            dotvalues.append(s[si+1:])
        else:
            valuesdot.append(s)

        if oi:
            valuesdot.append(o[:oi])
            dotvalues.append(o[oi+1:])
        else:
            valuesdot.append(o)


        # Find appendix for dotvalues
        # Goes for any sequence of sub-decimal values that aren't subject to calculations
        # In (22.450 + 35), 450 is the appendix and dotvalues gets cleared
        if len(dotvalues) == 1:
            # If the length of dotvalues is 1, meaning only one number has decimals, move the decimal value to appendix and paste at the end
            # Change dotvalues to an empty string (falsy)
            appendix = "".join(dotvalues[0])
            dotvalues = ''

        elif len(dotvalues) == 2 and len(dotvalues[0]) != len(dotvalues[1]):
            # If the length of dotvalues is 2, meaning both numbers are decimal numbers, and the lengths are not the same to each other, put the remainder in appendix and paste at the end
            # Remove the remainder from dotvalues

            longest = max(dotvalues, key=len)
            shortest = min(dotvalues, key=len)

            appendix = longest[len(shortest):]
            appendix = "".join(appendix)

            # Slice appendix out of dotvalues
            for i, sub in enumerate(dotvalues):
                if sub == longest:
                    dotvalues[i] = longest[:len(shortest)-len(longest)]

        elif len(dotvalues) == 1:
            appendix = "".join(dotvalues[0])

        else:
            appendix = False


        # If dotvalues, get the length of dotvalues[0]
        # At this point in the code, after looking for the appendix in the if-elif-else statements above, presence and length of dotvalues have been determined
        # Used once, but to good use
        if dotvalues:
            dot_len = len(dotvalues[0])
        else:
            dot_len = 0

        # Change list valuesdot to hold integers and add them up
        valuesdot = ["".join(number) for number in valuesdot]
        valuesdot[0], valuesdot[1] = int(valuesdot[0]), int(valuesdot[1])

        answerdot = valuesdot[0] + valuesdot[1]

        # Convert dotvalues of separate integers and add them up
        if dotvalues:
            for i, sub in enumerate(dotvalues):
                dotvalues[i] = ["".join(sub)]
                dotvalues[i] = int(dotvalues[i][0])

        # Sum up the digits after the decimal point of both numbers
        dotanswer = sum(dotvalues)

        # Turn dotanswer into a string of its held value
        dotanswer = str(dotanswer)

        # If the length of the decimals in dotvalues has changed after addition, add 1 to answerdot and remove the first digit from dotanswer
        # Written in pseudo-math in context with the code, when decimals don't add up to a new number before the dot (0.5 + 0.4 = 0.9), don't add 1
        # If the numbers behind the decimal do add up to a new number before the dot (0.9 + 0.2 = '0.11' = 1.1), account for displacement; add 1 and remove leftmost number from dotanswer
        if dotvalues and len(dotanswer) > dot_len:
            answerdot += 1
            dotanswer = dotanswer[1:]


        # Combine and finish
        final_answer = str(answerdot)

        final_answer += Decimals.separator

        final_answer += str(dotanswer)

        if appendix:
            final_answer += appendix

        return final_answer


    def subtractionDecimals(self, other):
        raise NotImplementedError
