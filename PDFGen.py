from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PIL import Image
import os
import glob
cardSize = (2.75*inch, 3.75*inch)

# Register the Helvetica TTF font, needed for DTC to print the file
pdfmetrics.registerFont(TTFont('Helvetica', 'Helvetica.ttf'))

# time to build the actual deck itself
cards = glob.glob("images/fronts/*.png")
cardBack = glob.glob("images/back/*.png")

c = canvas.Canvas("output.pdf", cardSize)
for card in cards:
    c.drawImage(card, 0, 0, width=198, height=270, mask=None)
    c.showPage()
    c.drawImage(cardBack[0], 0, 0, width=198, height=270, mask=None)
    c.showPage()
    print("Added "+card)
c.save()
