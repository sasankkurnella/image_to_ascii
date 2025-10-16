#!/usr/bin/env python3
"""
Image to ASCII Art Converter
Converts images to ASCII art with various customization options.
"""

import sys
from PIL import Image
import argparse
from pathlib import Path


class ASCIIConverter:
    """Convert images to ASCII art."""
    
    # Character sets from darkest to lightest
    ASCII_CHARS_DETAILED = "@%#*+=-:. "
    ASCII_CHARS_SIMPLE = "@#*+=-:. "
    ASCII_CHARS_BLOCKS = "█▓▒░ "
    
    def __init__(self, char_set="detailed"):
        """Initialize converter with specified character set."""
        if char_set == "detailed":
            self.chars = self.ASCII_CHARS_DETAILED
        elif char_set == "simple":
            self.chars = self.ASCII_CHARS_SIMPLE
        elif char_set == "blocks":
            self.chars = self.ASCII_CHARS_BLOCKS
        else:
            self.chars = char_set
    
    def resize_image(self, image, new_width=100):
        """Resize image maintaining aspect ratio."""
        width, height = image.size
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.55)  # 0.55 to account for char height
        return image.resize((new_width, new_height))
    
    def grayscale(self, image):
        """Convert image to grayscale."""
        return image.convert("L")
    
    def pixels_to_ascii(self, image):
        """Map pixels to ASCII characters."""
        pixels = image.getdata()
        ascii_str = ""
        for pixel in pixels:
            ascii_str += self.chars[pixel * len(self.chars) // 256]
        return ascii_str
    
    def convert(self, image_path, width=100, invert=False):
        """
        Convert image to ASCII art.
        
        Args:
            image_path: Path to the image file
            width: Width of ASCII art in characters
            invert: Invert brightness mapping
        
        Returns:
            String containing ASCII art
        """
        try:
            image = Image.open(image_path)
        except Exception as e:
            print(f"Error opening image: {e}")
            return None
        
        # Process image
        image = self.resize_image(image, width)
        image = self.grayscale(image)
        
        # Invert if requested
        if invert:
            self.chars = self.chars[::-1]
        
        # Convert to ASCII
        ascii_str = self.pixels_to_ascii(image)
        
        # Format as lines
        img_width = image.width
        ascii_img = ""
        for i in range(0, len(ascii_str), img_width):
            ascii_img += ascii_str[i:i+img_width] + "\n"
        
        return ascii_img


def save_ascii_art(ascii_art, output_path):
    """Save ASCII art to file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(ascii_art)
        print(f"ASCII art saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")


def main():
    """Main function to handle CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Convert images to ASCII art",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ascii_converter.py image.jpg
  python ascii_converter.py image.jpg -w 150 -o output.txt
  python ascii_converter.py image.jpg -c blocks -i
  python ascii_converter.py image.jpg -c "@#*+=-:. "
        """
    )
    
    parser.add_argument('image', help='Path to input image')
    parser.add_argument('-w', '--width', type=int, default=100,
                       help='Width of ASCII art in characters (default: 100)')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    parser.add_argument('-c', '--charset', default='detailed',
                       choices=['detailed', 'simple', 'blocks'],
                       help='Character set to use (default: detailed)')
    parser.add_argument('-i', '--invert', action='store_true',
                       help='Invert brightness mapping')
    parser.add_argument('--custom-chars', help='Custom character set (darkest to lightest)')
    
    args = parser.parse_args()
    
    # Use custom charset if provided
    charset = args.custom_chars if args.custom_chars else args.charset
    
    # Create converter and process image
    converter = ASCIIConverter(charset)
    ascii_art = converter.convert(args.image, args.width, args.invert)
    
    if ascii_art:
        # Display or save
        if args.output:
            save_ascii_art(ascii_art, args.output)
        else:
            print(ascii_art)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
    