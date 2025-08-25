#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
StegoForge - Simple LSB steganography (hide/extract text in RGB images).
Save as: stegoforge.py
Author: BlackIceSec
"""

import argparse
import sys
import os
from PIL import Image

# ---------------- Encode Function ----------------
def encode_message(input_image, output_image, message):
    if not os.path.exists(input_image):
        print(f"[-] Input file not found: {input_image}")
        return

    try:
        img = Image.open(input_image)
    except Exception as e:
        print(f"[-] Failed to open image: {e}")
        return

    img = img.convert('RGB')
    encoded = img.copy()
    width, height = img.size
    index = 0

    # Add delimiter at end of message to mark end
    delimiter = "%%END%%"
    message_full = message + delimiter
    binary_message = ''.join([format(ord(c), "08b") for c in message_full])
    total_bits = len(binary_message)

    capacity_bits = width * height * 3
    if total_bits > capacity_bits:
        print(f"[-] Message too large for this image. Capacity: {capacity_bits//8} bytes, Needed: {total_bits//8} bytes")
        return

    for row in range(height):
        for col in range(width):
            if index < total_bits:
                pixel = list(img.getpixel((col, row)))
                for n in range(3):  # R, G, B
                    if index < total_bits:
                        bit = int(binary_message[index])
                        pixel[n] = (pixel[n] & ~1) | bit
                        index += 1
                encoded.putpixel((col, row), tuple(pixel))
            else:
                # we've written entire message, save and exit
                try:
                    # ensure PNG for lossless storage
                    if not output_image.lower().endswith(".png"):
                        output_image = output_image + ".png"
                    encoded.save(output_image, format="PNG", optimize=True)
                    print(f"[+] Message encoded and saved as: {output_image}")
                except Exception as e:
                    print(f"[-] Failed to save output image: {e}")
                return

    # If loop finishes but message not fully encoded (shouldn't happen because capacity checked)
    print("[-] Unexpected end: message may not have been fully written.")


# ---------------- Decode Function ----------------
def decode_message(input_image):
    if not os.path.exists(input_image):
        print(f"[-] Input file not found: {input_image}")
        return

    try:
        img = Image.open(input_image)
    except Exception as e:
        print(f"[-] Failed to open image: {e}")
        return

    img = img.convert('RGB')
    width, height = img.size

    binary_data = []
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for n in range(3):  # R,G,B
                binary_data.append(str(pixel[n] & 1))

    # join bits and chunk into bytes
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ""
    for byte_bits in all_bytes:
        if len(byte_bits) < 8:
            break
        byte = int("".join(byte_bits), 2)
        message += chr(byte)
        if message.endswith("%%END%%"):
            secret = message[:-7]
            print("[+] Hidden message found:")
            print(secret)
            return

    print("[-] No hidden message found (or delimiter missing).")


# ---------------- CLI ----------------
def main():
    parser = argparse.ArgumentParser(prog="StegoForge", description="StegoForge - hide/extract text in images (LSB).")
    sub = parser.add_subparsers(dest="cmd")

    # encode
    p_enc = sub.add_parser("encode", help="Hide a message inside an image")
    p_enc.add_argument("-i", "--input", required=True, help="Input cover image (PNG/JPG)")
    p_enc.add_argument("-o", "--output", required=True, help="Output image path (PNG recommended)")
    group = p_enc.add_mutually_exclusive_group(required=True)
    group.add_argument("-m", "--message", help="Message text to hide")
    group.add_argument("-f", "--file", help="Read message from text file")

    # decode
    p_dec = sub.add_parser("decode", help="Extract hidden message from an image")
    p_dec.add_argument("-i", "--input", required=True, help="Stego image (PNG)")

    # capacity
    p_cap = sub.add_parser("capacity", help="Show approximate message capacity for an image")
    p_cap.add_argument("-i", "--input", required=True, help="Image to inspect")

    args = parser.parse_args()

    if args.cmd == "encode":
        if args.file:
            if not os.path.exists(args.file):
                print(f"[-] Message file not found: {args.file}")
                sys.exit(1)
            with open(args.file, "r", encoding="utf-8", errors="replace") as fh:
                message = fh.read()
        else:
            message = args.message or ""

        if not message:
            print("[-] Message cannot be empty.")
            sys.exit(1)
        encode_message(args.input, args.output, message)

    elif args.cmd == "decode":
        decode_message(args.input)

    elif args.cmd == "capacity":
        if not os.path.exists(args.input):
            print(f"[-] File not found: {args.input}")
            sys.exit(1)
        img = Image.open(args.input).convert("RGB")
        cap_bytes = (img.size[0] * img.size[1] * 3) // 8
        print(f"[i] Approximate capacity: ~{cap_bytes} bytes")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

