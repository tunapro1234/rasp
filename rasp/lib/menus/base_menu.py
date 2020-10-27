from rasp.res.settings import settings


class MetaMenu(type):
    def __new__(cls, name, bases, body):
        # print(cls, name, bases, body, sep="\n")

        attributes = ["draw"]

        if name != "BaseMenu":
            for attr in attributes:
                if attr not in body:
                    raise TypeError(f"Required attribute not found: {attr}")

        return super().__new__(cls, name, bases, body)


class BaseMenu(metaclass=MetaMenu):
    pass # gelicem