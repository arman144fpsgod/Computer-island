log = open("log.txt", 'a')

def oprint(message):
    print(message)
    global log
    log.write(message)
    return

oprint("10")

log.close()