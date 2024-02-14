from enum import Enum, unique


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


@unique
class GenericStatus(BaseEnum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DENIED = "DENIED"
