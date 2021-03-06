from seq_predict.seq_repr import NormalRepr


# class WellKnownSequence(NormalRepr):
#     """ A class for well known sequences
#     Attributes:
#         familiarity: size of smallest part that is needed to recognize
#                      the sequence
#     """
#
#     def __init__(self, *args, familiarity=3, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.familiarity = familiarity

seq_list = [
    (NormalRepr([i**2 for i in range(1, 12)]), "square numbers"),
    (NormalRepr([i**3 for i in range(1, 7)]), "cubes"),
    (NormalRepr([2**i for i in range(0, 12)]), "powers of 2"),
    (NormalRepr([3**i for i in range(0, 8)]), "powers of 3"),
    (NormalRepr([4**i for i in range(0, 7)]), "powers of 4"),
    (NormalRepr([10**i for i in range(0, 5)]), "powers of 10"),
    (NormalRepr([2, 3, 5, 7, 11, 13, 17, 19, 23]), "prime numbers")
]

seq_list.extend([(seq.reversed_copy(), descr + " reversed")
                 for seq, descr in seq_list])

famous_sequences = [t[0] for t in seq_list]


def get_description(seq):
    for s, descr in seq_list:
        if s == seq:
            return descr

    return "no description"
