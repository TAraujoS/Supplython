from . import views
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def mm_to_pt(mm):
    return mm/0.352777

pdf = canvas.Canvas('/list_suppliers.pdf', pagesize=A4)

pdf.drawString(mm_to_pt(20), mm_to_pt(400), views.SupplierDetailView)

pdf.save()