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
    def __init__ (self, start = 0):
        """
        creates a new serial generator object
        """
        self.start = self.next = start
    def __repr__(self)
        """Shows representation
        """
        return f"<SerialGenerator start = {self.start} next = {next}>"

    def generate(self):
        """
        Generate next number
        """
        self.next += 1
        return self.next - 1
    def reset(self):
        """
        Reset number to original starting number
        """
        self.next = self.start