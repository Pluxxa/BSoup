from bs4 import BeautifulSoup
import requests
from googletrans import Translator

url = "https://randomword.com/"



def get_english_word():
    url = "https://randomword.com/"
    try:
        resourse = requests.get(url)

        soup = BeautifulSoup(resourse.content, "html.parser")

        english_word = soup.find("div", id="random_word").text.strip()
        defin = soup.find("div", id="random_word_definition").text.strip()
        return {"english_word" : english_word,
                "defin" : defin
        }

    except:
        return None

def word_game():
    print("Добро пожаолвать в игру")
    while True:
        word_dict = get_english_word()
        word = word_dict.get("english_word")
        defin = word_dict.get("defin")
        translator = Translator()
        result = translator.translate(word, dest="ru")
        result1 = translator.translate(defin, dest="ru")
        print(f"Значение слова - {result1.text}")
        user = input("Что это за слово?")
        if user == word:
            print("Ответ верный!")
        else:
            print(f"Ответ не верный, было загадано слово - {result.text}")

        play_again = input("Хотите сыграть еще раз?")
        if play_again != "y":
            print("Спасибо за игру!")
            break
        else:
            continue


word_game()