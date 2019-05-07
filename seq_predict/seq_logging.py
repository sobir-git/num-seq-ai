class LogTree:
    '''
    A tree containg logs as nodes.
    '''
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print(self, level=0, **kwargs):
        for child in self.children:
            if isinstance(child, str):
                text = "{}| {}".format('----' * level, child)
                print(text, **kwargs)
            else:
                child.print(level + 1, **kwargs)

    def to_string(self, level=0):
        result = ""
        for child in self.children:
            if isinstance(child, str):
                text = "{}{}| {}".format(
                    '    ' * max(level - 1, 0), '----' * (level > 0), child)
                result += text + '\n'
            else:
                result += child.to_string(level=level + 1) + '\n'

        return result


if __name__ == "__main__":
    # some tests
    lt = LogTree(["1, -2, 3, -4"])
    lt1 = LogTree(["1, 3  \t\tby alternation"])
    lt2 = LogTree(["-2, -4  \t\tby alternation"])
    lt3 = LogTree(["2, 4  \t\tby abs values"])
    lt4 = LogTree(["-1, -1  \t\tby abs values"])
    lt2.add_child(lt3)
    lt2.add_child(lt4)
    lt.add_child(lt1)
    lt.add_child(lt2)
    lt.print()
