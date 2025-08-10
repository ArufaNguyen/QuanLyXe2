from abc import ABC, abstractmethod

class IAccountRepository(ABC):
    @abstractmethod
    def authenticate(self, username: str, password: str) :
        pass

    @abstractmethod
    def is_used(self, username: str) :
        pass

    @abstractmethod
    def is_admin(self, username: str) :
        pass

    @abstractmethod
    def is_owner(self, username: str) :
        pass

    @abstractmethod
    def create_account(self, username: str, password: str, role: str, requirement_role: str) :
        pass

    @abstractmethod
    def close(self) :
        pass
