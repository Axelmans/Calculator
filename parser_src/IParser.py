import abc


# simple interface for a parser; feel free to use own language recognition tools in derived classes
class IParser(abc.ABC):

    @abc.abstractmethod
    def parse(self, user_input: str):
        pass

    @staticmethod
    def print(output):
        print(str(output) + "\n")
