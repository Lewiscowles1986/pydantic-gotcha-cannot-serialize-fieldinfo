from pydantic import BaseModel, Field


class SomeClass(BaseModel):
    a: str = Field(default="field a")
    b: str = Field(default="field b"),
    c: str = Field(default="field c")


if __name__ == "__main__":
    c = SomeClass()
    dict = c.dict(by_alias=True)
    json = c.json(by_alias=True)
    print(f"dict:\n\t{str(dict)}\n\njson:\n\t{str(json)}\n\n")
