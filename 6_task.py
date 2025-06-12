text = "X-DSPAM-Confidence:    0.8475"
text_2 = text.find('0')  # Найти индекс начала числа
lego = text[text_2:]  # Взять срез строки, начиная с найденного индекса
print(float(lego)) 
