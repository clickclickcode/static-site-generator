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