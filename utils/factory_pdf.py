from fpdf import FPDF
from django.core.mail import EmailMessage
from django.conf import settings


def factory_pdf(self, contract, employee):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "", 14)
    pdf.multi_cell(txt="Supplython Invoices", h=1, align="C", w=0)
    pdf.ln()
    pdf.multi_cell(txt="_____________________________________________", align="C", w=0)
    pdf.ln(10)
    pdf.multi_cell(txt=f"Invoice Number : {self['invoice_number']}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Value : {self['value']}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Description : {self['description']}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Validity : {self['validity']}", w=0)
    pdf.ln(2)

    pdf.multi_cell(txt=f"Supplier", h=1, align="C", w=0)
    pdf.ln()
    pdf.multi_cell(txt="_____________________________________________", align="C", w=0)
    pdf.ln(10)
    pdf.multi_cell(txt=f"Id : {contract.supplier.id}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Name : {contract.supplier.name}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Email : {contract.supplier.email}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Telephone : {contract.supplier.tel}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"CNPJ : {contract.supplier.cnpj}", w=0)
    pdf.ln(2)

    pdf.multi_cell(txt=f"Category", h=1, align="C", w=0)
    pdf.ln()
    pdf.multi_cell(txt="_____________________________________________", align="C", w=0)
    pdf.ln(10)
    pdf.multi_cell(txt=f"Id : {contract.category.id}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Name : {contract.category.name}", w=0)
    pdf.ln(2)

    pdf.multi_cell(txt=f"Employee", h=1, align="C", w=0)
    pdf.ln()
    pdf.multi_cell(txt="_____________________________________________", align="C", w=0)
    pdf.ln(10)
    pdf.multi_cell(txt=f"Id : {employee.id}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Name : {employee.name}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Username : {employee.username}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Email : {employee.email}", w=0)
    pdf.ln(2)
    pdf.multi_cell(txt=f"Is_active : {employee.is_active}", w=0)
    pdf.ln(2)

    pdf.output("invoice.pdf")

    email = EmailMessage(
        subject="New Invoice Created",
        body="A new invoice was generated in the name of your company, check the data that were filled in!",
        from_email=settings.EMAIL_HOST_USER,
        to=[contract.supplier.email],
    )
    email.attach_file("invoice.pdf")

    return email.send(fail_silently=False)
