import numpy as np


def viz_mat(list_rows):
    """Vizualize matrix."""
    for row in list_rows:
        print("".join(row))



def get_list_rows(raw_lines):
    return [list(line) for line in raw_lines]



def get_seq_from_list(list_rows):
    segs = ["".join(row) for row in list_rows]
    return "/".join(segs)



def get_list_from_seq(seq):
    return [list(s) for s in seq.split("/")]



def get_variants(seq):
    list_rows = get_list_from_seq(seq)
    all_seqs = {seq}

    # 1. 90 Degrees Clockwise Rotation:
    variant = np.rot90(list_rows, -1).tolist()
    all_seqs.add(get_seq_from_list(variant))

    # 2. 180 Degrees Clockwise Rotation:
    variant = np.rot90(list_rows, -2).tolist()
    all_seqs.add(get_seq_from_list(variant))

    # 3. 270 Degrees Clockwise Rotation:
    variant = np.rot90(list_rows, -3).tolist()
    all_seqs.add(get_seq_from_list(variant))

    # 4. Vertical Flip:
    variant = np.flip(list_rows, 0).tolist()
    all_seqs.add(get_seq_from_list(variant))

    # 5. Horizontal Flip:
    variant = np.flip(list_rows, 1).tolist()
    all_seqs.add(get_seq_from_list(variant))

    # 6. Flip vertically then rotate 90 degrees clockwise:
    variant = np.rot90(np.flip(list_rows, 0), -1).tolist()
    all_seqs.add(get_seq_from_list(variant))

    # 7. Flip horizontally then rotate 90 degrees clockwise
    variant = np.rot90(np.flip(list_rows, 1), -1).tolist()
    all_seqs.add(get_seq_from_list(variant))
    return list(all_seqs)


def split_into_2x2(list_rows):
    assert len(list_rows) % 2 == 0
    assert len(list_rows[0]) % 2 == 0
    dim = len(list_rows)
    np_rows = np.array(list_rows)

    return np.vstack(
        [np.hsplit(row, dim//2) for row in np.vsplit(np_rows, dim//2)]
    ).reshape(-1,2,2).tolist()


def split_into_3x3(list_rows):
    assert len(list_rows) % 3 == 0
    assert len(list_rows[0]) % 3 == 0
    dim = len(list_rows)
    np_rows = np.array(list_rows)

    return np.vstack(
        [np.hsplit(row, dim//3) for row in np.vsplit(np_rows, dim//3)]
    ).reshape(-1,3,3).tolist()


def make_big_m(list_m):
    size = int(np.sqrt(len(list_m)))

    # Reshape list in "blocks"
    reshaped_list = [list_m[i:i+size] for i in range(0,len(list_m),size)]

    # Stack arrays horizontally and vertically
    big_m = np.vstack([np.hstack(blocks) for blocks in reshaped_list])

    return big_m.tolist()



def get_rules(is_test=False):
    if is_test is True:
        filename = "input-test.txt"
    else:
        filename = "input.txt"

    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_rules = {}
    for line in lines:
        segs = line.split(" => ")
        input_mat = segs[0]
        output_mat = segs[1]
        all_input_mats = get_variants(input_mat)
        for mat in all_input_mats:
            dict_rules[mat] = output_mat
    return dict_rules


def enhance(list_rows, dict_rules):
    if len(list_rows) % 2 == 0:
        # Break into 2x2.
        outs = split_into_2x2(list_rows)
    else:
        # Break into 3x3.
        outs = split_into_3x3(list_rows)

    # Enhance.
    list_enhanced = []
    for out in outs:
        # Enhance.
        seq = get_seq_from_list(out)
        list_enhanced.append(get_list_from_seq(dict_rules[seq]))

    # Combine into big mat.
    return make_big_m(list_enhanced)




"""
'.#./..#/###' does not have a match...
"""
# out = get_rules(True)
# print(out)

# exit()
# raw_lines = """\
# .#..
# ..#.
# ###.
# ..##
# """.splitlines()

# list_rows = get_list_rows(raw_lines)
# # print(list_rows)

# seq = get_seq_from_list(list_rows)
# # print(seq)

# list_rows = get_list_from_seq(seq)
# # print(list_rows)

# out = get_variants(seq)
# print(out)

# viz_mat(list_rows)

# outs = split_into_2x2(list_rows)
# print(outs)

# raw_lines = """\
# .#..##
# ..#...
# ###..#
# ..###.
# ...###
# ###...
# """.splitlines()
# list_rows = get_list_rows(raw_lines)
# outs = split_into_3x3(list_rows)
# print(outs)
# print(len(outs))

# big_m = make_big_m(outs)
# print("*" * 20)
# print(big_m)
# print("=" * 20)
# viz_mat(big_m)

