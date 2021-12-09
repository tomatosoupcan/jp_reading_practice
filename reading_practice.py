import random
import pykakasi
import os
from deep_translator import GoogleTranslator

kks = pykakasi.kakasi()
words = [line.strip() for line in open('popular_jp.txt', encoding='utf-8')]
hira_right = 0
hira_total = 0
kana_right = 0
kana_total = 0
while (True):
	translated = random.choice(words).split(" ")[0]
	english = GoogleTranslator(source='japanese',target='english').translate(translated)
	result = kks.convert(translated)
	compiled_kana = ""
	compiled_hira = ""
	compiled_hepb = ""
	for item in result:
		compiled_kana += item['kana']
		compiled_hira += item['hira']
		compiled_hepb += item['hepburn']
	if compiled_kana != english and compiled_hira != english:
		if random.randint(0, 1) == 0:
			response = input(compiled_kana + ": ")
			os.system('cls')
			kana_total +=1
			if response == compiled_hepb:
				kana_right += 1
				print("Correct!\nHepburn: {} | Response: {}\nJapanese: {} | English: {}".format(compiled_hepb, response, compiled_kana, english))
			else:
				print("Incorrect!\nHepburn: {} | Response: {}\nJapanese: {} | English: {}".format(compiled_hepb, response, compiled_kana, english))
		else:
			response = input(compiled_hira + ": ")
			os.system('cls')
			hira_total +=1
			if response == compiled_hepb:
				hira_right += 1
				print("Correct!\nHepburn: {} | Response: {}\nJapanese: {} | English: {}".format(compiled_hepb, response, compiled_hira, english))
			else:
				print("Incorrect!\nHepburn: {} | Response: {}\nJapanese: {} | English: {}".format(compiled_hepb, response, compiled_hira, english))
		print("Hiragana {}/{} | Katakana {}/{}\n\n".format(hira_right, hira_total, kana_right, kana_total))