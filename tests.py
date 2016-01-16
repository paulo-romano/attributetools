# coding: utf-8
from unittest import TestCase
from attributetools import attribute, set_attributes


class AttributeTest(TestCase):
    def test_set_attribute(self):
        """Should set a attribute to a function"""
        def f(): pass
        set_attributes(f, foo=1)

        self.assertEqual(1, f.foo)

    def test_set_by_decoration(self):
        """Should work by decoration too"""
        @attribute(foo='bar')
        def f(): pass

        self.assertEqual('bar', f.foo)

    def test_set_by_decoration_more_then_1(self):
        """Should work by decoration too"""
        attribs = dict(foo='bar', hue='br', intbar=1, floatfoo=1.5)

        @attribute(**attribs)
        def f(): pass

        for key in attribs:
            with self.subTest():
                self.assertEqual(attribs[key], f.__getattribute__(key))

