from dataclasses import dataclass, asdict


@dataclass
class Record:
    operation: str
    input: str
    output: str
    key: int


    def to_save(self):
        return

    def to_dict(self):
        return asdict(self)
