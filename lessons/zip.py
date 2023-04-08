"""CQ04 - Dict Function Writing."""

def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    output: dict[str, int] = dict()
    if len(keys) == 0 & len(values) == 0:
        return output
    elif len(keys) != len(values):
        return output
    else:
        i: int = 0
        while i < len(keys):
            output[keys[i]] = values[i]
            i += 1
        return output

