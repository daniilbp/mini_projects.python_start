import re


text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

result_1 = re.findall(r'\b\D\d{3}\D{2}\d{1,3}', text)
result_2 = re.findall(r'\b\D{2}\d{3}\d{1,3}', text)

print('Список номеров частных автомобилей:', result_1)
print('Список номеров такси:', result_2)
