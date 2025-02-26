from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")


for i, row in df.iterrows():
    pdf.add_page()
    # Set header
    pdf.set_font("Arial", style="B", size=24)
    pdf.set_text_color(0, 100, 254)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align="L", fill=False, link="")
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    pdf.set_line_width(0.5)
    pdf.set_draw_color(0, 100, 254)
    pdf.set_fill_color(200, 220, 255)

    # Set footer
    pdf.ln(265)
    pdf.set_font("Arial", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set footer
        pdf.ln(275)
        pdf.set_font("Arial", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align="R")
        
    




pdf.output("output.pdf")