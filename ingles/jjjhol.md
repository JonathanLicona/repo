# 📚 Bookstore Management System

This is a **console-based inventory and sales management system** for a national bookstore, developed in **Python**. It allows you to manage products, register and analyze sales, and generate detailed reports with stock control, validations, and discount handling.

---

## 🚀 Features

### 1. Inventory Management
- Add, update, delete, and list books.
- Each product includes: `title`, `author`, `category`, `price`, and `stock`.

### 2. Sales Module
- Register new sales by selecting products, quantity, customer, and optional discount.
- Automatically updates stock.
- Validates if there's enough stock before processing a sale.

### 3. Reporting
- Top 3 best-selling products.
- Total net sales grouped by author.
- Gross and net income (with and without discounts).

### 4. Validations
- Ensures all inputs are valid (positive numbers, required fields).
- Prevents sales if stock is insufficient.
- Error handling using `try-except`.

### 5. Modular Design
- All logic is divided into reusable functions.
- Uses dictionaries and lists to store and manage data.
- Functions use parameters, return values, and lambda expressions for reports.

---

## 📂 Data Structure

### Products
Stored in a dictionary like:
```python
products = {
  "P001": {
    "title": "Book Title",
    "author": "Author Name",
    "category": "Genre",
    "price": 19.99,
    "stock": 5
  },
  ...
}
