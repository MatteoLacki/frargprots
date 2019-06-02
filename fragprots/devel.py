# task, easy fragmentation of a sequence
# aa2atom, but more refined.
# input: sequence, modifications
# output: formulas of fragments
%load_ext autoreload
%autoreload 2

from fragprots.charged_isomer import ChargedIsomer



q_iso = ChargedIsomer('C100H202', 3)
x = q_iso + q_iso
x + 'C100H200'
x + 'H'
x.q = 0
x
x.q = +1

ChargedIsomer(Formula('C100H202'), 3)

# this is the best ideas for qisomer.
qi.formula + 'H'


# formulas need to be hashable.
# and they should.
# I need immutable formulas.
# addition of two formulas should give new formula





from fragprots.amino_acids import amino_acids


AAs = {(aa, part): Counter(dict(atomcnt))
		for aa, atoms in amino_acids
		for part, atomcnt in atoms}

seq = 'AAAPAAAPAA'
r = Counter()
for aa in seq:

	r += AAs[aa]


strAAs[('A','N')]


# there should be no extra g in formulas
# but then, it will be difficult to find reactions: these g things can descibe the edges, actually.


# P0 ------(react a b)------ qIsomer
# P1 ------(react c d)----------|
# we could also make a reaction pathway?
# too complicated.
