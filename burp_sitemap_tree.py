import xml.etree.ElementTree as ET
from anytree import Node, RenderTree

def parse_burp_sitemap(sitemap_path):
    """Parses the Burp Suite XML sitemap and extracts URLs."""
    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    # Extract URLs from <item><url> elements
    urls = [item.find("url").text for item in root.findall("item")]

    return urls

def is_file(part):
    """Check if a URL part is a file based on common extensions."""
    return "." in part and "?" not in part  # Query parameters should not be treated as files

def build_tree(urls):
    """Builds a hierarchical tree structure from URLs, correctly styling PHP files."""
    root_node = Node("🌐 Root")
    nodes = {"": root_node}  # Dictionary to store nodes
    php_parents = set()  # Track PHP files that contain query parameters

    for url in urls:
        # Remove protocol and split into directory parts
        url_cleaned = url.replace("https://", "").replace("http://", "").rstrip("/")
        
        # Separate query parameters from path
        if "?" in url_cleaned:
            path_part, query_part = url_cleaned.split("?", 1)
        else:
            path_part, query_part = url_cleaned, None

        # Split path into directories/files
        parts = path_part.split("/")
        path = ""
        parent = root_node

        for i, part in enumerate(parts):
            # Assign icons
            if is_file(part):
                icon = "📄"  # Default to document emoji
            else:
                icon = "📂"  # Directories get folder emoji

            part_with_icon = f"{icon} {part}"
            path = f"{path}/{part}" if path else part

            # Ensure folders and files are not duplicated
            if path not in nodes:
                nodes[path] = Node(part_with_icon, parent=parent)

            parent = nodes[path]  # Update parent

        # If there are query parameters, nest them under the PHP file and mark it as a parent
        if query_part:
            php_parents.add(path)  # Mark PHP file as a parent
            queries = query_part.split("&")  # Handle multiple parameters
            for query in queries:
                Node(f"📜 {query}", parent=parent)

    # Update PHP files that have query parameters to ⚙️
    for php_parent in php_parents:
        if php_parent in nodes:
            nodes[php_parent].name = nodes[php_parent].name.replace("📄", "⚙️")  # Change emoji

    return root_node

def display_tree(tree_root):
    """Displays the tree structure and exports it to a text file."""
    output_lines = []
    for pre, _, node in RenderTree(tree_root):
        line = f"{pre}{node.name}"
        output_lines.append(line)
        print(line)  # Print to terminal

    # Export to a text file
    with open("sitemap_tree.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(output_lines))

    print("\n✅ Tree structure saved to 'sitemap_tree.txt'")

if __name__ == "__main__":
    sitemap_path = "sitemap.xml"  # Change to your actual sitemap path
    urls = parse_burp_sitemap(sitemap_path)

    if urls:
        tree_root = build_tree(urls)
        display_tree(tree_root)
    else:
        print("❌ No URLs found in the sitemap.")
