from fnmatch import translate
from googletrans import Translator

#1. 번역기 생성하기
translator = Translator()

#2. 언어 감지 및 번역을 원하는 구절을 입력받기
book_sentence = input('책을 읽으며 인상 깊었던 구절을 적어주세요: ')

#3. 언어 감지하기
detected = translator.detect(book_sentence) 

#4. 변역을 원하는 언어를 설정하기-아랍어, 스페인어
lang_list = ['ar', 'es']
result1 = translator.translate(book_sentence, lang_list[0])
result2 = translator.translate(book_sentence, lang_list[1])
result_list = [result1.text, result2.text]
print('\n==================== 번역 결과 ====================\n')
print('입력어- ' + detected.lang + ': ' + book_sentence)
for i in range(len(lang_list)):
    
    print('번역어'+ str(i+1) + '- ' + lang_list[i] + ' : ' + result_list[i])
print('\n==================================================')
