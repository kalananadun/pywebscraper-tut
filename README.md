# 🖥️ E-Commerce Price Scraper

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-green)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-orange)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

A simple Python web-scraping application that retrieves the price of a computer component from a generic e-commerce website using **Requests** and **Beautiful Soup**.

---

## 📌 About

This project demonstrates the fundamentals of **web scraping with Python**.

The application sends an HTTP request to an e-commerce product page, retrieves the HTML content, parses the page using **Beautiful Soup**, and extracts information such as the product name and price.

### 🎯 Project Goals

- Learn the basics of Python web scraping
- Understand HTTP requests
- Parse HTML documents using Beautiful Soup
- Extract product information from a webpage
- Understand CSS selectors
- Build a simple and practical Python application

---

## 🛠️ Technologies

| Technology        | Purpose                          |
| ----------------- | -------------------------------- |
| 🐍 Python         | Application programming language |
| 🌐 Requests       | Send HTTP requests               |
| 🍲 Beautiful Soup | Parse HTML                       |
| 📄 HTML/CSS       | Locate webpage elements          |
| 🔧 Git            | Version control                  |

---

## 📂 Project Structure

```text
butifulsoup/
│
├── .venv/          # Python virtual environment
├── main.py         # Main web-scraping application
├── index.html      # Optional web interface
├── README.md       # Project documentation
└── .gitignore      # Git ignore rules
```

> **Note:** `.venv/` should not be committed to Git.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd butifulsoup
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install requests beautifulsoup4
```

---

## 🚀 Usage

Run the application with:

```bash
python main.py
```

A basic implementation looks like this:

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com/product"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.select_one(".price")

if price:
    print("Product Price:", price.get_text(strip=True))
else:
    print("Price not found")
```

### Example Output

```text
Product: Example Computer Component
Price: $129.99
```

> Replace `https://example.com/product` and `.price` with the appropriate product URL and CSS selector for the target website.

---

## 🔄 How It Works

```text
┌─────────────────────────┐
│  E-Commerce Web Page    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Requests Library      │
│     HTTP Request        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      HTML Response      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│    Beautiful Soup       │
│      HTML Parser        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Find Product / Price   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      Display Price      │
└─────────────────────────┘
```

---

## 🧪 Example Use Case

The application can be adapted to retrieve the price of computer components such as:

- 💻 CPUs
- 🎮 GPUs
- 🧠 RAM
- 💾 SSDs
- 🗄️ HDDs
- 🔌 Power Supplies
- 🖥️ Monitors
- ⌨️ Keyboards
- 🖱️ Mice
- 🧊 CPU Coolers

For example:

```text
Product: Example RTX Graphics Card
Price: Rs. 125,000
```

---

## ⚠️ Web Scraping Considerations

This project is intended for **educational purposes**.

Before scraping a website:

- Check its Terms of Service.
- Check its `robots.txt` where appropriate.
- Avoid excessive requests.
- Use reasonable request intervals.
- Do not scrape private or restricted information.
- Respect the website's policies.
- Be aware that webpage structures can change.

Some modern e-commerce websites use JavaScript to dynamically load product information. In such cases, a simple `requests` request may not contain the price in the initial HTML.

---

## 🔮 Future Improvements

Possible improvements include:

- [ ] Scrape multiple products
- [ ] Compare prices between stores
- [ ] Save results to CSV
- [ ] Store product information in a database
- [ ] Add a web interface
- [ ] Track price changes
- [ ] Send price-drop notifications
- [ ] Schedule automatic price checks
- [ ] Build a REST API
- [ ] Add product search functionality

---

## 📚 Learning Outcomes

After completing this project, you should have a basic understanding of:

- HTTP requests
- HTML structure
- DOM elements
- CSS selectors
- Web scraping
- Python libraries
- Virtual environments
- Git and GitHub

---

## 👨‍💻 Author

**Your Name**

GitHub: [@kalananadun](https://github.com/kalananadun)

---

## 📄 License

This project is intended as an educational project for learning **Python, Requests, Beautiful Soup, HTML parsing, and web scraping**.
