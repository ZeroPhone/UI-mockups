"""
Code written with help of https://www.blog.pythonlibrary.org Reportlab tutorials
"""


import sys
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, landscape, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

pagesize = landscape(A4)

try:
    width = int(sys.argv[1])
except:
    raise ValueError("First argument is width and needs to be a number")
try:
    height = int(sys.argv[2])
except:
    raise ValueError("Second argument is height and needs to be a number")

message = " ".join(sys.argv[3:])
if not message: print("all the other arguments are printed as header")

doc = SimpleDocTemplate("template_{}x{}.pdf".format(width, height), pagesize=pagesize,
                        rightMargin=72,leftMargin=72,
                        topMargin=40,bottomMargin=0)



styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

cell_width = float(pagesize[0]-100)/width
cell_height = float(pagesize[1])/height
	
#cells need to be square
cell_dim = min([cell_width, cell_height])

data = height*[width*[" "]] #just an empty table
#for i in data:
#    print(repr(data))

t=Table(data, width*[cell_dim], height*[cell_dim])
t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                       ('ALIGN',(0,0),(-1,-1),'RIGHT'),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black)]))

elements = []
elements.append(Paragraph(message if message else "Screen template", styles["Center"]))
elements.append(Spacer(1, 40))
elements.append(t)
doc.build(elements)
