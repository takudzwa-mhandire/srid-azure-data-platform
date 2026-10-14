# SRID Dataset Inventory

The SRID platform uses fully synthetic data representing a South African industrial distribution business.

No real customer, employee, supplier, or commercial data is used.

## Source Dataset Volumes

| Dataset | Grain / Primary Key | Rows |
|---|---|---:|
| customers.csv | One row per customer (`customer_id`) | 1,284 |
| products.csv | One row per product (`product_id`) | 6,735 |
| suppliers.csv | One row per supplier (`supplier_id`) | 218 |
| sales_orders.csv | One row per sales order (`sales_order_id`) | 14,860 |
| sales_order_lines.csv | One row per sales order line (`sales_order_line_id`) | 48,700 |
| invoices.csv | One row per invoice (`invoice_id`) | 13,940 |
| payments.csv | One row per payment (`payment_id`) | 11,620 |
| inventory_snapshots.csv | Product/location/date inventory snapshot | 82,000 |
| purchase_orders.csv | One row per purchase order (`purchase_order_id`) | 7,850 |
| shipment_events.csv | One row per shipment event (`shipment_event_id`) | 35,600 |

**Total synthetic source records: 222,807**

## Dataset Structure

### Customers
Customer master data including customer name, industry, province, city, credit limit, payment terms, status, and creation date.

### Products
Product master data including SKU, description, category, supplier, unit cost, list price, reorder level, and product status.

### Suppliers
Supplier master data including supplier name, country, payment terms, and supplier status.

### Sales Orders
Sales order header information including customer, order date, location, sales channel, status, and order value.

### Sales Order Lines
Individual product lines associated with sales orders, including quantity, unit price, discount percentage, and line value.

### Invoices
Customer invoices linked to sales orders, including invoice date, due date, subtotal, VAT, total amount, and invoice status.

### Payments
Payments received against invoices, including payment date, payment method, amount, and reference.

### Inventory Snapshots
Periodic inventory positions by product and location, including quantity on hand, reserved quantity, available quantity, reorder level, and unit cost.

### Purchase Orders
Supplier purchasing transactions including product, order date, expected delivery date, location, quantity ordered, unit cost, total PO value, and status.

### Shipment Events
Shipment tracking events linked to sales orders, including event sequence, event type, date, location, and carrier.

## Data Engineering Layers

- **Landing:** Immutable source CSV files.
- **Bronze:** Raw Delta representation with ingestion metadata.
- **Silver:** Cleaned, typed, deduplicated datasets.
- **Quarantine:** Records failing defined data-quality rules.
- **Gold:** Business-ready dimensional and fact tables for analytics.

## Gold Model

### Dimensions
- `dim_customer`
- `dim_product`
- `dim_supplier`
- `dim_date`

### Facts
- `fact_sales`
- `fact_inventory`
- `fact_finance`
- `fact_procurement`
