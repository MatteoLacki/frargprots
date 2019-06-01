# task, easy fragmentation of a sequence
# aa2atom, but more refined.
# input: sequence, modifications
# output: formulas of fragments
%load_ext autoreload
%autoreload 2

from collections import Counter, namedtuple, frozendict
??namedtuple

import re



formula = "H200C100"
formula_patern = re.compile('([A-Z][a-z]?)([0-9]*)')


a = {'C':1, 'H':2}
b = {'H':2, 'C':1}
for i in a:
	print(i)

from fragprots.ptms import ptms
f + ptms["phosphorylation"]


def add(a, b):

%%timeit
x = list(re.findall(formula_patern, formula))

{


# this is the best ideas for qisomer.
qIsomer = namedtuple("qIsomer", ["q", "formula"])
qi = qIsomer(10, Counter({'C':1, 'H':2}))



# formulas need to be hashable.
# and they should.
# I need immutable formulas.
# addition of two formulas should give new formula


id(qi)
qi.formula['C']
qi.formula[1]



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
