from GameTree import GameTree

def print_tree(node, file=None, _prefix="", _last=True):
    print(_prefix, "`- " if _last else "|- ", node.matches_list, sep="", file=file)
    _prefix += "   " if _last else "|  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        print_tree(child, file, _prefix, _last)

game_tree = GameTree(6, 1, str([7]))
print_tree(game_tree, file=None, _prefix="", _last=True)