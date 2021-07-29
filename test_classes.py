import unittest

from classes import ClassWithPass, ClassWithParentheses, ClassWithObject, ClassWithAttributes, ClassWithMethods, ClassWithAttributesAndMethods, Tim, Wande, Micah, Lucas, Peter, Daniel, David, Joel, Elam, Boy, Girl, Other


class TestClasses(unittest.TestCase):

	def test_class_definitions_with_pass(self):
		self.assertIsInstance(ClassWithPass(), object)

	def test_class_definitions_with_parentheses(self):
		self.assertIsInstance(ClassWithParentheses(), object)

	def test_class_definition_with_object(self):
		self.assertIsInstance(ClassWithObject(), object)

	def test_classes_with_attributes(self):
		self.assertEqual(
			ClassWithAttributes.attribute_a, 'AttributeA'
		)
		self.assertEqual(
			ClassWithAttributes.attribute_b, 'AttributeB'
		)
		self.assertEqual(
			ClassWithAttributes.attribute_c, 'AttributeC'
		)
		self.assertEqual(
			ClassWithAttributes.attribute_d, 'AttributeD'
		)

	def test_classes_with_methods(self):
		self.assertEqual(
			ClassWithMethods.method_a(), 'MethodA'
		)
		self.assertEqual(
			ClassWithMethods.method_b(), 'MethodB'
		)
		self.assertEqual(
			ClassWithMethods.method_c(), 'MethodC'
		)
		self.assertEqual(
			ClassWithMethods.method_d(), 'MethodD'
		)

	def test_classes_with_attributes_and_methods(self):
		self.assertEqual(
			ClassWithAttributesAndMethods.attribute, 
			'Attribute'
		)
		self.assertEqual(
			ClassWithAttributesAndMethods.method(), 'Method'
		)

	def test_classes_with_initializers(self):
		self.assertEqual(Boy().sex, 'M')
		self.assertEqual(Girl(sex='F').sex, 'F')
		self.assertEqual(Other(sex='?').sex, '?')

	def test_tim_knows_classes(self):
		self.assertEqual(Tim().last_name, 'elam')
		self.assertEqual(Wande().last_name, 'elam')
		self.assertEqual(Micah().last_name, 'elam')
		self.assertEqual(Lucas().last_name, 'elam')
		self.assertEqual(Peter().last_name, 'elam')
		self.assertEqual(Daniel().last_name, 'elam')
		self.assertEqual(David().last_name, 'elam')
		self.assertEqual(Joel().last_name, 'elam')

		self.assertEqual(Tim().first_name, 'tim')
		self.assertEqual(Wande().first_name, 'wande')
		self.assertEqual(Micah().first_name, 'micah')
		self.assertEqual(Lucas().first_name, 'lucas')
		self.assertEqual(Peter().first_name, 'peter')
		self.assertEqual(Daniel().first_name, 'daniel')
		self.assertEqual(David().first_name, 'david')
		self.assertEqual(Joel().first_name, 'joel')

		self.assertEqual(Tim().sex, 'M')
		self.assertEqual(Wande().sex, 'F')
		self.assertEqual(Micah().sex, 'M')
		self.assertEqual(Lucas().sex, 'M')
		self.assertEqual(Peter().sex, 'M')
		self.assertEqual(Daniel().sex, 'M')
		self.assertEqual(David().sex, 'M')
		self.assertEqual(Joel().sex, 'M')

		self.assertEqual(Tim().year_of_birth, 1986)
		self.assertEqual(Wande().year_of_birth, 1983)
		self.assertEqual(Micah().year_of_birth, 2014)
		self.assertEqual(Lucas().year_of_birth, 2017)
		self.assertEqual(Peter().year_of_birth, 1978)
		self.assertEqual(Daniel().year_of_birth, 1980)
		self.assertEqual(David().year_of_birth, 1983)
		self.assertEqual(Joel().year_of_birth, 1990)

		self.assertEqual(Tim().age(), 35)
		self.assertEqual(Wande().age(), 38)
		self.assertEqual(Micah().age(), 7)
		self.assertEqual(Lucas().age(), 4)
		self.assertEqual(Peter().age(), 43)
		self.assertEqual(Daniel().age(), 41)
		self.assertEqual(David().age(), 38)
		self.assertEqual(Joel().age(), 31)

		self.assertEqual(Tim().is_minor(), False)
		self.assertEqual(Wande().is_minor(), False)
		self.assertEqual(Micah().is_minor(), True)
		self.assertEqual(Lucas().is_minor(), True)
		self.assertEqual(Peter().is_minor(), False)
		self.assertEqual(Daniel().is_minor(), False)
		self.assertEqual(David().is_minor(), False)
		self.assertEqual(Joel().is_minor(), False)

	@unittest.skip
	def test_listing_class_attributes(self):
		self.assertEqual(
			dir(Elam), 
			[
				'__class__',
				'__delattr__',
				'__dict__',
				'__dir__',
				'__doc__',
				'__eq__',
				'__format__',
				'__ge__',
				'__getattribute__',
				'__gt__',
				'__hash__',
				'__init__',
				'__init_subclass__',
				'__le__',
				'__lt__',
				'__module__',
				'__ne__',
				'__new__',
				'__reduce__',
				'__reduce_ex__',
				'__repr__',
				'__setattr__',
				'__sizeof__',
				'__str__',
				'__subclasshook__',
				'__weakref__',
				'age',
				'is_minor',
				'last_name',
				'sex'
			]
		)
