from abc import ABC, abstractmethod # permite usar classe/metodos abstratos

# classe abstrata para as outras ferramentas
class Ferramenta(ABC):
    def __init__(self, canvas):
        self.canvas = canvas

    @abstractmethod
    def clicar_esquerdo(self):
        pass

    @abstractmethod
    def arrastar_esquerdo(self):
        pass

    @abstractmethod
    def soltar_esquerdo(self):
        pass

    @abstractmethod
    def clicar_direito(self):
        pass

    @abstractmethod
    def arrastar_direito(self):
        pass

    @abstractmethod
    def soltar_direito(self):
        pass