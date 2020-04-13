from fpdf import FPDF
from SRC.var_text_report import texto


def situation (country, owner):
    if country == "Ghana" and owner == "Government":
        return texto["Situation1"]
    elif country == "Ghana" and owner == "Private":
        return texto["Situation2"]
    elif country == "Spain" and owner == "Government":
        return texto["Situation3"]
    elif country == "Spain" and owner == "Private":
        return texto["Situation4"]


def createpdf (country, owner):

    # Generate FPDF object and add page
    pdf = FPDF("P","mm","A4") # (orientation, unit, format)
    pdf.add_page()

    # Title
    pdf.set_font("Courier", "B", 20) # (letter type, style, size)
    pdf.set_text_color(15,20,85)
    #pdf.set_draw_color(220,220,220) # give color to borders
    pdf.set_fill_color(200,200,200)
    pdf.cell(0, 20, f"{country} hospitals - mortality report", 0, 1, "C", True)

    # Image
    pdf.image("OUTPUT/graphic.png", x = 25, y = 40, w = 160, h = 120)

    # Text
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(10,10,10)
    pdf.cell(0, 100, situation (country, owner))
    
    # Save File
    pdf.output("OUTPUT/Report.pdf","F")