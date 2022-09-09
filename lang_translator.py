from googletrans import Translator
translator = Translator()
def translate(prompt):
    res = translator.translate(prompt)
    if res.src == 'th':
        return res.text
    elif res.src == 'en':
        return prompt
    else :
        raise Exception("Unsupported Language")