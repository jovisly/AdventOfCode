class Blob:
    def __init__(self, type, name, parent, depth):
        # A blob can be a directory ("d") or a file ("f").
        self.type = type
        self.name = name
        self.parent = parent
        # Children are also blobs.
        self.children = set()
        self.size = -1
        # Depth 0 is root, 1 is root's children, etc. This is to dedupe on the
        # name level.
        self.depth = depth



def process_cd(line, dict_blobs, curr_blob, depth):
    command = line[2:].split(" ")
    dest = command[1]
    if dest == "..":
        depth -= 1
        curr_blob = dict_blobs[(curr_blob.parent, depth)]
    elif dest == "/":
        depth = 0
        if ("/", depth) not in list(dict_blobs):
            dict_blobs[("/", depth)] = Blob("d", "/", None, depth)
        curr_blob = dict_blobs[("/", depth)]
    else:
        depth += 1
        if (dest, depth) not in list(dict_blobs):
            dict_blobs[(dest, depth)] = Blob("d", dest, curr_blob.name, depth)
        curr_blob = dict_blobs[(dest, depth)]

    return dict_blobs, curr_blob, depth



def process_ls(line, dict_blobs, curr_blob, depth):
    result = line.split(" ")
    # When we do ls, the depth of the new blobs is 1 more than the current.
    new_depth = depth + 1
    if result[0] == "dir":
        # Add a directory if it doesn't already exist.
        dirname = result[1]
        if (dirname, new_depth) not in list(dict_blobs):
            dict_blobs[(dirname, new_depth)] = Blob("d", dirname, curr_blob.name, new_depth)
        # We also want to denote that the directory is a child of the current blob.
        curr_blob.children.add((dirname, new_depth))
    else:
        # Otherwise we have a file with a file size.
        size = int(result[0])
        file = result[1]
        if (file, new_depth) not in list(dict_blobs):
            dict_blobs[(file, new_depth)] = Blob("f", file, curr_blob.name, new_depth)
        dict_blobs[(file, new_depth)].size = size
        # We also want to denote that the file is a child of the current blob.
        curr_blob.children.add((file, new_depth))

    return dict_blobs, curr_blob, depth


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()

    curr_blob = None
    depth = 0
    dict_blobs = {}
    ls_mode = False
    for line in lines:
        if line.startswith("$ cd"):
            ls_mode = False
            dict_blobs, curr_blob, depth = process_cd(line, dict_blobs, curr_blob, depth)
        elif line.startswith("$ ls"):
            ls_mode = True
        elif ls_mode == True:
            dict_blobs, curr_blob, depth = process_ls(line, dict_blobs, curr_blob, depth)


    print("=" * 30)
    for k, v in dict_blobs.items():
        print(k, v.__dict__)
    print("=" * 30)

    # Traverse the tree until we have all the directory sizes.
    queue = [k for k, v in dict_blobs.items() if v.size == -1]
    while len(queue) > 0:
        # Find a node whose children all have sizes.
        for q in queue:
            children = dict_blobs[q].children
            if all([dict_blobs[c].size != -1 for c in children]):
                # We can now compute the size of this node.
                dict_blobs[q].size = sum([int(dict_blobs[c].size) for c in children])
                queue.remove(q)
                break

    total = 0
    for _, v in dict_blobs.items():
        if v.type == "d" and v.size <= 100000:
            total += v.size

    return total


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 95437

    # Same input as above but we changed folder "e" to "d" to have dupe folder
    # name. The answer should be the same.
    filename = "input-test2.txt"
    assert solve(filename) == 95437


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
    # 551163 is too low.
    # 757593 is too low T_T
