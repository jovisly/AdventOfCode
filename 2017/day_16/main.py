# Problem type:
# ~~~~~~~~~~~~ follow instruction; find pattern ~~~~~~~~~~~~

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
line = lines[0]
instructions = line.split(",")
seq = "abcdefghijklmnop"
assert len(seq) == 15 + 1
# print(instructions[:10])
# 10000
# print(len(instructions))

# instructions = ["s1", "x3/4", "pe/b"]
# seq = "abcde"

def spin_once(seq):
    return seq[-1] + seq[:-1]

def do_spins(seq, n):
    for _ in range(n):
        seq = spin_once(seq)
    return seq

def do_swap(seq, id1, id2):
    i1 = min(id1, id2)
    i2 = max(id1, id2)
    return seq[:i1] + seq[i2] + seq[i1+1:i2] + seq[i1] + seq[i2+1:]


for inst in instructions:
    if inst.startswith("s"):
        n = int(inst[1:])
        seq = do_spins(seq, n)
    elif inst.startswith("x"):
        segs = inst[1:].split("/")
        id1, id2 = int(segs[0]), int(segs[1])
        seq = do_swap(seq, id1, id2)
    elif inst.startswith("p"):
        segs = inst[1:].split("/")
        s1, s2 = segs[0], segs[1]
        seq = do_swap(seq, seq.index(s1), seq.index(s2))
    else:
        raise ValueError(f"Unknown instruction: {inst}")
    # print("seq:", seq)

print("Part 1:", seq)


# My guess is that we don't want to do 1000000000 times so there must be some
# periodicity where we'd get the same pattern back. The instruction is 10000
# long, and the sequence is 16. Presumably there's something about the multiple
# of the two?
# Reset.
lines = open(filename, encoding="utf-8").read().splitlines()
line = lines[0]
instructions = line.split(",")
seq = "abcdefghijklmnop"
assert len(seq) == 15 + 1

maybe_cycle = len(seq) * len(instructions)

dict_cycle = {}
for i in range(60):
    for inst in instructions:
        if inst.startswith("s"):
            n = int(inst[1:])
            seq = do_spins(seq, n)
        elif inst.startswith("x"):
            segs = inst[1:].split("/")
            id1, id2 = int(segs[0]), int(segs[1])
            seq = do_swap(seq, id1, id2)
        elif inst.startswith("p"):
            segs = inst[1:].split("/")
            s1, s2 = segs[0], segs[1]
            seq = do_swap(seq, seq.index(s1), seq.index(s2))
        else:
            raise ValueError(f"Unknown instruction: {inst}")

    dict_cycle[i] = seq

# Ah indeed there's a period of 60.  so we just need to know what is 1B mod 60.
m = 1000000000 % 60
print("Part 2:", dict_cycle[m])
# hm it's not jlpkcngfbmiahdoe and not cbojdgnhkiepmlaf oh lol it's the one
# before ok.
"""
i and seq: 0 ociedpjbmfnkhlga
i and seq: 1 adeflockihgjmbnp
i and seq: 2 bcgnpijmafodhekl
i and seq: 3 gielanokhcjfmbpd
i and seq: 4 klfnjigeamcphdob
i and seq: 5 jaokdgihncbfmlpe
i and seq: 6 kbcdjonempglhfai
i and seq: 7 oaieckfjnhbdmpgl
i and seq: 8 gdcfljombpeahkni
i and seq: 9 clgepafjhiobmdkn
i and seq: 10 ieolagpfbmjchknd
i and seq: 11 efndpaghkiclmjob
i and seq: 12 onkpdbifmajchlge
i and seq: 13 edpalonckhgimfjb
i and seq: 14 fngjbkimeaodhpcl
i and seq: 15 gkplejochniamfbd
i and seq: 16 clajikgpemnbhdof
i and seq: 17 ieocdgkhjnfamlbp
i and seq: 18 cfndiojpmbglhaek
i and seq: 19 oekpncaijhfdmbgl
i and seq: 20 gdnaliomfbpehcjk
i and seq: 21 nlgpbeaihkofmdcj
i and seq: 22 kpolegbafminhcjd
i and seq: 23 pajdbeghcknlmiof
i and seq: 24 ojcbdfkameinhlgp
i and seq: 25 pdbelojnchgkmaif
i and seq: 26 ajgifckmpeodhbnl
i and seq: 27 gcblpionhjkemafd
i and seq: 28 nleikcgbpmjfhdoa
i and seq: 29 kpondgchijaemlfb
i and seq: 30 najdkoibmfglhepc
i and seq: 31 opcbjnekihadmfgl
i and seq: 32 gdjelkomafbphnic
i and seq: 33 jlgbfpekhcoamdni
i and seq: 34 cbolpgfeamkjhnid
i and seq: 35 beidfpghncjlmkoa
i and seq: 36 oinfdacempkjhlgb
i and seq: 37 bdfploijnhgcmeka
i and seq: 38 eigkancmbpodhfjl
i and seq: 39 gnflbkojhicpmead
i and seq: 40 jlpkcngfbmiahdoe
i and seq: 41 cbojdgnhkiepmlaf
i and seq: 42 jeidcokfmaglhpbn
i and seq: 43 obnfijpckhedmagl
i and seq: 44 gdiplcomeafbhjkn
i and seq: 45 ilgfabpchnoemdjk
i and seq: 46 nfolbgapemcihjkd
i and seq: 47 fpkdabghjnilmcoe
i and seq: 48 okjadenpmbcihlgf
i and seq: 49 fdablokijhgnmpce
i and seq: 50 pkgcejnmfbodhail
i and seq: 51 gjalfcoihknbmped
i and seq: 52 ilbcnjgafmkehdop
i and seq: 53 nfoidgjhckpbmlea
i and seq: 54 ipkdnocameglhbfj
i and seq: 55 ofjakibnchpdmegl
i and seq: 56 gdkblnompeafhicj
i and seq: 57 klgaefbnhjopmdic
i and seq: 58 jaolfgebpmnkhicd
i and seq: 59 abcdefghijklmnop
i and seq: 60 ociedpjbmfnkhlga
i and seq: 61 adeflockihgjmbnp
i and seq: 62 bcgnpijmafodhekl
i and seq: 63 gielanokhcjfmbpd
i and seq: 64 klfnjigeamcphdob
i and seq: 65 jaokdgihncbfmlpe
i and seq: 66 kbcdjonempglhfai
i and seq: 67 oaieckfjnhbdmpgl
i and seq: 68 gdcfljombpeahkni
i and seq: 69 clgepafjhiobmdkn
i and seq: 70 ieolagpfbmjchknd
i and seq: 71 efndpaghkiclmjob
i and seq: 72 onkpdbifmajchlge
i and seq: 73 edpalonckhgimfjb
i and seq: 74 fngjbkimeaodhpcl
i and seq: 75 gkplejochniamfbd
i and seq: 76 clajikgpemnbhdof
i and seq: 77 ieocdgkhjnfamlbp
i and seq: 78 cfndiojpmbglhaek
i and seq: 79 oekpncaijhfdmbgl
i and seq: 80 gdnaliomfbpehcjk
i and seq: 81 nlgpbeaihkofmdcj
i and seq: 82 kpolegbafminhcjd
i and seq: 83 pajdbeghcknlmiof
i and seq: 84 ojcbdfkameinhlgp
i and seq: 85 pdbelojnchgkmaif
i and seq: 86 ajgifckmpeodhbnl
i and seq: 87 gcblpionhjkemafd
i and seq: 88 nleikcgbpmjfhdoa
i and seq: 89 kpondgchijaemlfb
i and seq: 90 najdkoibmfglhepc
i and seq: 91 opcbjnekihadmfgl
i and seq: 92 gdjelkomafbphnic
i and seq: 93 jlgbfpekhcoamdni
i and seq: 94 cbolpgfeamkjhnid
i and seq: 95 beidfpghncjlmkoa
i and seq: 96 oinfdacempkjhlgb
i and seq: 97 bdfploijnhgcmeka
i and seq: 98 eigkancmbpodhfjl
i and seq: 99 gnflbkojhicpmead
i and seq: 100 jlpkcngfbmiahdoe
i and seq: 101 cbojdgnhkiepmlaf
i and seq: 102 jeidcokfmaglhpbn
i and seq: 103 obnfijpckhedmagl
i and seq: 104 gdiplcomeafbhjkn
i and seq: 105 ilgfabpchnoemdjk
i and seq: 106 nfolbgapemcihjkd
i and seq: 107 fpkdabghjnilmcoe
i and seq: 108 okjadenpmbcihlgf
i and seq: 109 fdablokijhgnmpce
i and seq: 110 pkgcejnmfbodhail
i and seq: 111 gjalfcoihknbmped
i and seq: 112 ilbcnjgafmkehdop
i and seq: 113 nfoidgjhckpbmlea
i and seq: 114 ipkdnocameglhbfj
i and seq: 115 ofjakibnchpdmegl
i and seq: 116 gdkblnompeafhicj
i and seq: 117 klgaefbnhjopmdic
i and seq: 118 jaolfgebpmnkhicd
i and seq: 119 abcdefghijklmnop
i and seq: 120 ociedpjbmfnkhlga
i and seq: 121 adeflockihgjmbnp
i and seq: 122 bcgnpijmafodhekl
i and seq: 123 gielanokhcjfmbpd
i and seq: 124 klfnjigeamcphdob
i and seq: 125 jaokdgihncbfmlpe
i and seq: 126 kbcdjonempglhfai
i and seq: 127 oaieckfjnhbdmpgl
i and seq: 128 gdcfljombpeahkni
i and seq: 129 clgepafjhiobmdkn
i and seq: 130 ieolagpfbmjchknd
i and seq: 131 efndpaghkiclmjob
i and seq: 132 onkpdbifmajchlge
i and seq: 133 edpalonckhgimfjb
i and seq: 134 fngjbkimeaodhpcl
i and seq: 135 gkplejochniamfbd
i and seq: 136 clajikgpemnbhdof
i and seq: 137 ieocdgkhjnfamlbp
i and seq: 138 cfndiojpmbglhaek
i and seq: 139 oekpncaijhfdmbgl
i and seq: 140 gdnaliomfbpehcjk
i and seq: 141 nlgpbeaihkofmdcj
i and seq: 142 kpolegbafminhcjd
i and seq: 143 pajdbeghcknlmiof
i and seq: 144 ojcbdfkameinhlgp
i and seq: 145 pdbelojnchgkmaif
i and seq: 146 ajgifckmpeodhbnl
i and seq: 147 gcblpionhjkemafd
i and seq: 148 nleikcgbpmjfhdoa
i and seq: 149 kpondgchijaemlfb
i and seq: 150 najdkoibmfglhepc
i and seq: 151 opcbjnekihadmfgl
i and seq: 152 gdjelkomafbphnic
i and seq: 153 jlgbfpekhcoamdni
i and seq: 154 cbolpgfeamkjhnid
i and seq: 155 beidfpghncjlmkoa
i and seq: 156 oinfdacempkjhlgb
i and seq: 157 bdfploijnhgcmeka
i and seq: 158 eigkancmbpodhfjl
i and seq: 159 gnflbkojhicpmead
i and seq: 160 jlpkcngfbmiahdoe
i and seq: 161 cbojdgnhkiepmlaf
i and seq: 162 jeidcokfmaglhpbn
i and seq: 163 obnfijpckhedmagl
i and seq: 164 gdiplcomeafbhjkn
i and seq: 165 ilgfabpchnoemdjk
i and seq: 166 nfolbgapemcihjkd
i and seq: 167 fpkdabghjnilmcoe
i and seq: 168 okjadenpmbcihlgf
i and seq: 169 fdablokijhgnmpce
i and seq: 170 pkgcejnmfbodhail
i and seq: 171 gjalfcoihknbmped
i and seq: 172 ilbcnjgafmkehdop
i and seq: 173 nfoidgjhckpbmlea
i and seq: 174 ipkdnocameglhbfj
i and seq: 175 ofjakibnchpdmegl
i and seq: 176 gdkblnompeafhicj
i and seq: 177 klgaefbnhjopmdic
i and seq: 178 jaolfgebpmnkhicd
i and seq: 179 abcdefghijklmnop
i and seq: 180 ociedpjbmfnkhlga
i and seq: 181 adeflockihgjmbnp
i and seq: 182 bcgnpijmafodhekl
i and seq: 183 gielanokhcjfmbpd
i and seq: 184 klfnjigeamcphdob
i and seq: 185 jaokdgihncbfmlpe
i and seq: 186 kbcdjonempglhfai
i and seq: 187 oaieckfjnhbdmpgl
i and seq: 188 gdcfljombpeahkni
i and seq: 189 clgepafjhiobmdkn
i and seq: 190 ieolagpfbmjchknd
i and seq: 191 efndpaghkiclmjob
i and seq: 192 onkpdbifmajchlge
i and seq: 193 edpalonckhgimfjb
i and seq: 194 fngjbkimeaodhpcl
i and seq: 195 gkplejochniamfbd
i and seq: 196 clajikgpemnbhdof
i and seq: 197 ieocdgkhjnfamlbp
i and seq: 198 cfndiojpmbglhaek
i and seq: 199 oekpncaijhfdmbgl
i and seq: 200 gdnaliomfbpehcjk
i and seq: 201 nlgpbeaihkofmdcj
i and seq: 202 kpolegbafminhcjd
i and seq: 203 pajdbeghcknlmiof
i and seq: 204 ojcbdfkameinhlgp
i and seq: 205 pdbelojnchgkmaif
i and seq: 206 ajgifckmpeodhbnl
i and seq: 207 gcblpionhjkemafd
i and seq: 208 nleikcgbpmjfhdoa
i and seq: 209 kpondgchijaemlfb
i and seq: 210 najdkoibmfglhepc
i and seq: 211 opcbjnekihadmfgl
i and seq: 212 gdjelkomafbphnic
i and seq: 213 jlgbfpekhcoamdni
i and seq: 214 cbolpgfeamkjhnid
i and seq: 215 beidfpghncjlmkoa
i and seq: 216 oinfdacempkjhlgb
i and seq: 217 bdfploijnhgcmeka
i and seq: 218 eigkancmbpodhfjl
i and seq: 219 gnflbkojhicpmead
i and seq: 220 jlpkcngfbmiahdoe
i and seq: 221 cbojdgnhkiepmlaf
i and seq: 222 jeidcokfmaglhpbn
i and seq: 223 obnfijpckhedmagl
i and seq: 224 gdiplcomeafbhjkn
i and seq: 225 ilgfabpchnoemdjk
i and seq: 226 nfolbgapemcihjkd
i and seq: 227 fpkdabghjnilmcoe
i and seq: 228 okjadenpmbcihlgf
i and seq: 229 fdablokijhgnmpce
i and seq: 230 pkgcejnmfbodhail
i and seq: 231 gjalfcoihknbmped
i and seq: 232 ilbcnjgafmkehdop
i and seq: 233 nfoidgjhckpbmlea
i and seq: 234 ipkdnocameglhbfj
i and seq: 235 ofjakibnchpdmegl
i and seq: 236 gdkblnompeafhicj
i and seq: 237 klgaefbnhjopmdic
i and seq: 238 jaolfgebpmnkhicd
i and seq: 239 abcdefghijklmnop
i and seq: 240 ociedpjbmfnkhlga
i and seq: 241 adeflockihgjmbnp
i and seq: 242 bcgnpijmafodhekl
i and seq: 243 gielanokhcjfmbpd
i and seq: 244 klfnjigeamcphdob
i and seq: 245 jaokdgihncbfmlpe
i and seq: 246 kbcdjonempglhfai
i and seq: 247 oaieckfjnhbdmpgl
i and seq: 248 gdcfljombpeahkni
i and seq: 249 clgepafjhiobmdkn
i and seq: 250 ieolagpfbmjchknd
i and seq: 251 efndpaghkiclmjob
i and seq: 252 onkpdbifmajchlge
i and seq: 253 edpalonckhgimfjb
i and seq: 254 fngjbkimeaodhpcl
i and seq: 255 gkplejochniamfbd
i and seq: 256 clajikgpemnbhdof
i and seq: 257 ieocdgkhjnfamlbp
i and seq: 258 cfndiojpmbglhaek
i and seq: 259 oekpncaijhfdmbgl
i and seq: 260 gdnaliomfbpehcjk
i and seq: 261 nlgpbeaihkofmdcj
i and seq: 262 kpolegbafminhcjd
i and seq: 263 pajdbeghcknlmiof
i and seq: 264 ojcbdfkameinhlgp
i and seq: 265 pdbelojnchgkmaif
i and seq: 266 ajgifckmpeodhbnl
i and seq: 267 gcblpionhjkemafd
i and seq: 268 nleikcgbpmjfhdoa
i and seq: 269 kpondgchijaemlfb
i and seq: 270 najdkoibmfglhepc
i and seq: 271 opcbjnekihadmfgl
i and seq: 272 gdjelkomafbphnic
i and seq: 273 jlgbfpekhcoamdni
i and seq: 274 cbolpgfeamkjhnid
i and seq: 275 beidfpghncjlmkoa
i and seq: 276 oinfdacempkjhlgb
i and seq: 277 bdfploijnhgcmeka
i and seq: 278 eigkancmbpodhfjl
i and seq: 279 gnflbkojhicpmead
"""
