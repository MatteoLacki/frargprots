import re

from .formula import Formula, dict2str
# TODO: maybe also make it possible to accept "HNO-" and such things.

class ChargedIsomer(Formula):
	"""A class representing a charged isomer."""
	def __init__(self, formula="", q=0):
		super().__init__(formula)
		try:
			self.q = formula.q
		except AttributeError:
			try:
				self.q = int(formula.split("^")[1])
			except IndexError:
				self.q = q
			except AttributeError: # no .split() method
				self.q = q

	def __hash__(self):
		return hash( (dict2str(self), self.q) )

	def __str__(self):
		res = super().__str__()
		if self.q > 0:
			res += "^+{}".format(self.q)
		if self.q < 0:
			res += "^{}".format(self.q)
		return res

	def __add__(self, formula):
		out = super().__add__(formula)
		out.q = self.q
		try:
			out.q += formula.q
		except AttributeError:
			pass
		return out


def test_charged_isomers():
	q_iso = ChargedIsomer('C100H202', 3)
	assert str(q_iso + q_iso) == 'C200H404^+6'
	assert q_iso + "H^+1" == 'C100H202^+4'