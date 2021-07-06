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

    def __init__(self, start=100):
        """sets the starting number"""
        self.start = start
        self.current = start

    def generate(self):
        """increment the number by 1 each time"""
        num = self.current
        self.current += 1
        return num

    def reset(self):
        """reset to the original number"""
        self.current = self.start




    
