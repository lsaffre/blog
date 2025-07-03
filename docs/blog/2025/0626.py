from jinja2 import Environment, DictLoader

A = False
B = True


class Foo:

    _bar = None

    @property
    def bar(self):
        if self._bar is None:
            self._bar = Answer(self)
        return self._bar


class Answer:

    def __init__(self, foo):
        if A:
            raise Exception("Oops")
        elif B:
            raise AttributeError("Oops")
        self.answer = 42


TEMPLATE = "The answer is {{foo.bar.answer}}."


env = Environment(
    loader=DictLoader({'1': TEMPLATE}),
)
tpl = env.get_template('1')
print(tpl.render(foo=Foo()))
