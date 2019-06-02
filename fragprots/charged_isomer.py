from .formula import Formula, dict2str


class ChargedIsomer(Formula):
	"""A class representing a charged isomer."""
	def __init__(self, formula="", q=0):
		super().__init__(formula)
		try:
			self.q = formula.q
		except AttributeError:
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
