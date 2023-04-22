from option import Option, some, none


def list_get(list, index: int) -> Option:
    if 0 <= index < len(list):
        return some(list[index])
    else:
        return none()
