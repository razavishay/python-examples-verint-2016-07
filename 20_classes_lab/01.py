class Summer(object):
    def __init__(self, val = 0):
        self.sum = val
    def add(self, *vals):
        for val in vals:
            self.sum += val
    def total (self):
        return self.sum

