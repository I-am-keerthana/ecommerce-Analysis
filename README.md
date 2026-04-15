# E-commerce laptop analysis (Newegg)

> End-to-end pipeline that scrapes laptop product listings from Newegg.com,
> cleans and structures the raw data with Python, and delivers insights through
> interactive Tableau dashboards.

---

## 🧩 Problem it solves

Laptop buyers and market analysts need to compare hundreds of products across
price, brand, specs, and ratings — but no single view exists across an entire
retailer's catalogue. This project automates the full journey from raw web data
to polished, interactive visualizations, enabling instant market-level analysis
of pricing strategies, brand distribution, and specification trends.

---

## 🛠️ Technologies used

| Tool | Purpose |
|---|---|
| Python | Core language |
| Scrapy (`neweggspider.py`) | High-performance web crawler |
| JSON / Pandas (`cleaningjson.py`) | Data cleaning and normalization |
| Tableau | Interactive dashboard visualizations |

---

## ⚙️ Installation & setup

**1. Clone the repo**
```bash
git clone https://github.com/I-am-keerthana/ecommerce-Analysis.git
cd ecommerce-Analysis
```

**2. Install dependencies**
```bash
pip install scrapy pandas
```

**3. Run the spider**
```bash
scrapy runspider neweggspider.py -o laptops_raw.json
```

**4. Clean the data**
```bash
python cleaningjson.py
```

This outputs a clean `laptops_clean.csv` ready for Tableau import.

---

## 📊 Key findings

- **ASUS and Lenovo** dominate the mid-range segment ($500–$900)
- Laptops with **16GB RAM** have disproportionately higher ratings vs 8GB equivalents
- **Price clustering** around $699 and $999 reveals common psychological pricing points
- Gaming laptops average **2.3× the price** of standard business laptops at the same
  RAM tier

--## 📌 Notes

> Scraping is done responsibly with request delays built in.
> Data is collected from publicly available Newegg product listings.
