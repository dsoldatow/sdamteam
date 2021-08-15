from abc import ABCMeta, ABC, abstractmethod
class State(ABC):

    @abstractmethod
    def process_message(self):
        pass

    def validate_message(self):
        pass