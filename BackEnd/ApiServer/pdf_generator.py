import base64
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from datetime import datetime

import os


def generate_pdf(company_logo, company_legal_name, platform_name, user_full_name) -> bytes:
    today_date = datetime.now().strftime("%d/%m/%Y")
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    times_font = os.path.join(os.path.dirname(__file__), 'fonts/Times.ttf')

    pdfmetrics.registerFont(TTFont('Times', times_font))
    pdf.setFont('Times', 12)

    pdf.drawString(100, 630, "Этот текст в договоре сгенерирован автоматически")
    pdf.drawString(100, 610, f"имя пользователя: {user_full_name}")
    pdf.drawString(100, 590, f"название компании: {company_legal_name}")
    pdf.drawString(100, 570, f"название площадки: {platform_name}")
    pdf.drawString(100, 550, f"дата генерации договора: {today_date}")

    img_data = base64.b64decode(company_logo)

    with open("temp.jpg", "wb") as f:
        f.write(img_data)

    pdf.drawInlineImage("temp.jpg", 100, 650, width=100, height=100)

    pdf.showPage()
    pdf.save()

    buffer.seek(0)

    return buffer.read()
