
class Blob:
    def __init__(self, type, name, parent):
        # A blob can be a directory ("d") or a file ("f").
        self.type = type
        self.name = name
        self.parent = parent
        # Children are also blobs.
        self.children = set()
        self.size = -1



def process_cd(line, dict_blobs, curr_blob):
    command = line[2:].split(" ")
    dest = command[1]
    # if curr_blob is not None:
    #     print("curr")
    #     print(curr_blob.__dict__)
    if dest == "..":
        # cd .. when we are already at root does nothing.
        # if curr_blob.parent is not None:
        curr_blob = dict_blobs[curr_blob.parent]
    else:
        if dest in list(dict_blobs):
            curr_blob = dict_blobs[dest]
        else:
            if dest == "fqg":
                print("======= WHAT IS GOING ON =======")
                print(curr_blob.__dict__)
                print(line)
            parent = None if dest == "/" else curr_blob.name
            curr_blob = Blob("d", dest, parent)
            dict_blobs[dest] = curr_blob

    return dict_blobs, curr_blob



def process_ls(line, dict_blobs, curr_blob):
    result = line.split(" ")
    if result[0] == "dir":
        # Add a directory if it doesn't already exist.
        dirname = result[1]
        if dirname not in list(dict_blobs):
            if dirname == "fqg":
                print("======= WHAT IS GOING ON =======")
                print(curr_blob.__dict__)
                print(line)
                print("~~~~~~~")

            dict_blobs[dirname] = Blob("d", dirname, curr_blob.name)
        # We also want to denote that the directory is a child of the current blob.
        curr_blob.children.add(dirname)
    else:
        # Otherwise we have a file with a file size.
        size = int(result[0])
        file = result[1]
        if file not in list(dict_blobs):
            dict_blobs[file] = Blob("f", file, curr_blob.name)
        dict_blobs[file].size = size
        # We also want to denote that the file is a child of the current blob.
        curr_blob.children.add(file)

    return dict_blobs, curr_blob


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()

    curr_blob = None
    dict_blobs = {}
    ls_mode = False
    for line in lines:
        # print("-" * 40)
        # print(line)
        if line.startswith("$ cd"):
            ls_mode = False
            dict_blobs, curr_blob = process_cd(line, dict_blobs, curr_blob)
        elif line.startswith("$ ls"):
            ls_mode = True
        elif ls_mode == True:
            dict_blobs, curr_blob = process_ls(line, dict_blobs, curr_blob)


    # Traverse the tree until we have all the directory sizes.
    queue = [v.name for v in dict_blobs.values() if v.size == -1]
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


if __name__ == "__main__":
    # mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
    # 551163 is too low.
