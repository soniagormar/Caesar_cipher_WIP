from dataclasses import dataclass, asdict


@dataclass
class Record:
    operation: str
    input: str
    output: str
    key: int

    def to_save(self, history: list):
        """saves an operation in history"""
        history.append([self.operation, self.input, self.output, self.key])

    # def to_dict(self):
    #     return asdict(self)
