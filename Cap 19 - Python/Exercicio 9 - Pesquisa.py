texto =  "Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e meu site é https://iaexpert.academy http://iaexpert.academy"

import re

re.findall(r'\d', texto)

re.findall(r'\d{5}-\d{3}', texto)

re.findall(r'https?://[A-Za-z0-9./]+', texto)