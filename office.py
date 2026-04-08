class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        print(f"Printing: {document}")

    def fax(self, document):
        pass  # ei tee midagi

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan!")


# TEST
printer = OldFashionedPrinter()

printer.print("Hello")   # töötab
printer.fax("Test")      # ei tee midagi
printer.scan("Test")     # viskab vea