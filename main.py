from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_receipt(transaction_id, date, name, amount, items):
    # Define the PDF file name
    file_name = f"receipt_{transaction_id}.pdf"
    document_title = "Payment Receipt"
    title = "Payment Receipt"
    sub_title = f"Transaction ID: {transaction_id}"
    date_of_purchase = f"Date: {date}"
    customer_name = f"Customer: {name}"

    # Create a canvas object
    pdf = canvas.Canvas(file_name, pagesize=letter)
    pdf.setTitle(document_title)

    # Add the title and other details
    pdf.drawString(30, 750, title)
    pdf.drawString(30, 735, sub_title)
    pdf.drawString(30, 720, date_of_purchase)
    pdf.drawString(30, 705, customer_name)
    pdf.drawString(30, 690, "Items Purchased:")

    # List the items
    y = 675
    for item in items:
        pdf.drawString(30, y, f"- {item}")
        y -= 15

    # Add the amount
    pdf.drawString(30, y - 15, f"Total Amount: ${amount}")

    # Save the PDF
    pdf.save()

    print(f"Receipt saved as {file_name}")

# Example usage
transaction_id = "12345"
date = "2024-11-14"
name = "John Doe"
amount = 150.75
items = ["Item 1 - $50", "Item 2 - $100", "Discount - $-10"]

generate_receipt(transaction_id, date, name, amount, items)
