import unittest

from functions import function_with_pass, function_with_return, function_with_return_none, passthrough, parameter_counter, passthrough_with_keywords, passthrough_with_positions, keyword_counter, argument_counter, name, joe


class TestFunctions(unittest.TestCase):

	def test_functions_with_pass(self):
		self.assertIsNone(function_with_pass())

	def test_functions_with_return(self):
		self.assertIsNone(function_with_return())

	def test_functions_with_return_none(self):
		self.assertIsNone(function_with_return_none())

	def test_passthrough(self):
		self.assertEqual(passthrough(False), False)
		self.assertEqual(passthrough(0), 0)
		self.assertEqual(passthrough('tim'), 'tim')
		self.assertEqual(passthrough(set((1, 2))) , {1, 2})
		self.assertEqual(
			passthrough(
				list(('tim', 'wande'))
			), 
			['tim', 'wande']
		)
		self.assertEqual(passthrough(dict(tim='tim')) , {'tim': 'tim'})
		self.assertEqual(passthrough(tuple((4, 5))) , (4, 5))
		self.assertEqual(passthrough(True) , True)

	def test_functions_with_unknown_number_of_parameters(self):
		self.assertEqual(parameter_counter(1, 2, 3), 3)
		self.assertEqual(parameter_counter(1, 2, 3, 4, 5), 5)

	def test_functions_with_positional_arguments(self):
		self.assertEqual(
			passthrough_with_positions('tim', 'elam'), 
			('tim', 'elam')
		)
		self.assertEqual(
			passthrough_with_positions('elam', 'tim'), 
			('tim', 'elam')
		)

	def test_functions_with_keyword_arguments(self):
		self.assertEqual(
			passthrough_with_keywords(
				first_name='tim', last_name='elam'
			),
			('tim', 'elam') 
		)
		self.assertEqual(
			passthrough_with_keywords(
				last_name='elam', first_name='tim', 
			),
			('tim', 'elam') 
		)

	def test_functions_with_unknown_number_of_keyword_arguments(self):
		self.assertEqual(
			keyword_counter(a=1, b=2, c=3, d=4), 4
		)
		self.assertEqual(
			keyword_counter(a=1, b=2), 2
		)

	def test_functions_with_unknown_number_of_positional_arguments_and_keyword_arguments(self):
		self.assertEqual(
			argument_counter(1, 2, 3, 4, a=5, b=6, c=7, d=8), 
			8
		)
		self.assertEqual(
			argument_counter(1, 2, c=7, d=8), 
			4
		)

	def test_singleton_function(self):
		self.assertEqual(name(), 'tim')

	def test_singleton_function_with_input(self):
		self.assertEqual(joe('Bob', 'James', 'Frank'), 'joe')

	def test_function_signatures(self):
		self.assertEqual(name(), 'tim')
