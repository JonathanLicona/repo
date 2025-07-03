import datetime

# ---------------- Constantes / Constants ---------------- #
PRODUCT_FIELDS = ["title", "author", "category", "price", "stock"]
products = {}  # Diccionario para productos / Dictionary for products
sales = []     # Lista para ventas / List for sales

# ---------------- Funciones auxiliares / Helper Functions ---------------- #
def generate_product_id():
    # Genera un ID único para el producto / Generate a unique product ID
    return f"P{len(products) + 1:03d}"

def validate_positive_float(prompt):
    # Valida que sea un número flotante positivo / Validate positive float input
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Debe ser un número positivo / Must be a positive number.")
            return value
        except ValueError as e:
            print(f"Error: {e}")

def validate_positive_int(prompt):
    # Valida que sea un entero positivo / Validate positive integer input
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Debe ser un número entero positivo / Must be a positive integer.")
            return value
        except ValueError as e:
            print(f"Error: {e}")

# ---------------- Gestión de inventario / Inventory Management ---------------- #
def add_product():
    print("\n--- Agregar producto / Add New Product ---")
    product_id = generate_product_id()
    title = input("Título / Title: ")
    author = input("Autor / Author: ")
    category = input("Categoría / Category: ")
    price = validate_positive_float("Precio / Price: ")
    stock = validate_positive_int("Cantidad en stock / Stock quantity: ")

    products[product_id] = {
        "title": title,
        "author": author,
        "category": category,
        "price": price,
        "stock": stock
    }
    print(f"Producto '{title}' agregado con ID: {product_id} / Product added with ID: {product_id}")

def update_product():
    print("\n--- Actualizar producto / Update Product ---")
    pid = input("Ingrese el ID del producto / Enter Product ID: ")
    if pid in products:
        print(f"Actualizando '{products[pid]['title']}' / Updating '{products[pid]['title']}'")
        products[pid]["price"] = validate_positive_float("Nuevo precio / New Price: ")
        products[pid]["stock"] = validate_positive_int("Nuevo stock / New Stock: ")
        print("Producto actualizado / Product updated.")
    else:
        print("Producto no encontrado / Product not found.")

def delete_product():
    print("\n--- Eliminar producto / Delete Product ---")
    pid = input("ID del producto / Product ID: ")
    if pid in products:
        del products[pid]
        print("Producto eliminado / Product deleted.")
    else:
        print("Producto no encontrado / Product not found.")

def list_products():
    print("\n--- Lista de productos / Product List ---")
    if not products:
        print("No hay productos registrados / No products registered.")
    else:
        for pid, p in products.items():
            print(f"{pid}: {p['title']} por/by {p['author']} | {p['category']} | ${p['price']} | Stock: {p['stock']}")

# ---------------- Registro de ventas / Sales Management ---------------- #
def register_sale():
    print("\n--- Registrar venta / Register Sale ---")
    customer = input("Nombre del cliente / Customer name: ")
    list_products()
    pid = input("ID del producto / Enter Product ID: ")
    if pid not in products:
        print("ID no válido / Invalid Product ID.")
        return

    product = products[pid]
    quantity = validate_positive_int("Cantidad / Quantity: ")
    if quantity > product["stock"]:
        print("¡Stock insuficiente! / Insufficient stock!")
        return

    discount = validate_positive_float("Descuento (%) [0 si no aplica] / Discount (%): ")

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    total_price = product["price"] * quantity
    discounted_price = total_price * (1 - discount / 100)

    # Registrar venta / Record sale
    sales.append({
        "customer": customer,
        "product_id": pid,
        "title": product["title"],
        "author": product["author"],
        "quantity": quantity,
        "price": product["price"],
        "discount": discount,
        "date": date,
        "net_price": discounted_price
    })

    # Actualizar stock / Update stock
    product["stock"] -= quantity

    print(f"Venta registrada: {quantity} x {product['title']} con {discount}% de descuento.")

def view_sales():
    print("\n--- Historial de ventas / Sales Records ---")
    if not sales:
        print("No hay ventas registradas / No sales registered.")
    else:
        for s in sales:
            print(f"{s['date']} | {s['customer']} compró/bought {s['quantity']} x {s['title']} por/for ${s['net_price']:.2f} (Descuento/Discount: {s['discount']}%)")

# ---------------- Módulo de reportes / Reports ---------------- #
def top_3_products():
    print("\n--- Top 3 productos más vendidos / Top 3 Bestsellers ---")
    stats = {}
    for s in sales:
        stats[s["product_id"]] = stats.get(s["product_id"], 0) + s["quantity"]
    top = sorted(stats.items(), key=lambda x: x[1], reverse=True)[:3]
    for pid, qty in top:
        print(f"{products[pid]['title']} - {qty} vendidos / sold")

def sales_by_author():
    print("\n--- Ventas por autor / Sales by Author ---")
    authors = {}
    for s in sales:
        authors[s["author"]] = authors.get(s["author"], 0) + s["net_price"]
    for author, total in authors.items():
        print(f"{author}: ${total:.2f}")

def calculate_revenue():
    print("\n--- Ingresos / Revenue Summary ---")
    gross = sum(s["price"] * s["quantity"] for s in sales)
    net = sum(s["net_price"] for s in sales)
    print(f"Ingreso bruto / Gross Income: ${gross:.2f}")
    print(f"Ingreso neto / Net Income (después de descuentos): ${net:.2f}")

# ---------------- Menú principal / Main Menu ---------------- #
def main_menu():
    while True:
        print("\n========== Sistema de Librería / Bookstore System ==========")
        print("1. Agregar producto / Add Product")
        print("2. Actualizar producto / Update Product")
        print("3. Eliminar producto / Delete Product")
        print("4. Listar productos / List Products")
        print("5. Registrar venta / Register Sale")
        print("6. Ver ventas / View Sales")
        print("7. Top 3 más vendidos / Top 3 Products")
        print("8. Ventas por autor / Sales by Author")
        print("9. Reporte de ingresos / Revenue Report")
        print("0. Salir / Exit")
        choice = input("Selecciona una opción / Select an option: ")

        try:
            match choice:
                case "1": add_product()
                case "2": update_product()
                case "3": delete_product()
                case "4": list_products()
                case "5": register_sale()
                case "6": view_sales()
                case "7": top_3_products()
                case "8": sales_by_author()
                case "9": calculate_revenue()
                case "0":
                    print("¡Hasta pronto! / Goodbye!")
                    break
                case _: print("Opción inválida / Invalid choice.")
        except Exception as e:
            print(f"Ocurrió un error inesperado / Unexpected error: {e}")

# ---------------- Datos iniciales / Initial Data ---------------- #
def preload_products():
    sample = [
        {"title": "Python 101", "author": "John Smith", "category": "Programming", "price": 25.99, "stock": 10},
        {"title": "Digital Marketing", "author": "Alice Brown", "category": "Business", "price": 19.99, "stock": 15},
        {"title": "Data Science Basics", "author": "Jane Doe", "category": "Data", "price": 30.00, "stock": 8},
        {"title": "AI Revolution", "author": "Dr. Tech", "category": "Technology", "price": 40.50, "stock": 5},
        {"title": "History of Art", "author": "L. Vinci", "category": "Art", "price": 22.75, "stock": 12}
    ]
    for p in sample:
        pid = generate_product_id()
        products[pid] = p

# ---------------- Ejecución principal / Main Execution ---------------- #
if __name__ == "__main__":
    preload_products()  # Cargar productos iniciales / Load preloaded products
    main_menu()         # Iniciar menú / Start menu
