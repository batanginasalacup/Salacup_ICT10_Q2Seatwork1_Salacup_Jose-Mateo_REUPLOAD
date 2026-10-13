from pyscript import display, document, window

# RECEIPT GENERATOR

# Prices
Bangerz_price = 4500
BRAT_price = 2300
Prima_price = 2500
DETOUR_price = 1700
Olivia_price = 3000

def get_int(element_id):
    """Safely fetch integer values without crashing on blank inputs."""
    try:
        val = document.getElementById(element_id).value
        return int(val) if val else 0
    except ValueError:
        return 0

def generate_receipt(e=None):
    # Clear previous output
    receipt_box = document.getElementById("receipt")
    receipt_box.replaceChildren()

    # Get customer information
    customer_name = document.getElementById("customerName").value or "N/A"
    contact_number = document.getElementById("contactNumber").value or "N/A"

    # Get checked states and quantities
    bangerz_checked = document.getElementById("Bangerz").checked
    brat_checked = document.getElementById("BRAT").checked
    prima_checked = document.getElementById("Prima").checked
    detour_checked = document.getElementById("DETOUR").checked
    olivia_checked = document.getElementById("Olivia").checked

    Bangerz_quantity = get_int("BangerzQty") if bangerz_checked else 0
    BRAT_quantity = get_int("BRATQty") if brat_checked else 0
    Prima_quantity = get_int("PrimaQty") if prima_checked else 0
    DETOUR_quantity = get_int("DETOURQty") if detour_checked else 0
    Olivia_quantity = get_int("OliviaQty") if olivia_checked else 0

    # Calculate subtotal
    subtotal = (
        (Bangerz_price * Bangerz_quantity)
        + (BRAT_price * BRAT_quantity)
        + (Prima_price * Prima_quantity)
        + (DETOUR_price * DETOUR_quantity)
        + (Olivia_price * Olivia_quantity)
    )

    # Calculate VAT and Total
    vat = subtotal * 0.12
    total_amount = subtotal + vat

    # Display receipt line by line
    display("===== RECEIPT =====", target="receipt")
    display(f"Customer Name: {customer_name}", target="receipt")
    display(f"Contact Number: {contact_number}", target="receipt")
    display("-------------------------", target="receipt")

    if Bangerz_quantity > 0:
        display(f"Bangerz x {Bangerz_quantity}: ₱{Bangerz_price * Bangerz_quantity:,.2f}", target="receipt")

    if BRAT_quantity > 0:
        display(f"BRAT x {BRAT_quantity}: ₱{BRAT_price * BRAT_quantity:,.2f}", target="receipt")

    if Prima_quantity > 0:
        display(f"Prima x {Prima_quantity}: ₱{Prima_price * Prima_quantity:,.2f}", target="receipt")

    if DETOUR_quantity > 0:
        display(f"DETOUR x {DETOUR_quantity}: ₱{DETOUR_price * DETOUR_quantity:,.2f}", target="receipt")

    if Olivia_quantity > 0:
        display(f"You Seem Pretty Sad x {Olivia_quantity}: ₱{Olivia_price * Olivia_quantity:,.2f}", target="receipt")

    display("-------------------------", target="receipt")
    display(f"Subtotal: ₱{subtotal:,.2f}", target="receipt")
    display(f"VAT (12%): ₱{vat:,.2f}", target="receipt")
    display(f"Total Amount: ₱{total_amount:,.2f}", target="receipt")


# SKU GENERATOR

def generate_sku(e=None):
    # Clear previous output
    sku_box = document.getElementById("skuOutput")
    sku_box.replaceChildren()

    category = document.getElementById("category").value.strip()
    product_name = document.getElementById("productName").value.strip()
    stock_qty = document.getElementById("stockQuantity").value.strip()

    if not category or not product_name or not stock_qty:
        display("Please fill in all SKU fields.", target="skuOutput")
        return

    # Create the SKU
    SKU = f"{category[:3].upper()}-{product_name[:4].upper()}-{stock_qty}"

    # Display the SKU
    display(f"SKU: {SKU}", target="skuOutput")


# PAGE NAVIGATION

def show_receipt(e=None):
    document.getElementById("receiptPage").style.display = "block"
    document.getElementById("skuPage").style.display = "none"

def show_sku(e=None):
    document.getElementById("receiptPage").style.display = "none"
    document.getElementById("skuPage").style.display = "block"


# Bind to global window scope so HTML py-click triggers reliably
window.generate_receipt = generate_receipt
window.generate_sku = generate_sku
window.show_receipt = show_receipt
window.show_sku = show_sku