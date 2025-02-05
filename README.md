![img](https://i.imgur.com/2e5aLuy.png)

## **📂 Burp Suite Sitemap Tree Visualizer**

### **📌 Overview**
This Python script **parses a Burp Suite sitemap XML export** and converts it into a **hierarchical tree structure**, mimicking Burp Suite's built-in sitemap view.  

✅ **Nests query parameters (`?param=value`) under their respective PHP files**  
✅ **Uses proper styling for files & folders:**
   - **📂** Directories  
   - **📄** Standalone PHP files  
   - **⚙️** PHP files with nested query parameters  
   - **📜** Query parameters  
✅ **Exports the tree to a text file (`sitemap_tree.txt`)**  
✅ **Easily extensible for JSON export or graphical representation**  

---

### **🖼 Example Output**
```
🌐 Root
├── 📂 example.com
│   ├── 📂 assets
│   │   ├── 📂 js
│   │   │   ├── 📄 script1.js
│   │   │   └── 📄 script2.js
│   ├── 📄 file1.txt
└── 📂 www.example.com
    ├── 📂 assets
    │   ├── 📂 css
    │   ├── 📂 favicons
    │   ├── 📂 js
    │   ├── 📂 plugins
    ├── 📂 secrets
    │   ├── 📂 api
    │   │   ├── 📄 book.php
    │   │   ├── 📄 keys.php
    │   │   ├── ⚙️ loader.php
    │   │   │   ├── 📜 f=reviews.php
    │   │   ├── ⚙️ profile.php
    │   │   │   ├── 📜 data=bio

```

---

## **🚀 Installation**
1. **Clone the repository**  
   ```bash
   git clone https://github.com/L0WK3Y-IAAN/burp-sitemap-parser.git
   cd burp-sitemap-parser
   ```

2. **Install dependencies**  
   ```bash
   pip install anytree
   ```

---

## **🛠 Usage**
1. **Ensure you have a Burp Suite sitemap XML export** (e.g., `sitemap.xml`).
2. **Run the script:**
   ```bash
   python burp_sitemap_tree.py
   ```
3. **View the output in the terminal** or **open `sitemap_tree.txt`** for a saved version.

---

## **⚡ Features**
- 📜 **Parses Burp Suite sitemap exports** (`.xml`)  
- 🏗 **Builds a structured tree view**  
- 📂 **Accurately categorizes directories, files, and query parameters**  
- 📄 **Standalone PHP files get `📄` while nested ones get `⚙️`**  
- 📁 **Supports all file types**  
- 📄 **Saves output as `sitemap_tree.txt`**  
- 🛠 **Lightweight & easily extendable**  

---

## **📌 Planned Enhancements**
✅ **Export to JSON format**  
✅ **Graph visualization using NetworkX**  
✅ **Web-based UI for interactive sitemap exploration**  

---

## **💡 Contributing**
Want to improve the script?  
1. Fork the repo  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Make your changes  
4. Submit a pull request 🚀  

---

## **📄 License**
This project is licensed under the **MIT License**.

---

## **👨‍💻 Author**
- **[Your Name]**  
- GitHub: [Your GitHub](https://github.com/L0WK3Y-IAAN)  
- Twitter: [Your Twitter](https://twitter.com/L0WK3Y_OFFICIAL)  

