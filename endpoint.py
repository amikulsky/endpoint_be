import sys

tree = {}


def create(dir):
    """ Creates a directory in a hierarchy
    :param dir: directory to add to the tree
    """
    parent = tree
    for name in dir.split('/'):
        p = parent.get(name)
        if p == None:
            p = {}
            parent[name] = p
        parent = p
    print(f"CREATE {dir}")


def list(dir, padding=''):
    """ Recursively print out the hierarchy below
    :param dir: parent(root) directory
    :param padding: left-padding for current directory level
    """
    for name in sorted(dir):
        print(padding, name, sep='')
        list(dir[name], padding=padding + '  ')


def _find_dir(source_dir):
    """Finds the parent dictionary and the final key.
       If some part of the path is missing, returns the missing part for error reporting.
       :param source_dir source directory to find
       :return parent and directory name
    """
    path_split = source_dir.split('/')
    parent = tree
    for i, part in enumerate(path_split[:-1]):  # Traverse all but the last part
        if part in parent:
            parent = parent[part]
        else:
            return None, path_split[i]  # Return the missing part
    if path_split[-1] not in parent:
        return None, path_split[-1]  # Final element does not exist

    return parent, path_split[-1]  # Return valid parent and key


def move(src, dest):
    """
    move directory
    :param src: source dir
    :param dest: destination
    """

    # 1. find source source
    src_parent, src_key = _find_dir(src)
    if src_parent is None:
        print(f"Cannot move {src} - {src_key} does not exist")
        return

    # 2. find the destination
    parent = tree
    dest_split = dest.split('/')
    for part in dest_split:
        if part not in parent:
            parent[part] = {}  # create parent part if missing
        parent = parent[part]
    dest_parent = parent

    # 3. Move the item
    item_to_move = src_parent.pop(src_key)
    dest_parent[src_key] = item_to_move

    print(f"MOVE {src} {dest}")


def delete(dir_to_delete):
    """
    delete directory
    :param dir_to_delete: directory to delete
    """
    print("DELETE", dir_to_delete)
    parent, key = _find_dir(dir_to_delete)

    if parent is None:
        print(f"Cannot delete {dir_to_delete} - {key} does not exist")
        return

    del parent[key]
    # print(f"DELETE {dir}")


def process_command(command):
    """
    process the command
    :param command: command string
    """
    args = command.strip().split()
    if not args:
        return

    command = args[0].upper()
    params = args[1:]

    if command == "CREATE" and len(params) == 1:
        create(params[0])
    elif command == "LIST" and len(params) == 0:
        print("LIST")
        list(tree)
    elif command == "MOVE" and len(params) == 2:
        move(params[0], params[1])
    elif command == "DELETE" and len(params) == 1:
        delete(params[0])
    else:
        print(f"Ignoring: {command.strip()}")


if __name__ == "__main__":
    for line in sys.stdin:
        process_command(line)
