from fpdf import FPDF
from SRC.var_text_report import texto


def situation (country, owner):
    if country == "Ghana" and owner == "Government":
        txt = texto["Situation1"]
    elif country == "Ghana" and owner == "Private":
        txt = texto["Situation2"] 
    elif country == "Spain" and owner == "Government":
        txt = texto["Situation3"]
    elif country == "Spain" and owner == "Private":
        txt = texto["Situation4"]
    else:
        txt = ""
    #elif country == "Both" and owner == "Government":
    #    txt = texto["Situation5"]
    #elif country == "Both" and owner == "Private":
    #    txt = texto["Situation6"]
    return txt


def writing_analysis(txt, country):
    if country == "Ghana" or country == "Spain":
        report = f"""Regions in {txt["param1"]} usually have one {txt["param2"]} hospital for every {txt["param3"]} people 
        whereas infant mortality goes from {txt["param4"]}. This number {txt["param5"]} related to the number of hospitals 
        {txt["param6"]} have been counted as one unit and not for number of beds. On the other hand, {txt["param7"]} 
        relationship could be observed between the area covered by a hospital and mortality{txt["param8"]} """
        report = "".join(report.split("\n    "))
    else:
        report = """Great differences can be appreciated between countries as Ghana's mortality is ten times higher than
        Spain's. Nevertheless, in order to draw a conclusion regarding the influence of the population/hospitals and 
        area/hospital ratios, more parameters would have to be taken into account, such as the capacity of the hospital."""
        report = "".join(report.split("\n        "))
    print(report)     
    return report    


def createpdf (country, owner):

    # Generate FPDF object and add page
    pdf = FPDF("P","mm","A4") # (orientation, unit, format)
    pdf.add_page()

    # Title
    pdf.set_font("Courier", "B", 20) # (letter type, style, size)
    pdf.set_text_color(15,20,85)
    #pdf.set_draw_color(220,220,220) # give color to borders
    pdf.set_fill_color(200,200,200)
    
    if country == "Both":
        pdf.cell(0, 20, f"Mortality in Ghana and Spain - Report", 0, 1, "C", True)
    else:
        pdf.cell(0, 20, f"{country} hospitals - mortality report", 0, 1, "C", True)
    #FPDF.set_title(title = f"{country} hospitals - mortality report")

    # Image
    pdf.image("OUTPUT/graphic.png", x = 25, y = 40, w = 150, h = 110)

    # Text
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(10,10,10)
    txt = situation (country, owner)
    report = writing_analysis(txt, country)
    #pdf.cell(0, 240, report)
    #FPDF.text(x=0, y=140, report)
    #FPDF.set_xy(0.00, 10.00)
    pdf.set_xy(25,160)
    pdf.write(10, report)
    
    # Save File
    pdf.output("OUTPUT/Report.pdf","F")