import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/gp/product/B075BCSFNN/ref=s9_acss_bw_cg_INPCWe_3a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=8522N2AJG1KA8TXGVPEJ&pf_rd_t=101&pf_rd_p=f7b9aca3-bbba-46d4-b6b5-9b81c1f3b2bc&pf_rd_i=11599648031'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    convertedPrice = float(price[2:3]+price[4:7])

    if convertedPrice < 1300.0:
        sendMail()

    print(convertedPrice)
    print(title.strip())


def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('9780066535.vs@gmail.com', 'dswpmoyfmeidqkds')

    subject = "Price fell down!"
    body = "Check link https://www.amazon.in/gp/product/B075BCSFNN/ref=s9_acss_bw_cg_INPCWe_3a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=8522N2AJG1KA8TXGVPEJ&pf_rd_t=101&pf_rd_p=f7b9aca3-bbba-46d4-b6b5-9b81c1f3b2bc&pf_rd_i=11599648031"
    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail('9780066535.vs@gmail.com', 'sharmavik279@gmail.com', msg)
    print('EMAIL SENT')
    server.quit()


while True:
    checkPrice()
    time.sleep(43200)
