import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", None, {"class": "container"})
        self.assertEqual(node.props_to_html(), 'class="container"')

    def test_props_to_html_none(self):
        node = HTMLNode("div", "This is a div")
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_empty(self):
        node = HTMLNode("div", "This is a div", None, {})
        self.assertEqual(node.props_to_html(), '')

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph")
        self.assertEqual(node.to_html(), "This is a paragraph")

    def test_to_html_no_value(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()


class TestParentNode(unittest.TestCase):
    # simple parent with leaf children
    def test_to_html(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph")])
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p></div>")

    # parent with no children (should raise ValueError)
    def test_to_html_no_children(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    # parent with no tag (should raise ValueError)
    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "This is a paragraph")])
        with self.assertRaises(ValueError):
            node.to_html()

    # nested parents (parent containing parent)
    def test_to_html_nested(self):
        node = ParentNode("div", [ParentNode("div", [LeafNode("p", "This is a paragraph")])])
        self.assertEqual(node.to_html(), "<div><div><p>This is a paragraph</p></div></div>")

    # mixed children (parent containing leaf and parent)
    def test_to_html_mixed(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph"), ParentNode("div", [LeafNode("p", "This is a paragraph")])])
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p><div><p>This is a paragraph</p></div></div>")

    # parent with and without props
    def test_to_html_props(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph")], {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p>This is a paragraph</p></div>')

        node = ParentNode("div", [LeafNode("p", "This is a paragraph")])
        self.assertEqual(node.to_html(), '<div><p>This is a paragraph</p></div>')


if __name__ == "__main__":
    unittest.main()