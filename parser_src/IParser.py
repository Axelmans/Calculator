import abc


class IParser(abc.ABC):

    @abc.abstractmethod
    def parse(self, user_input: str):
        pass

    @staticmethod
    def print(output):
        print(str(output) + "\n\n")
