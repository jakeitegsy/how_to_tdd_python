class TruthTable:
	pass

	def logical_true(self, x):
		return True

	def logical_negation(self, x):
		return not x

	def logical_identity(self, x):
		return x

	def logical_false(self, x):
		return False

	def tautology(self, x, y):
		return True

	def project_second(self, x, y):
		return y

	def project_first(self, x, y):
		return x

	def negation_two(self, x, y):
		return not y

	def negation(self, x, y):
		return not x

	def material_nonimplication(self, x, y):
		return x and (not y)

	def logical_nor(self, x, y):
		return not (x or y)

	def logical_nand(self, x, y):
		return not (x and y)

	def logical_implication(self, x, y):
		return not (x and (not y))

	def logical_equality(self, x, y):
		return x==y

	def logical_disjunction(self, x, y):
		return x or y

	def logical_conjunction(self, x, y):
		return x and y

	def exclusive_disjunction(self, x, y):
		return x and (not y) or (not x) and y

	def converse_nonimplication(self, x, y):
		return (not x) and y

	def converse_implication(self, x, y):
		return not (y and (not x))

	def contradiction(self, x, y):
		return False
