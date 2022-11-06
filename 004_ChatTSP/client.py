class packet:
    NEW_FILE = 0
    GO_ON = 1
    END_FILE = 2

    def __init__(self, status, data):
        # TODO: add validation
        self.status = status
        self.data = data

    def to_bytes(self):
        status = self.statuss.to_bytes(1, 'big')
        size = len(self.data)
        size = size.to_bytes(2, 'big')
        return status + size + self.data

    @staticmethod
    def 