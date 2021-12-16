import random
import pykakasi
import os
import re
from deep_translator import GoogleTranslator

os.system('cls')
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
	compiled_hepb = re.sub(r'[\W_]+','',compiled_hepb)
	if compiled_kana != english and compiled_hira != english and compiled_kana != '' and compiled_hira != '':
		passed = False
		if random.randint(0, 1) == 0:
			while not passed:
				response = input(compiled_kana + ": ")
				if response == "h":
					hira_right += 1
				elif response == "k":
					kana_right += 1
				elif response == compiled_hepb:
					kana_right += 1
					os.system('cls')
					print("Correct!\nHepburn: {} | Response: {}\nJapanese: {} | English: {}".format(compiled_hepb, response, compiled_kana, english))
					passed = True
				else:
					os.system('cls')
					print("Incorrect!\nHepburn: {} | Response: {}\nJapanese: {} | English: {}".format(compiled_hepb, response, compiled_kana, english))
					passed = True
			kana_total +=1
		else:
			while not passed:
				response = input(compiled_hira + ": ")
				if response == "h":
					hira_right += 1
				elif response == "k":
					kana_right += 1
				elif response == compiled_hepb:
					hira_right += 1
					os.system('cls')
					print("Correct!\nHepburn: {} | Response: {}\nJapanese: {} | English: {}".format(compiled_hepb, response, compiled_hira, english))
					passed = True
				else:
					os.system('cls')
					print("Incorrect!\nHepburn: {} | Response: {}\nJapanese: {} | English: {}".format(compiled_hepb, response, compiled_hira, english))
					passed = True
			hira_total +=1
		print("Hiragana {}/{} | Katakana {}/{}\n\n".format(hira_right, hira_total, kana_right, kana_total))