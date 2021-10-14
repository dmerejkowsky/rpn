# Roadmap

* Handle floats

Currently the stack only handles integers because the spec said nothing
about floats, and json conversion of floats can get tricky. Still, it's
weird that

```
  - push 7
  - push 2
  - apply /
```

returns 2


* Add a route to clear a stack

* Add a route to evaluate expressions, like so:

```
  post /rpn/stack/stack_id/eval
    {"expression" : "8 4 3 + - 5 +"}
```

  which should assert the stack is of length 1 and return the
  last element


* Add a basic UI
