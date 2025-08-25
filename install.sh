#!/bin/bash

echo "🚀 Installing StegoForge..."

# Step 1: Virtual environment (optional)
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Step 2: Activate virtual environment
source venv/bin/activate

# Step 3: Install requirements
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Installation complete!"
echo ""
echo "👉 To run StegoForge:"
echo "   source venv/bin/activate"
echo "   python3 stegoforge.py --help"

