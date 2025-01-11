import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_eq_url_false(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.yahoo.com")
        self.assertNotEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("This is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        # arrange
        node = TextNode("This is a text node", TextType.TEXT)
        # act
        html_node = text_node_to_html_node(node)
        # assert
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.props, None)            
        self.assertEqual(html_node.value, "This is a text node")        
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_text_node_to_html_node_bold(self):
        # arrange
        node = TextNode("This is a text node", TextType.BOLD)
        # act
        html_node = text_node_to_html_node(node)
        # assert
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.props, None)            
        self.assertEqual(html_node.value, "This is a text node")        
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>")

    def test_text_node_to_html_node_italic(self):
        # arrange
        node = TextNode("This is a text node", TextType.ITALIC)
        # act
        html_node = text_node_to_html_node(node)
        # assert
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.props, None)            
        self.assertEqual(html_node.value, "This is a text node")        
        self.assertEqual(html_node.to_html(), "<i>This is a text node</i>")

    def test_text_node_to_html_node_code(self):
        # arrange
        node = TextNode("This is a text node", TextType.CODE)
        # act
        html_node = text_node_to_html_node(node)
        # assert
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.props, None)            
        self.assertEqual(html_node.value, "This is a text node")        
        self.assertEqual(html_node.to_html(), "<code>This is a text node</code>")

    def test_text_node_to_html_node_link(self):
        # arrange
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        # act
        html_node = text_node_to_html_node(node)
        # assert
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})            
        self.assertEqual(html_node.value, "This is a text node")        
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">This is a text node</a>')

    def test_text_node_to_html_node_image(self):
        # arrange
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.google.com")
        # act
        html_node = text_node_to_html_node(node)
        # assert
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.google.com", "alt": "This is a text node"})            
        self.assertEqual(html_node.value, "")        
        self.assertEqual(html_node.to_html(), '<img src="https://www.google.com" alt="This is a text node">')


if __name__ == "__main__":
    unittest.main()