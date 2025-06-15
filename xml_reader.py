import sys
import xml.etree.ElementTree as ET


def print_element(elem, indent=0):
    indent_str = '  ' * indent
    print(f"{indent_str}<{elem.tag}>")
    for key, value in elem.attrib.items():
        print(f"{indent_str}  @{key}={value}")
    if elem.text and elem.text.strip():
        text = elem.text.strip().replace('\n', '\n')
        print(f"{indent_str}  {text}")
    for child in elem:
        print_element(child, indent + 1)
    print(f"{indent_str}</{elem.tag}>")


def main():
    if len(sys.argv) != 2:
        print("Usage: python xml_reader.py <xml_file>")
        return
    xml_file = sys.argv[1]
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except Exception as e:
        print(f"Error reading {xml_file}: {e}")
        return
    print_element(root)


if __name__ == "__main__":
    main()

