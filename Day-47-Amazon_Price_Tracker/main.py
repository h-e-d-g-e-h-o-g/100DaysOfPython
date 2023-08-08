import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    'Accept-Language': "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=header)
response_html = response.text

soup = BeautifulSoup(response_html, 'lxml')
price_html = soup.find(name="span", class_= "a-offscreen")
price = float(price_html.getText().split("$")[1])
product_title_html = soup.find(name="span", id="productTitle")
product_title = product_title_html.getText().replace("        ", "")
print(price)
print(product_title)

my_email = "raholverma20@gmail.com"
my_password = "fttwxryohmtkqraa"
message = f"Subject:Amazon Price Alert\n\n{product_title}\n{URL}"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    if price < 100:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rahulver345@yahoo.com", 
            msg=message.encode("utf-8")
            )
