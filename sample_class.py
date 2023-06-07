class DummyParam:
    def __init__(self, param_a: int) -> None:
        self.param_a = param_a

    def __str__(self) -> str:
        return f"DummyParam({self.param_a})"

class DummyClass:
    def __init__(self,
                 param_a: DummyParam,
                 param_b: int = 1,
                 param_c: str="hi",
                ) -> None:
        self.a = param_a
        self.b = param_b
        self.c = param_c

    def print(self, ):
        print(self.a, "<-->", self.b, "<-->", self.c)
