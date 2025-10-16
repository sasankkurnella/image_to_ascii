# 🎨 Image to ASCII Art Converter

Convert any image into beautiful ASCII art! This Python tool transforms images into text-based art using various character sets and customization options.

## ✨ Features

- 🖼️ Convert any image format (JPG, PNG, GIF, etc.) to ASCII art
- 🎭 Multiple character sets (detailed, simple, blocks)
- 📏 Customizable output width
- 🔄 Invert brightness mapping
- 💾 Save to file or print to console
- 🎨 Support for custom character sets
- ⚡ Fast and efficient conversion

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/image-to-ascii.git
cd image-to-ascii
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Usage

Convert an image and display in terminal:
```bash
python ascii_converter.py image.jpg
```

### Advanced Options

**Specify output width:**
```bash
python ascii_converter.py image.jpg -w 150
```

**Save to file:**
```bash
python ascii_converter.py image.jpg -o output.txt
```

**Use different character sets:**
```bash
# Detailed (default)
python ascii_converter.py image.jpg -c detailed

# Simple
python ascii_converter.py image.jpg -c simple

# Block characters
python ascii_converter.py image.jpg -c blocks
```

**Invert brightness:**
```bash
python ascii_converter.py image.jpg -i
```

**Custom character set:**
```bash
python ascii_converter.py image.jpg --custom-chars "█▓▒░ "
```

**Combine options:**
```bash
python ascii_converter.py image.jpg -w 120 -c blocks -o art.txt -i
```

## 🎯 Examples

### Input Image
```bash
python ascii_converter.py samples/portrait.jpg -w 100
```

### Output
```
                    @@@@@@@@@@@@@@@
                @@@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@@@@
            @@@@@@@@#########@@@@@@@@@@@@@
           @@@@@@@##############@@@@@@@@@@
          @@@@@@#################@@@@@@@@@
         @@@@@####################@@@@@@@@
        @@@@######################@@@@@@@
        @@@#####*****########*****#@@@@@@
       @@@####**:::::**###**:::::**#@@@@@
       @@####**:.....:**#**:.....:**#@@@@
       @####***::....:***:::.....:**##@@@
```

## 🛠️ Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--width` | `-w` | Width of ASCII art in characters | 100 |
| `--output` | `-o` | Save output to file | None (prints to console) |
| `--charset` | `-c` | Character set (detailed/simple/blocks) | detailed |
| `--invert` | `-i` | Invert brightness mapping | False |
| `--custom-chars` | | Custom character set string | None |

## 📁 Project Structure

```
image-to-ascii/
├── ascii_converter.py    # Main converter script
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── samples/             # Sample images (optional)
│   └── example.jpg
└── outputs/             # Generated ASCII art (optional)
    └── example.txt
```

## 🎨 Character Sets

**Detailed:** `@%#*+=-:. ` - Best for complex images with lots of detail

**Simple:** `@#*+=-:. ` - Good balance between detail and simplicity

**Blocks:** `█▓▒░ ` - Creates a blocky, retro aesthetic

## 💡 Tips

- **Width:** Smaller width (50-80) works well for simple images, larger width (100-200) for detailed images
- **Invert:** Use `-i` flag if your ASCII art looks reversed (dark areas appear light)
- **File Output:** Save to file for easier sharing and viewing: `-o output.txt`
- **Best Images:** High contrast images with clear subjects work best
- **Terminal:** For best results, use a terminal with a small font size

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Python and Pillow (PIL)
- Inspired by classic ASCII art converters

## 📧 Contact

Your Name - [@yourhandle](https://twitter.com/yourhandle)

Project Link: [https://github.com/yourusername/image-to-ascii](https://github.com/yourusername/image-to-ascii)

---

⭐ Star this repo if you found it helpful!