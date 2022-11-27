class packet:

    def _init_(self, messaggio):
        self.messaggio=messaggio

    def to_bytes(self):
        messaggio_encoded = self.messaggio.encode("utf8")
        return messaggio_encoded

    @staticmethod
    def from_bytes(buffer):
        messaggio = buffer.decode("utf-8")
        return packet(messaggio)