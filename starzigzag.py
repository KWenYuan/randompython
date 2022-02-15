import time

indent = 0
ascending = True

while True:
    print(" " * indent, sep='', end='')
    print("********")
    # prints every 0.5 seconds
    time.sleep(0.5)
    if ascending == True:
        indent += 1
        if indent == 10:
            ascending = False
    else:
        indent -= 1
        if indent == 0:
            ascending = True
