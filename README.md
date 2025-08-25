# StegoForge

StegoForge is a simple steganography tool to hide secret messages inside images.

## Features
- Encode secret text messages into PNG images
- Decode hidden messages from stego-images
- Check capacity of an image before encoding

## Installation
```bash
git clone https://github.com/yourusername/StegoForge.git
cd StegoForge
pip install -r requirements.txt
```

## Usage
Encode a message:
```bash
python3 StegoForge.py encode -i input.png -o output.png -m "Your secret message"
```

Decode a message:
```bash
python3 StegoForge.py decode -i output.png
```

Check capacity:
```bash
python3 StegoForge.py capacity -i input.png
```

---
👤 Author: BlackIceSec  
📧 Email: blackicesec@protonmail.com
