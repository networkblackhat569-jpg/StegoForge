# StegoForge

StegoForge is a lightweight steganography tool written in Python that allows you to **hide secret messages inside images** and retrieve them later.  
This project is made for **educational and research purposes only**.

---

## 🚀 Features
- 🔒 Encode (hide) text messages inside PNG images.
- 🔍 Decode and extract hidden messages from stego images.
- 📊 Check how much message capacity an image can hold.
- 🖥️ Simple and lightweight command-line interface.

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/StegoForge.git
cd StegoForge
pip install -r requirements.txt

⚡ Usage
🔹 Encode a message:

python3 StegoForge.py encode -i input.png -o secret.png -m "My hidden text"

🔹 Decode a message:

python3 StegoForge.py decode -i secret.png

🔹 Check image capacity:

python3 StegoForge.py capacity -i input.png

🛡️ Disclaimer

StegoForge is developed for educational and research purposes only.

By using this tool, you agree to the following:

    ✅ You will use it only on images and systems that you own or have explicit permission to test.

    🚫 The author(s) of this project are not responsible for any misuse, damage, or illegal activity carried out with this tool.

    ⚠️ Using this software to hide malicious code, illegal data, or confidential information without authorization is strictly prohibited and may violate laws.

    📝 The responsibility for the ethical and legal use of this project lies entirely with the end-user.

If you are unsure whether your use case is legal, please consult with a professional or seek proper authorization before proceeding.
⭐ Support the Project

If you found StegoForge useful:

    Leave a ⭐ on the GitHub Repository

    Share it with your friends & colleagues

Made with ❤️ for learning and security research.
