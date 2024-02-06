from abc import ABC, abstractmethod


class BaseEstudante:
    @abstractmethod
    def __init__(self, nome, matricula, curso): pass

    @abstractmethod
    @property
    def matricula(self): pass

    @abstractmethod
    @property
    def curso(self): pass
