
def greet(name):
    message = 'Hello, ' + name + '-san!'
    print(message)


from datetime import datetime

def greet_new():
    hour = datetime.now().hour
    if hour <= 11:
        greeting = 'Good morning'
    elif hour <= 17:
        greeting = 'Hello'
    else:
        greeting = 'Good evening'
    print(greeting)    



greet('Inoue')
greet_new()
