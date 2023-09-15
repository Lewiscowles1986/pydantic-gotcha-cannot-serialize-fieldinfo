# Minimal reproducible example

This is a Minimal reproducible example of a weird error from Pydantic, I got a bit turned around by today. Thanks to Robert Cox for rubber-ducking my hellish code (it wasn't this small)

<figure>
<img alt="screenshot of python error, read caption" src="https://github.com/Lewiscowles1986/pydantic-gotcha-cannot-serialize-fieldinfo/assets/2605791/69af5c29-f4b7-4e78-8238-fbb024b10b6c">
<figcaption>

```
Exception has occurred: PydanticSerializationError
Unable to serialize unknown type: <class 'pydantic.fields.FieldInfo'>
  File "/Users/lewiscowles/Projects/study/pydantic-horror-show/pydantic_horror_show/__init__.py", line 13, in <module>
    json = c.json(by_alias=True)
           ^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.PydanticSerializationError: Unable to serialize unknown type: <class 'pydantic.fields.FieldInfo'>
```

</figcaption>
</figure>

## The fix

Well it's simple, just remove the comma, after field b is defined.

https://pylint.pycqa.org/en/latest/user_guide/messages/refactor/trailing-comma-tuple.html

Annoyingly I was using Ruff, black, mypy and some more linting in my project; they all missed this.
My Google search also turned up nothing of much use.

So here is a repo with a minimal example and the advice on fixing 🙃

## Author note

Pydantic is great. I'd consider this a weakness of implementation though. It's a bit of a footgun.
Maybe the error could be nicer; and specifically call out two fields in a tuple being unable to de-serialize.

It's still a great tool, and I hope to avoid this footgun in future 😄.
