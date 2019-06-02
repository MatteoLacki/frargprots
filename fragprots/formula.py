import re

formula_patern = re.compile(r"([A-Z][a-z]?)(-?\d*)")


class NegativeAtomCount(Exception):
    pass

def str2dict(formula):
    """Represent a string chemical formula as a dictonay.
    
    Arguments:
        formula (str): A chemical formula, like 'C100H202' or 'CO2H'.
    """
    res = {}
    for el, cnt in re.findall(formula_patern, formula):
        cnt = int(cnt) if cnt else 1
        res[el] = res.get(el, 0) + cnt
    return res


def test_str2dict():
    assert str2dict('C100H202') == {'C':100, 'H':202}
    assert str2dict('COOH') == {'C':1, 'O':2, 'H':1}
    assert str2dict('C2O1H5(OH)') == {'C':2, 'O':2, 'H':6}


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
            super().__init__(((el, int(cnt)) if cnt else (el, 1)
                              for el, cnt in re.findall(formula_patern, formula)))
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
