import re


# Maybe this pattern should be more general, to encompass chemical diffs?
# Or maybe there shouldn't be any chemical diffs?
# Or keep chemical diffs only as strings and make it impossible to accept anything like that?
formula_patern = re.compile(r"([A-Z][a-z]?)(-?\d*)")
#TODO: add support for CH things.

# formula = 'C100H200Mg'
# ?re.findall
# for el, cnt in re.findall(formula_patern, formula):
#     print(el, int(cnt))


class NegativeAtomCount(Exception):
    pass

def str2dict(formula):
    return {el: int(cnt) for el, cnt in re.findall(formula_patern, formula)}

def dict2str(formula):
    return "".join(el + str(cnt) for el, cnt in sorted(formula.items()))


class Formula(dict):
    """Represent a chemical formula."""
    def __init__(self, formula=""):
        """Initialize the formula.

        Parameters
        ==========
        formula : str or dict
            A string, or a dict-like object, e.g. 'C100H202'.
            specifying the chemical formula, e.g. "{'C':100, 'H':202}".
        """
        # only string needs to be sorted.
        if isinstance(formula, str):
            super().__init__(((el,int(cnt)) for el, cnt in re.findall(formula_patern, formula)))
        else: # copy constructor
            super().__init__(((f, int(formula[f])) for f in formula))

    def __str__(self):
        return dict2str(self)

    def __hash__(self):
        return hash(dict2str(self))

    def __repr__(self):
        return self.__str__()

    def __add__(self, formula):
        out = self.__class__(formula)
        for el, cnt in self.items():
            atomcnt = out.get(el, 0) + cnt
            if atomcnt == 0:
                del out[el]
            else:
                if not atomcnt > 0:
                    raise NegativeAtomCount
                out[el] = atomcnt
        return out


def test_formula():
    f = Formula('W100C100H200')
    assert str(f) == "C100H200W100"
    assert str(f+f) == "C200H400W200"
    assert str(f+"Mg10") == "C100H200Mg10W100"
    #immutability?
    x = {'C':100}
    y = Formula(x)
    assert id(x) != id(y)
    x['C'] = 13
    assert y['C'] == 100
    z = Formula(y)
    y['C'] = 11
    assert z['C'] == 100

#TODO: Move this to aa2atom?
