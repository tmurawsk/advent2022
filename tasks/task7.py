from tasks.base import Task


class Node:
    def __init__(self, name: str, is_dir: bool, size: int = -1, parent: "Node" = None):
        self.name: str = name
        self.is_dir: bool = is_dir
        self.size: int = size
        self.parent: Node = parent
        self.children: {str: Node} = {}

    def get_size(self) -> int:
        if not self.is_dir or self.size > 0:
            return self.size
        size = 0
        if self.is_dir:
            for child in self.children.values():
                size += child.get_size()
        self.size = size
        return self.size


class Task7(Task):
    def __init__(self, filename="input/7.txt"):
        super().__init__(filename)

    def read_tree(self) -> Node:
        root = Node('root', True)
        cdir = root
        with self.file as file:
            line = 'temp'
            while line:
                line = file.readline().strip()
                parts = line.split(' ')
                if parts[0] == '$':
                    if parts[1] == 'cd':
                        if parts[2] == '/':
                            cdir = root
                        elif parts[2] == '..':
                            cdir = cdir.parent
                        else:
                            cdir = cdir.children[parts[2]]
                    elif parts[1] == 'ls':
                        next_line = self.peek().strip()
                        while next_line.split(' ')[0] not in ['$', '']:
                            self.file.readline()
                            [dir_or_size, name] = next_line.split(' ')
                            cdir.children[name] = Node(
                                name,
                                dir_or_size == 'dir',
                                int(dir_or_size) if dir_or_size != 'dir' else 0,
                                cdir
                            )
                            next_line = self.peek().strip()
        return root

    def run1(self):
        root = self.read_tree()

        def sum_sizes(node: Node) -> int:
            size = 0
            for child in node.children.values():
                size += (sum_sizes(child) if child.is_dir else 0)
            return size + (node.get_size() if node.get_size() <= 100000 else 0)
        print(sum_sizes(root))
        pass

    def run2(self):
        root = self.read_tree()
        root_size = root.get_size()
        missing_size = 30000000 - (70000000 - root_size)

        def find_min_dir(node: Node, needed_size: int, min_size: int) -> int:
            if needed_size <= node.get_size() < min_size:
                min_size = node.get_size()
            for child in node.children.values():
                if child.is_dir:
                    min_size = find_min_dir(child, needed_size, min_size)
            return min_size
        print(find_min_dir(root, missing_size, root_size))
