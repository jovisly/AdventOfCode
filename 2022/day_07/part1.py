class Blob:
    def __init__(self, type, fullpath, parent):
        # A blob can be a directory ("d") or a file ("f").
        self.type = type
        self.fullpath = fullpath
        self.parent = parent
        # Children are also blobs.
        self.children = set()
        self.size = -1



def process_cd(line, dict_blobs, curr_blob):
    command = line[2:].split(" ")
    dest = command[1]
    if dest == "..":
        curr_blob = dict_blobs[curr_blob.parent]
    elif dest == "/":
        if "/home" not in list(dict_blobs):
            dict_blobs["/home"] = Blob("d", "/home", None)
        curr_blob = dict_blobs["/home"]
    else:
        fullpath = curr_blob.fullpath + "/" + dest
        if fullpath not in list(dict_blobs):
            dict_blobs[fullpath] = Blob("d", fullpath, curr_blob.fullpath)
        curr_blob = dict_blobs[fullpath]

    return dict_blobs, curr_blob



def process_ls(line, dict_blobs, curr_blob):
    result = line.split(" ")
    # When we do ls, the depth of the new blobs is 1 more than the current.
    if result[0] == "dir":
        # Add a directory if it doesn't already exist.
        dirname = result[1]
        fullpath = curr_blob.fullpath + "/" + dirname
        if fullpath not in list(dict_blobs):
            dict_blobs[fullpath] = Blob("d", fullpath, curr_blob.fullpath)
        # We also want to denote that the directory is a child of the current blob.
        curr_blob.children.add(fullpath)
    else:
        # Otherwise we have a file with a file size.
        size = int(result[0])
        file = result[1]
        fullpath = curr_blob.fullpath + "/" + file
        if fullpath not in list(dict_blobs):
            dict_blobs[fullpath] = Blob("f", fullpath, curr_blob.fullpath)
        dict_blobs[fullpath].size = size
        # We also want to denote that the file is a child of the current blob.
        curr_blob.children.add(fullpath)

    return dict_blobs, curr_blob



def get_dict_blobs(lines):
    curr_blob = None
    dict_blobs = {}
    ls_mode = False
    for line in lines:
        if line.startswith("$ cd"):
            ls_mode = False
            dict_blobs, curr_blob = process_cd(line, dict_blobs, curr_blob)
        elif line.startswith("$ ls"):
            ls_mode = True
        elif ls_mode == True:
            dict_blobs, curr_blob = process_ls(line, dict_blobs, curr_blob)

    # Traverse the tree until we have all the directory sizes.
    queue = [k for k, v in dict_blobs.items() if v.size == -1]
    while len(queue) > 0:
        # Find a node whose children all have sizes.
        for q in queue:
            children = dict_blobs[q].children
            if all([dict_blobs[c].size != -1 for c in children]):
                # We can now compute the size of this node.
                dict_blobs[q].size = sum([dict_blobs[c].size for c in children])
                queue.remove(q)
                break

    return dict_blobs



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_blobs = get_dict_blobs(lines)
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

    # Same as above but we change a filename to be the same and with the same
    # depth to break uniqueness.
    filename = "input-test3.txt"
    assert solve(filename) == 95437


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
