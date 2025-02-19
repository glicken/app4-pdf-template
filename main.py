from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="p", unit="mm", format="A4")

df = pd.read_csv("topics.csv")


for i, row in df.iterrows():
    pdf.add_page()

    pdf.set_font("Arial", style="B", size=24)
    pdf.set_text_color(0, 100, 254)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align="L", fill=False, link="")
    pdf.line(x1=10, y1=21, x2=200, y2=21)






pdf.output("output.pdf")