"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "Create a serial number starting from a given number"
        self.start = start
        self.plusone = self.start

    def __repr__(self):
        return f"Generate a serial number from {self.start}, with reset functionality. Next number is {self.plusone}."

    def generate(self):
        """Must add one before returning because return stops function.
            Therefore must take away one from the return to avoid returning a 
            number that is one ahead"""
        self.plusone = self.plusone + 1
        return self.plusone - 1

    def reset(self):
        "Reset serial number back to original start number"
        self.plusone = self.start
