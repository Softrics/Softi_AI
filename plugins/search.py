import wikipedia
import kit
def wiki(command):
    person = command.replace('search wikipedia', '')
    info = wikipedia.summary(person, 10)
    return info
def google(query):
    query = query.replace('search google', '')
    kit.search(query)