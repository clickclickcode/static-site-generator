from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        first_delimiter = node.text.find(delimiter)
        second_delimiter = node.text.find(delimiter, first_delimiter + 1)

        if first_delimiter == -1:
            new_nodes.append(node)
            continue
        
        if second_delimiter == -1:
            raise Exception('That is invalid markdown syntax')
        
        before_delimiter = node.text[:first_delimiter]
        between_delimiters = node.text[first_delimiter + len(delimiter):second_delimiter]
        after_delimiter = node.text[second_delimiter + len(delimiter):]
        
        if before_delimiter:
            new_nodes.append(TextNode(before_delimiter, TextType.TEXT))
        
        if between_delimiters:
            new_nodes.append(TextNode(between_delimiters, text_type))

        if after_delimiter:
            remaining_node = TextNode(after_delimiter, TextType.TEXT)
            remaining_nodes = split_nodes_delimiter([remaining_node], delimiter, text_type)
            new_nodes.extend(remaining_nodes)

    return new_nodes
