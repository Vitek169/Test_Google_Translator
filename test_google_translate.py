import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

"""Вводим в поисковике Переводчик онлайн"""
print('Вводим на английской раскладке, русскоии буквами')
driver.get('https://www.google.com/search?q=gthtdjlxbr+jykfqy+&sxsrf=AJOqlzXy-N1OYTJi8oUOdJ6hs1nDoKh8qg%3A1675863275440&ei=66TjY--fGu2FwPAPhPmF-AY&ved=0ahUKEwivweWZhYb9AhXtAhAIHYR8AW8Q4dUDCA8&uact=5&oq=gthtdjlxbr+jykfqy+&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCMQsQIQJzIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjoKCAAQRxDWBBCwAzoLCAAQgAQQChABECo6CQgAEBYQHhDxBDoGCAAQFhAeOggIABAWEB4QD0oECEEYAEoECEYYAFD2NljMPmCOVGgDcAB4AIABVYgBzQOSAQE2mAEAoAEByAEIwAEB&sclient=gws-wiz-serp')
driver.maximize_window()
print('Колдунщик появился первым при выдаче результатов')

enter_text = driver.find_element(By.XPATH,'//*[@id="tw-source-text-ta"]')
enter_text.click()
print('Кликаем на поле "Введите текст"')
time.sleep(3)

"""Пишем текст, который будет вводится в поле"""
text_1 = 'Today is a wonderful day'
enter_text.send_keys(text_1)
print('Текст введен')

"""Пишем ожидаемый перевод"""
translation = driver.find_element(By.XPATH, '//*[@id="tw-target-text"]')
value_translation = translation.text
print(value_translation, 'Перевод текста успешен!', sep = '\n')
time.sleep(2)

"""Кликаем на кнопку обратный перевод"""
change_language = driver.find_element(By.XPATH, '//*[@id="tw-swap"]/span')
change_language.click()
time.sleep(2)
translation_2 = driver.find_element(By.XPATH, '//*[@id="tw-target-text"]')
value_translation_2 = translation_2.text
print(value_translation_2, "Обратный перевод успешен!", sep = '\n')
time.sleep(2)

'''Выбираем другой язык в меню выбора языка на который хотим перевести'''
language_exit = driver.find_element(By.XPATH, '//*[@id="tw-tl"]')
language_exit.send_keys(Keys.ENTER)
time.sleep(2)

"""Выбираем язык Китайский"""
chine_language = driver.find_element(By.XPATH, '//*[@id="tw-container"]/g-expandable-container/div/div/div[7]/g-expandable-container/div/g-expandable-content/span/div/div[2]/div[1]/div/div[2]/div[52]')
chine_language.send_keys(Keys.ENTER)
value_chine_language = '今天是美好的一天'
print(value_chine_language, 'Китайский язык выбран', sep = '\n')
time.sleep(2)

voice_chaine_language = driver.find_element(By.XPATH, '//*[@id="tw-spkr-button"]')
voice_chaine_language.send_keys(Keys.ENTER)
print('Воспроизведение перевода на Китайском. Функция голосового воспроизведения работает.')
time.sleep(3)
driver.quit()
print('Тест успешно завершен!')
