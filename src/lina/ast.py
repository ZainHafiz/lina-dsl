from dataclass import dataclass
from typing import Tuple

Shape = Tuple[int, int]

@dataclass(frozen=True)
class Expr:
    shape: Shape

@dataclass(frozen=True)
class Var(Expr):
    name: str

@dataclass(frozen=True)
class MatMul(Expr):
    left: Expr
    right: Expr

    def __post_init__(self):
        if self.left.shape[1] != self.right.shape[0]:
            raise ValueError(
                f"Incompatible shapes for multiplication: "
                f"{self.left.shape} x {self.right.shape}"
            )
