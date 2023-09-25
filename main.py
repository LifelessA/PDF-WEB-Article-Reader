from tool import extract_paragraphs_from_page,speak,html_to_text
from mtranslate import translate
import threading
from time import sleep
import keyboard
import os
from gtts import gTTS



en = {}
hi = {}
def translator(text_data, index, language=None):
    
    if language == "en":
        en[index] = text_data
        return en
    elif language == 'hi':
        tr = translate(text_data, from_language="en", to_language="hi")
        hi[index] = tr
        return hi
    elif language is None:
        print("please select language")
    else:
        print("Help")

def main_pdf(path, page, language):
    en.clear()
    hi.clear()
        
    pdf_data = extract_paragraphs_from_page(path, page)
    threads = []
    for k in range(len(pdf_data)):
        process1 = threading.Thread(target=translator, args=(pdf_data[k], k, language, ))
        sleep(0.1)
        print(f"\rpage:-{page} pera{k} complete : {'░'*int(k/len(pdf_data)*100)}",end="")
        threads.append(process1)
        process1.start()

    # Wait for all threads of the current chapter to finish
    for thread in threads:
        thread.join()
    print("")
    if language=="en":
        sorted_dict = dict(sorted(en.items()))
        return sorted_dict
    elif language=="hi":
        sorted_dict = dict(sorted(hi.items()))
        return  sorted_dict
        
def main_web(url, language, tags):
    en.clear()
    hi.clear()
    web_data = html_to_text(url,tags)

    threads = []
    for k,item in enumerate(web_data[tags]):
        process1 = threading.Thread(target=translator, args=(item, k, language, ))
        sleep(0.1)
        print(f"\rpage:- pera{k} complete : {'░'*int(k/len(web_data['p'])*100)}",end="")
        threads.append(process1)
        process1.start()

    # Wait for all threads of the current chapter to finish
    for thread in threads:
        thread.join()
    print("")
    if language=="en":
        sorted_dict = dict(sorted(en.items()))
        return sorted_dict
    elif language=="hi":
        sorted_dict = dict(sorted(hi.items()))
        return  sorted_dict          

def pdf_read(path, pages, speak_language, print_language,Gtts = False,audio_path=os.getcwd()):
    enter = input("Enter:-")
    en_words = main_pdf(path=path, page=pages,language="en")
    hi_words = main_pdf(path=path, page=pages,language="hi")
    # print(f"\n{en_words}")
    # print(f"\n{hi_words}")
    if Gtts == False:
        for h,e in zip(hi_words,en_words):
            if keyboard.is_pressed("space"):
                print("Loop paused.")
                print("Hit enter to continue")
                keyboard.wait("enter")  # Wait for any key press
                print("Loop resumed.")
            if speak_language == "hi" and print_language == "en":
                print(en_words[e])
                speak(hi_words[h],210,"hi")
            elif speak_language == "en" and print_language == "en":
                print(en_words[e])
                speak(hi_words[e],210)
            elif speak_language == "hi" and print_language == "hi":
                print(en_words[h])
                speak(hi_words[h],210,"hi")
            elif speak_language == "en" and print_language == "hi":
                print(en_words[h])
                speak(hi_words[e],210)
    elif Gtts == True:
        en_text = ""
        hi_text = ""
        for h,e in zip(hi_words,en_words):
            en_text += en_words[e]
            hi_text += hi_words[h]
        if speak_language == "hi":
            audio = gTTS(hi_text)
        elif speak_language == "en":
            audio = gTTS(en_text)
        audio_p = os.path.join(audio_path, "output_audio.mp3")
        audio.save(audio_p)
        print("Wait for Further Updates...")


def web_read(url,tag,speak_language,print_language,Gtts=False,audio_path=os.getcwd()):
    enter = input("Enter:-")
    en_words = main_web(url=url,tags=tag,language="en")
    hi_words = main_web(url=url, tags=tag,language="hi")
    # print(f"\n{en_words}")
    # print(f"\n{hi_words}")
    if Gtts == False:
        for h,e in zip(hi_words,en_words):
            if keyboard.is_pressed("space"):
                print("Loop paused.")
                print("Hit enter to continue")
                keyboard.wait("enter")  # Wait for any key press
                print("Loop resumed.")
            if speak_language == "hi" and print_language == "en":
                print(en_words[e])
                speak(hi_words[h],210,"hi")
            elif speak_language == "en" and print_language == "en":
                print(en_words[e])
                speak(hi_words[e],210)
            elif speak_language == "hi" and print_language == "hi":
                print(en_words[h])
                speak(hi_words[h],210,"hi")
            elif speak_language == "en" and print_language == "hi":
                print(en_words[h])
                speak(hi_words[e],210) 
    elif Gtts == True:
        en_text = ""
        hi_text = ""
        for h,e in zip(hi_words,en_words):
            en_text += en_words[e]
            hi_text += hi_words[h]
        if speak_language == "hi":
            audio = gTTS(hi_text)
        elif speak_language == "en":
            audio = gTTS(en_text)
        audio_p = os.path.join(audio_path, "output_audio.mp3")
        audio.save(audio_p)
        print("Wait for Further Updates...")
        

if __name__ == '__main__':
    path = "Network Vulnerability Assessment - Identify Security Loopholes in Your Network’s Infrastructur.pdf"
    url = "https://allnovelbook.com/novel/reincarnation-of-the-businesswoman-at-school/chapter-154"
    pages = 18

    # pdf_read(path=path, pages=pages, speak_language="hi", print_language="en", Gtts=True)
    # web_read(url=url,tag="p",speak_language="hi",print_language="en", Gtts=True)
