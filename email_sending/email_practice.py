import smtplib
from email.message import EmailMessage
# from string import Template
# from pathlib import Path  # similar to os.path

# html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'David Hanson'
email['to'] = 'dave.hanson.c@icloud.com'
email['subject'] = 'You won 1,000,000 dollars!!'

email.set_content('I am a Python Master!')
# email.set_content(html.substitute({'name': 'Jessica'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('python.testing.djhd@gmail.com', 'david#hanson')
    smtp.send_message(email)
    print('all good boss!')