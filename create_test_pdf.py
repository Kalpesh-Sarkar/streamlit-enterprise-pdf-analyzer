from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("test_document.pdf", pagesize=letter)

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(100, 750, "TechCorp Innovations - Q3 2026 Financial Report")

# Content Body
c.setFont("Helvetica", 12)
c.drawString(100, 710, "1. Financial Highlights:")
c.drawString(120, 690, "- Total revenue for Q3 2026 reached $4.2 Million.")
c.drawString(120, 670, "- Net profit margin expanded to 18.5%.")
c.drawString(120, 650, "- Operating expenses decreased by 5% due to cloud optimization.")

c.drawString(100, 610, "2. Operational Updates:")
c.drawString(120, 590, "- The AI research team expanded by 12 new engineers in August.")
c.drawString(120, 570, "- Project Alpha was officially launched with an initial budget of $50,000.")

c.drawString(100, 530, "3. Q4 Targets:")
c.drawString(120, 510, "- Projected revenue target for Q4 2026 is $5.0 Million.")

c.save()
print("✅ 'test_document.pdf' successfully created in your project folder!")