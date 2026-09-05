from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("test_document_2.pdf", pagesize=letter)

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(100, 750, "TechCorp Innovations - Q4 2026 Financial Report")

# Content Body
c.setFont("Helvetica", 12)
c.drawString(100, 710, "1. Financial Highlights:")
c.drawString(120, 690, "- Total revenue for Q4 2026 reached $5.1 Million (up from $4.2M in Q3).")
c.drawString(120, 670, "- Net profit margin expanded to 21.0% due to automated pipeline workflows.")
c.drawString(120, 650, "- Operating expenses increased slightly by 2% to $1.1M for end-of-year bonuses.")

c.drawString(100, 610, "2. Operational Updates:")
c.drawString(120, 590, "- The AI research team added 8 new engineers in November (total 20 hires in 2026).")
c.drawString(120, 570, "- Project Alpha reached 100,000 active users; budget expanded to $120,000.")

c.drawString(100, 530, "3. Full Year 2027 Projections:")
c.drawString(120, 510, "- Projected Full Year 2027 revenue target is set at $22.0 Million.")

c.save()
print("✅ 'test_document_2.pdf' created successfully!")