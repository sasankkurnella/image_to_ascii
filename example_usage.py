#!/usr/bin/env python3
"""
Example usage of ASCIIConverter class for programmatic use.
"""

from ascii_converter import ASCIIConverter, save_ascii_art


def example_basic():
    """Basic conversion example."""
    print("=== Basic Conversion ===\n")
    converter = ASCIIConverter(char_set="detailed")
    ascii_art = converter.convert("sample.jpg", width=80)
    if ascii_art:
        print(ascii_art)


def example_different_styles():
    """Convert same image with different character sets."""
    print("\n=== Different Styles ===\n")
    
    styles = ["detailed", "simple", "blocks"]
    
    for style in styles:
        print(f"\n--- {style.upper()} Style ---")
        converter = ASCIIConverter(char_set=style)
        ascii_art = converter.convert("sample.jpg", width=60)
        if ascii_art:
            print(ascii_art[:300] + "...")  # Print first 300 chars


def example_save_to_file():
    """Convert and save to file."""
    print("\n=== Saving to File ===\n")
    converter = ASCIIConverter(char_set="blocks")
    ascii_art = converter.convert("sample.jpg", width=100)
    if ascii_art:
        save_ascii_art(ascii_art, "output_example.txt")


def example_custom_charset():
    """Use custom character set."""
    print("\n=== Custom Character Set ===\n")
    custom_chars = "█▓▒░ .:-=+*#%@"
    converter = ASCIIConverter(char_set=custom_chars)
    ascii_art = converter.convert("sample.jpg", width=70)
    if ascii_art:
        print(ascii_art)


def example_inverted():
    """Convert with inverted brightness."""
    print("\n=== Inverted Brightness ===\n")
    converter = ASCIIConverter(char_set="detailed")
    ascii_art = converter.convert("sample.jpg", width=80, invert=True)
    if ascii_art:
        print(ascii_art)


def batch_convert():
    """Convert multiple images."""
    print("\n=== Batch Conversion ===\n")
    
    images = ["image1.jpg", "image2.png", "image3.gif"]
    converter = ASCIIConverter(char_set="detailed")
    
    for img in images:
        print(f"\nConverting {img}...")
        ascii_art = converter.convert(img, width=100)
        if ascii_art:
            output_name = f"ascii_{img.rsplit('.', 1)[0]}.txt"
            save_ascii_art(ascii_art, output_name)


if __name__ == "__main__":
    # Run examples (comment out the ones you don't need)
    
    # example_basic()
    # example_different_styles()
    # example_save_to_file()
    # example_custom_charset()
    # example_inverted()
    # batch_convert()
    
    print("\nUncomment the examples you want to run!")