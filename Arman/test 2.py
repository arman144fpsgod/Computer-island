import test
'''THI IS THE MAIN FILE'''
print("hello")
while True:

    ui = input(">>")
    if 'hello' in ui:
        print("hi!")
    elif 'how are you' in ui:
        print("im fine")
    elif 'game' in ui:
        '''open the game'''
        test.mygame()
    elif 'exit' in ui:
        break
