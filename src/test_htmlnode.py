import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
)

class TestHTMLNode(unittest.TestCase):
    def test_to_html_prop(self):
        node = HTMLNode(
            "div",
            "This is a test!",
            None,
            {"href": "https://laviniadasani.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://laviniadasani.com" target="_blank"',
        )

    def test_leafnode(self):
        node = LeafNode(
            "p",
            "Hello, how are you?",
        )
        self.assertEqual(
            node.to_html(),
            "<p>Hello, how are you?</p>",
        )
    def test_leafnode_no_tag(self):
        node = LeafNode(
            None,
            "Have a good day!",
        )
        self.assertEqual(
            node.to_html(),
            "Have a good day!",
        )

    def test_parentnode_with_children(self):
        node = ParentNode("p", [LeafNode("b", "child")])
        self.assertEqual(node.to_html(), "<p><b>child</b></p>",)

    def test_parentnode_with_gradchildren(self):
        grandchild = LeafNode("i", "Nooooooo")
        child = ParentNode("span", [grandchild])
        node = ParentNode("h1", [child])
        self.assertEqual(
            node.to_html(),
            "<h1><span><i>Nooooooo</i></span></h1>",
        )
    def test_parentnode_with_more_children_and_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("h1", "This is a heading"),
                LeafNode("i", "Spooky text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://laviniadasani.com", "target": "_blank"},
        )
        self.assertEqual(
            node.to_html(),
            '<p href="https://laviniadasani.com" target="_blank"><h1>This is a heading</h1><i>Spooky text</i>Normal text</p>'
        )
    

if __name__ == "__main__":
    unittest.main()