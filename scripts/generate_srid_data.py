from pathlib import Path
from datetime import date, timedelta
import csv
import random

# ---------------------------------------------------------
# SRID SYNTHETIC SOURCE DATA GENERATOR
# ---------------------------------------------------------

SEED = 42
random.seed(SEED)

START_DATE = date(2025, 10, 1)
END_DATE = date(2026, 3, 31)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "source"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

COUNTS = {
    "customers": 1284,
    "products": 6735,
    "suppliers": 218,
    "sales_orders": 14860,
    "sales_order_lines": 48700,
    "invoices": 13940,
    "payments": 11620,
    "inventory_snapshots": 82000,
    "purchase_orders": 7850,
    "shipment_events": 36500,
}

LOCATIONS = [
    "Germiston Distribution Centre",
    "Rustenburg Depot",
    "eMalahleni Depot",
    "Durban Depot",
]

PROVINCES = [
    ("Gauteng", ["Johannesburg", "Midrand", "Germiston", "Boksburg", "Pretoria"]),
    ("North West", ["Rustenburg", "Brits", "Klerksdorp"]),
    ("Mpumalanga", ["eMalahleni", "Middelburg", "Secunda"]),
    ("KwaZulu-Natal", ["Durban", "Richards Bay", "Pinetown"]),
    ("Limpopo", ["Polokwane", "Lephalale", "Mokopane"]),
    ("Free State", ["Bloemfontein", "Sasolburg", "Welkom"]),
]

INDUSTRIES = [
    "Mining",
    "Manufacturing",
    "Construction",
    "Engineering",
    "Energy",
    "Process Industries",
]

PRODUCT_CATEGORIES = {
    "Mechanical": [
        "Industrial Bearing",
        "Gearbox",
        "Coupling",
        "Pump",
        "Valve",
        "Seal Kit",
        "Conveyor Roller",
        "Drive Belt",
    ],
    "Electrical": [
        "Electric Motor",
        "Contactor",
        "Circuit Breaker",
        "Cable",
        "Variable Speed Drive",
        "Control Panel",
        "Power Supply",
    ],
    "Process Control": [
        "Pressure Transmitter",
        "Flow Meter",
        "Temperature Sensor",
        "PLC Module",
        "Level Sensor",
        "Control Valve",
        "Instrumentation Cable",
    ],
    "Safety": [
        "Safety Helmet",
        "Protective Gloves",
        "Respirator",
        "Safety Harness",
        "Protective Goggles",
        "Safety Boots",
        "Hearing Protection",
    ],
}

COMPANY_PREFIXES = [
    "Makhulu",
    "Thaba",
    "Imbokodo",
    "Metsi",
    "Khanyisa",
    "Ubuntu",
    "Siyanda",
    "Mahlathi",
    "Ikhwezi",
    "Tshwane",
    "Lethabo",
    "Mvelo",
    "Mzimkhulu",
    "Kganya",
    "Masakhane",
    "Vuka",
    "Bokamoso",
    "Ndlovu",
    "Ridgeway",
    "Highveld",
]

COMPANY_SUFFIXES = [
    "Mining",
    "Engineering",
    "Industrial",
    "Manufacturing",
    "Projects",
    "Resources",
    "Construction",
    "Processing",
    "Solutions",
    "Holdings",
]

SUPPLIER_PREFIXES = [
    "Apex",
    "Atlas",
    "Vector",
    "Prime",
    "Titan",
    "Global",
    "Precision",
    "Industrial",
    "Continental",
    "Metro",
    "Dynamic",
    "Advanced",
]

SUPPLIER_SUFFIXES = [
    "Components",
    "Engineering Supplies",
    "Industrial Systems",
    "Process Solutions",
    "Mechanical Supplies",
    "Electrical Systems",
    "Safety Products",
    "Automation",
]

PAYMENT_METHODS = [
    "EFT",
    "Bank Transfer",
    "Direct Deposit",
]

ORDER_CHANNELS = [
    "Email",
    "Sales Representative",
    "Customer Portal",
    "Telephone",
]

SHIPMENT_EVENT_TYPES = [
    "Picked",
    "Dispatched",
    "In Transit",
    "Delivered",
]


def random_date(start=START_DATE, end=END_DATE):
    days = (end - start).days
    return start + timedelta(days=random.randint(0, days))


def money(value):
    return round(value, 2)


def write_csv(filename, rows, fieldnames):
    path = OUTPUT_DIR / filename

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"{filename:<28} {len(rows):>8,} rows")


# ---------------------------------------------------------
# 1. CUSTOMERS
# ---------------------------------------------------------

customers = []

for i in range(1, COUNTS["customers"] + 1):
    province, cities = random.choice(PROVINCES)
    company = (
        f"{random.choice(COMPANY_PREFIXES)} "
        f"{random.choice(COMPANY_SUFFIXES)} "
        f"{i:04d}"
    )

    customers.append({
        "customer_id": f"CUS{i:06d}",
        "customer_name": company,
        "industry": random.choice(INDUSTRIES),
        "province": province,
        "city": random.choice(cities),
        "credit_limit": money(random.randint(50, 1500) * 1000),
        "payment_terms_days": random.choice([30, 30, 30, 45, 60]),
        "customer_status": random.choices(
            ["Active", "On Hold"],
            weights=[97, 3]
        )[0],
        "created_date": random_date(
            date(2015, 1, 1),
            date(2025, 9, 30)
        ).isoformat(),
    })

write_csv(
    "customers.csv",
    customers,
    customers[0].keys()
)


# ---------------------------------------------------------
# 2. SUPPLIERS
# ---------------------------------------------------------

suppliers = []

for i in range(1, COUNTS["suppliers"] + 1):
    suppliers.append({
        "supplier_id": f"SUP{i:04d}",
        "supplier_name": (
            f"{random.choice(SUPPLIER_PREFIXES)} "
            f"{random.choice(SUPPLIER_SUFFIXES)} "
            f"{i:03d}"
        ),
        "country": random.choices(
            ["South Africa", "Germany", "China", "United Kingdom", "United States"],
            weights=[65, 10, 12, 7, 6]
        )[0],
        "payment_terms_days": random.choice([30, 45, 60]),
        "supplier_status": random.choices(
            ["Active", "Inactive"],
            weights=[96, 4]
        )[0],
    })

write_csv(
    "suppliers.csv",
    suppliers,
    suppliers[0].keys()
)


# ---------------------------------------------------------
# 3. PRODUCTS
# ---------------------------------------------------------

products = []
category_names = list(PRODUCT_CATEGORIES.keys())

for i in range(1, COUNTS["products"] + 1):
    category = random.choice(category_names)
    description = random.choice(PRODUCT_CATEGORIES[category])

    unit_cost = money(random.uniform(80, 18000))
    markup = random.uniform(1.18, 1.55)
    selling_price = money(unit_cost * markup)

    products.append({
        "product_id": f"PRD{i:06d}",
        "sku": f"SRID-{category[:3].upper()}-{i:05d}",
        "product_description": description,
        "category": category,
        "supplier_id": random.choice(suppliers)["supplier_id"],
        "unit_cost": unit_cost,
        "list_price": selling_price,
        "reorder_level": random.randint(5, 80),
        "product_status": random.choices(
            ["Active", "Discontinued"],
            weights=[98, 2]
        )[0],
    })

write_csv(
    "products.csv",
    products,
    products[0].keys()
)


# ---------------------------------------------------------
# 4. SALES ORDERS + SALES ORDER LINES
# ---------------------------------------------------------

orders = []

for i in range(1, COUNTS["sales_orders"] + 1):
    order_date = random_date()

    orders.append({
        "sales_order_id": f"SO{i:07d}",
        "customer_id": random.choice(customers)["customer_id"],
        "order_date": order_date,
        "location": random.choice(LOCATIONS),
        "order_channel": random.choice(ORDER_CHANNELS),
        "status": "Completed",
        "order_total_excl_vat": 0.00,
    })

# Every order receives at least one line.
line_counts = [1] * COUNTS["sales_orders"]

remaining_lines = (
    COUNTS["sales_order_lines"]
    - COUNTS["sales_orders"]
)

while remaining_lines > 0:
    index = random.randrange(COUNTS["sales_orders"])

    if line_counts[index] < 8:
        line_counts[index] += 1
        remaining_lines -= 1

sales_order_lines = []
line_id = 1

for order_index, order in enumerate(orders):
    order_total = 0.0

    for line_number in range(1, line_counts[order_index] + 1):
        product = random.choice(products)

        quantity = random.randint(1, 25)
        unit_price = float(product["list_price"])

        discount_pct = random.choices(
            [0, 2.5, 5, 7.5, 10, 15],
            weights=[35, 15, 25, 10, 10, 5]
        )[0]

        line_total = money(
            quantity
            * unit_price
            * (1 - discount_pct / 100)
        )

        order_total += line_total

        sales_order_lines.append({
            "sales_order_line_id": f"SOL{line_id:08d}",
            "sales_order_id": order["sales_order_id"],
            "line_number": line_number,
            "product_id": product["product_id"],
            "quantity": quantity,
            "unit_price": unit_price,
            "discount_pct": discount_pct,
            "line_total_excl_vat": line_total,
        })

        line_id += 1

    order["order_total_excl_vat"] = money(order_total)

# 920 orders remain open/cancelled/not invoiced.
invoice_order_indices = set(
    random.sample(
        range(COUNTS["sales_orders"]),
        COUNTS["invoices"]
    )
)

for index, order in enumerate(orders):
    if index not in invoice_order_indices:
        order["status"] = random.choice(
            ["Open", "Pending", "Cancelled"]
        )

# Convert dates before writing.
sales_orders_csv = []

for order in orders:
    row = order.copy()
    row["order_date"] = row["order_date"].isoformat()
    sales_orders_csv.append(row)

write_csv(
    "sales_orders.csv",
    sales_orders_csv,
    sales_orders_csv[0].keys()
)

write_csv(
    "sales_order_lines.csv",
    sales_order_lines,
    sales_order_lines[0].keys()
)


# ---------------------------------------------------------
# 5. INVOICES
# ---------------------------------------------------------

invoices = []

invoice_orders = [
    orders[i]
    for i in sorted(invoice_order_indices)
]

for i, order in enumerate(invoice_orders, start=1):
    invoice_date = order["order_date"] + timedelta(
        days=random.randint(0, 7)
    )

    if invoice_date > END_DATE:
        invoice_date = END_DATE

    subtotal = float(order["order_total_excl_vat"])
    vat_amount = money(subtotal * 0.15)
    invoice_total = money(subtotal + vat_amount)

    customer = next(
        c for c in customers
        if c["customer_id"] == order["customer_id"]
    )

    due_date = invoice_date + timedelta(
        days=int(customer["payment_terms_days"])
    )

    invoices.append({
        "invoice_id": f"INV{i:07d}",
        "sales_order_id": order["sales_order_id"],
        "customer_id": order["customer_id"],
        "invoice_date": invoice_date,
        "due_date": due_date,
        "subtotal_excl_vat": money(subtotal),
        "vat_amount": vat_amount,
        "invoice_total": invoice_total,
        "invoice_status": "Unpaid",
    })


# ---------------------------------------------------------
# 6. PAYMENTS
# ---------------------------------------------------------

payments = []

paid_invoice_indices = random.sample(
    range(len(invoices)),
    COUNTS["payments"]
)

for i, invoice_index in enumerate(paid_invoice_indices, start=1):
    invoice = invoices[invoice_index]

    invoice_date = invoice["invoice_date"]
    invoice_total = float(invoice["invoice_total"])

    payment_date = invoice_date + timedelta(
        days=random.randint(5, 60)
    )

    if payment_date > END_DATE:
        payment_date = END_DATE

    payment_ratio = random.choices(
        [1.00, 0.75, 0.50],
        weights=[82, 12, 6]
    )[0]

    amount = money(invoice_total * payment_ratio)

    invoice["invoice_status"] = (
        "Paid"
        if payment_ratio == 1.00
        else "Partially Paid"
    )

    payments.append({
        "payment_id": f"PAY{i:07d}",
        "invoice_id": invoice["invoice_id"],
        "customer_id": invoice["customer_id"],
        "payment_date": payment_date.isoformat(),
        "payment_method": random.choice(PAYMENT_METHODS),
        "amount": amount,
        "reference": f"SRIDPAY{i:07d}",
    })

invoice_rows = []

for invoice in invoices:
    row = invoice.copy()
    row["invoice_date"] = row["invoice_date"].isoformat()
    row["due_date"] = row["due_date"].isoformat()
    invoice_rows.append(row)

write_csv(
    "invoices.csv",
    invoice_rows,
    invoice_rows[0].keys()
)

write_csv(
    "payments.csv",
    payments,
    payments[0].keys()
)


# ---------------------------------------------------------
# 7. INVENTORY SNAPSHOTS
# ---------------------------------------------------------

inventory_snapshots = []

snapshot_dates = [
    date(2025, 10, 31),
    date(2025, 11, 30),
    date(2025, 12, 31),
    date(2026, 1, 31),
    date(2026, 2, 28),
    date(2026, 3, 31),
]

used_inventory_keys = set()

while len(inventory_snapshots) < COUNTS["inventory_snapshots"]:
    product = random.choice(products)
    location = random.choice(LOCATIONS)
    snapshot_date = random.choice(snapshot_dates)

    key = (
        product["product_id"],
        location,
        snapshot_date
    )

    if key in used_inventory_keys:
        continue

    used_inventory_keys.add(key)

    reorder_level = int(product["reorder_level"])

    quantity_on_hand = random.randint(
        0,
        max(20, reorder_level * 4)
    )

    quantity_reserved = random.randint(
        0,
        min(quantity_on_hand, 30)
    )

    inventory_snapshots.append({
        "snapshot_date": snapshot_date.isoformat(),
        "location": location,
        "product_id": product["product_id"],
        "quantity_on_hand": quantity_on_hand,
        "quantity_reserved": quantity_reserved,
        "quantity_available": quantity_on_hand - quantity_reserved,
        "reorder_level": reorder_level,
        "unit_cost": product["unit_cost"],
    })

write_csv(
    "inventory_snapshots.csv",
    inventory_snapshots,
    inventory_snapshots[0].keys()
)


# ---------------------------------------------------------
# 8. PURCHASE ORDERS
# ---------------------------------------------------------

purchase_orders = []

for i in range(1, COUNTS["purchase_orders"] + 1):
    product = random.choice(products)

    po_date = random_date()
    quantity = random.randint(5, 150)
    unit_cost = float(product["unit_cost"])

    expected_date = po_date + timedelta(
        days=random.randint(5, 35)
    )

    purchase_orders.append({
        "purchase_order_id": f"PO{i:07d}",
        "supplier_id": product["supplier_id"],
        "product_id": product["product_id"],
        "order_date": po_date.isoformat(),
        "expected_delivery_date": expected_date.isoformat(),
        "location": random.choice(LOCATIONS),
        "quantity_ordered": quantity,
        "unit_cost": money(unit_cost),
        "po_total": money(quantity * unit_cost),
        "status": random.choices(
            ["Received", "Open", "Partial", "Cancelled"],
            weights=[75, 12, 8, 5]
        )[0],
    })

write_csv(
    "purchase_orders.csv",
    purchase_orders,
    purchase_orders[0].keys()
)


# ---------------------------------------------------------
# 9. SHIPMENT EVENTS
# ---------------------------------------------------------

shipment_events = []

event_counts = [2] * COUNTS["sales_orders"]

remaining_events = (
    COUNTS["shipment_events"]
    - (COUNTS["sales_orders"] * 2)
)

while remaining_events > 0:
    index = random.randrange(COUNTS["sales_orders"])

    if event_counts[index] < 4:
        event_counts[index] += 1
        remaining_events -= 1

shipment_id = 1

for order_index, order in enumerate(orders):
    event_count = event_counts[order_index]

    event_types = SHIPMENT_EVENT_TYPES[:event_count]

    base_date = order["order_date"]

    for sequence, event_type in enumerate(event_types, start=1):
        event_date = base_date + timedelta(
            days=sequence + random.randint(0, 2)
        )

        if event_date > END_DATE:
            event_date = END_DATE

        shipment_events.append({
            "shipment_event_id": f"SHP{shipment_id:08d}",
            "sales_order_id": order["sales_order_id"],
            "location": order["location"],
            "event_sequence": sequence,
            "event_type": event_type,
            "event_date": event_date.isoformat(),
            "carrier": random.choice([
                "SRID Logistics",
                "TransAfrica Freight",
                "Highveld Logistics",
                "Ubuntu Distribution",
            ]),
        })

        shipment_id += 1

write_csv(
    "shipment_events.csv",
    shipment_events,
    shipment_events[0].keys()
)


# ---------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------

print("\nSRID synthetic source data generation complete.")
print(f"Output directory: {OUTPUT_DIR}")
print(f"Data period: {START_DATE} to {END_DATE}")
print(f"Random seed: {SEED}")

total_rows = sum(COUNTS.values())

print(f"Total generated rows: {total_rows:,}")