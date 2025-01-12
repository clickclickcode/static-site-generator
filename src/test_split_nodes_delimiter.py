import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        # Test with text after delimiter
        node = TextNode("hello **world** today", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[2].text, " today")

    def test_split_nodes_delimiter_no_text_after(self):
        # Test with no text after delimiter
        node = TextNode("hello **world**", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "hello ")
        self.assertEqual(nodes[1].text, "world")

    def test_split_nodes_delimiter_no_text_before(self):
        # Test with no text before delimiter
        node = TextNode("**world** today", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "world")
        self.assertEqual(nodes[1].text, " today")

    def test_split_nodes_delimiter_no_text_before_or_after(self):
        # Test with no text before or after delimiter
        node = TextNode("**world**", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "world")

    def test_split_nodes_delimiter_no_delimiter(self):
        # Test with no delimiter
        node = TextNode("hello world", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "hello world")

    def test_split_nodes_delimiter_multiple_delimiters(self):
        # Test with multiple delimiters
        node = TextNode("hello **world** today **is** a good day", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[2].text, " today ")
        self.assertEqual(nodes[3].text, "is")
        self.assertEqual(nodes[4].text, " a good day")

    def test_split_nodes_delimiter_nested_delimiters(self):
        # Test with nested delimiters
        node = TextNode("hello **world _today_ is** a good day", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "hello ")
        self.assertEqual(nodes[1].text, "world _today_ is")
        self.assertEqual(nodes[2].text, " a good day")
    
    def test_split_nodes_delimiter_nested_delimiters_reverse(self):
        # Test with nested delimiters
        node = TextNode("hello **world _today_ is** a good day", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "hello **world ")
        self.assertEqual(nodes[1].text, "today")
        self.assertEqual(nodes[2].text, " is** a good day")

    def test_split_nodes_delimiter_unmatched(self):
        node = TextNode("hello **world", TextType.TEXT)
        # This should raise an exception
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_split_nodes_delimiter_non_text_node(self):
        node = TextNode("**already bold**", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        # Should return unchanged
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "**already bold**")