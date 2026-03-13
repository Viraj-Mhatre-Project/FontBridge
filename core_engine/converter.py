import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MAPPING_PATH = BASE_DIR / "docs" / "shivaji_mapping.json"

with open(MAPPING_PATH, "r", encoding="utf-8") as f:
    mapping_data = json.load(f)

consonants = mapping_data["consonants"]
vowels = mapping_data["vowels"]
matras = mapping_data["matras"]
special = mapping_data["special_characters"]

lookup = {}
lookup.update(consonants)
lookup.update(vowels)
lookup.update(matras)
lookup.update(special)


def convert_text(text: str) -> str:
    result = ""
    for char in text:
        if char in lookup:
            result += lookup[char]
        else:
            result += char
    return result


if __name__ == "__main__":
    print("FontBridge Shivaji Converter")
    text = input("Enter Shivaji encoded text: ")
    converted = convert_text(text)
    print("\nConverted Unicode Text:")
    print(converted)

with open("test_output.txt", "w", encoding="utf-8") as f:
    f.write(converted)