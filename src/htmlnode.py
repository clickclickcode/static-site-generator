class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None or (not self.value and self.tag != "img"):
            raise ValueError("All leaf nodes must have a value")
        elif not self.tag:
            return self.value
        else:
            props_html = self.props_to_html()
            if self.tag == "img":
                return f"<{self.tag}{' ' + props_html if props_html else ''}>"
            else:
                return f"<{self.tag}{' ' + props_html if props_html else ''}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        elif not self.children:
            raise ValueError("All parent nodes must have children")
        else:
            #print(f"Props are: {self.props}") # Debugging
            props_html = self.props_to_html()
            #print(f"Props HTML is: {props_html}")  # Debug line
            result = f"<{self.tag}{' ' + props_html if props_html else ''}>"
            for node in self.children:
                result += node.to_html()
            return result + f"</{self.tag}>"
        
