import pyttsx3
import speech_recognition as sr
import re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    try:
        # Automatically pick the default microphone or specify the correct device index
        with sr.Microphone() as source:  # Removed device_index=1 for simplicity
            print("Listening...")
            r.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
            r.pause_threshold = 1  # Waits for silence to start recognizing
            audio = r.listen(source, timeout=10, phrase_time_limit=5)  # Listen for audio input
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}')
    except sr.RequestError:
        speak("Sorry, I couldn't reach the Google servers.")
        return "none"
    except sr.UnknownValueError:
        speak("Sorry, I did not understand. Could you please say that again?")
        return "none"
    except Exception as e:
        print(e)
        speak("Sorry, say that again...")
        return "none"
    return query.lower()

availabelItmes = {
    1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5},
    2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35},
    3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
    4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
    5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}
}

def things_finder(item):
    for key, value in availabelItmes.items():
        if value['Item'].lower() == item:
            isPresent = True
            particular_quantity = value['Quantity']
            particular_cost = value['Cost/Item']
            return [isPresent, particular_quantity, particular_cost]
    return [False, 0, 0]

def display_shopping_cart(cart):
    print("Welcome to Ram Library".center(100))
    print(f'{"S.No":<15}{"Item":<15}{"Quantity":<15}')
    for i, (item, details) in enumerate(cart.items(), 1):
        print(f'{i:<15}{item:<15}{details["quantity"]:<15}')

def add_item_inCart(user_cart):
    speak("Enter item name to add: ")
    item_to_added = takecommand()
    if item_to_added == "none":
        return
    speak("Enter number of quantity: ")
    number_quantity = take_number()
    try:
        number_quantity = int(number_quantity)
    except ValueError:
        speak("Please enter a valid number.")
        return

    present, quan, costt = things_finder(item_to_added)
    if present and number_quantity <= quan:
        if item_to_added in user_cart:
            user_cart[item_to_added]['quantity'] += number_quantity
        else:
            user_cart[item_to_added] = {'quantity': number_quantity}
        speak(f'{number_quantity} of {item_to_added} added to cart.')
    else:
        speak(f'{item_to_added} is not available right now. You will be notified soon.')

def remove_item_inCart(user_cart):
    speak("Enter item name to remove: ")
    item_to_added = takecommand()
    if item_to_added == "none":
        return
    speak("Enter number of quantity: ")
    number_quantity = takecommand()
    try:
        number_quantity = int(number_quantity)
    except ValueError:
        speak("Please enter a valid number.")
        return

    if item_to_added in user_cart:
        if number_quantity >= user_cart[item_to_added]['quantity']:
            del user_cart[item_to_added]
            speak(f"All {item_to_added}s removed from the cart.")
        else:
            user_cart[item_to_added]['quantity'] -= number_quantity
            speak(f"{number_quantity} {item_to_added}(s) removed, {user_cart[item_to_added]['quantity']} left in the cart.")
    else:
        speak("Item not found in cart.")

def replace_item_inCart(user_cart):
    speak("Enter item name to replace: ")
    item_to_replace = takecommand()
    if item_to_replace == "none":
        return
    speak("Enter the name of item to add: ")
    item_to_add = takecommand()
    if item_to_add == "none":
        return
    speak('Enter number of quantity: ')
    number_quantity = takecommand()
    try:
        number_quantity = int(number_quantity)
    except ValueError:
        speak("Please enter a valid number.")
        return

    if item_to_replace in user_cart:
        user_cart[item_to_add] = {'quantity': number_quantity}
        del user_cart[item_to_replace]
        speak(f"{item_to_replace} replaced with {item_to_add} ({number_quantity}) in cart.")
    else:
        speak("No such item in cart.")

user_cart = {}
while True:
    speak("What do you want to perform? Add to cart, remove from cart, replace item in cart, display my cart, or no more item.")
    user_said = takecommand()
    if user_said == "none":
        continue
    match user_said:
        case "add to cart":
            add_item_inCart(user_cart)
        case "remove from cart":
            remove_item_inCart(user_cart)
        case "replace item in cart":
            replace_item_inCart(user_cart)
        case "display my cart":
            display_shopping_cart(user_cart)
        case "no more item":
            speak("Have a good day!")
            break
