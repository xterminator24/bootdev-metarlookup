import pyttsx3

# This is just a file that is used for testing

def main():
    engine = pyttsx3.init()
    text = "Hello, this is a test to see how things work"
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    main()