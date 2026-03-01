# utils/helpers.py

def get_welcome_text():
    return "Welcome! Please choose your language / कृपया अपनी भाषा चुनें:"

def get_link_text(lang):
    if lang == "en":
        return "Your online service website link is here:"
    else:
        return "आपकी ऑनलाइन सर्विस वेबसाइट की लिंक यहां है:"