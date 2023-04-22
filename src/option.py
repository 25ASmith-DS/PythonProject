

class CalledUnwrap(Exception):
    def __init__(self):
        super().__init__()


class Option:
    def __init__(self, item, is_none):
        if is_none:
            self.item = None
        else:
            self.item = item

    def some(s):
        return Option(s, False)

    def none():
        return Option(0, True)

    def is_some(self) -> bool:
        return self.item is not None

    def is_none(self) -> bool:
        return not self.is_some()

    def from_bool(b: bool, item):
        return Option.some(item) if b else Option.none()

    def unwrap(self):
        if self.is_some():
            return self.item
        else:
            raise CalledUnwrap

    def unwrap_or(self, other):
        try:
            return self.unwrap()
        except CalledUnwrap:
            return other

    def unwrap_or_else(self, func):
        try:
            return self.unwrap()
        except CalledUnwrap:
            return func()

    def map(self, func):
        if self.is_some():
            return Option.some(func(self.unwrap()))
        else:
            return Option.none()


none = Option.none
some = Option.some
