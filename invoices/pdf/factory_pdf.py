from fpdf import FPDF


class Factory_pdf:

    def Pdf(text_exemple):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "", 14)
        pdf.multi_cell(txt=f"ID {text_exemple['id']}", w=0)
        pdf.ln(2)
        pdf.multi_cell(txt=f"DANFE {text_exemple['invoice_number']}", w=0)
        pdf.ln(2)
        pdf.multi_cell(txt=f"DANFE {text_exemple['value']}", w=0)
        pdf.ln(2)
        pdf.multi_cell(txt=f"DANFE {text_exemple['description']}", w=0)
        pdf.ln(2)