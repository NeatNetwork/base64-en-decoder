#--- encode Function to encode text ---#
def encode():
    import base64
    b64encode = input("enter Text to code in base64 \n")
    message_bytes = b64encode.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("Encoded Text: " + base64_message)
    import time
    time.sleep(5)
    start()
#--- decode Function to decode text ---#
def decode():
    import base64
    b64decode = input("enter base64 to decode \n")
    base64_bytes = b64decode.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print("Decoded Text: " + message)
    import time
    time.sleep(5)
    start()
#--- start Function to recall start message ---#
def start():
    q1 = input("do you want to decode or encode text? [type exit to close] \n")
    if q1.lower() == "encode":
        encode()
    elif q1.lower() == "decode":
        decode()
    elif q1.lower() == "exit":
        exit()
    else:
        print("thats not a valid answer")
        start()
start()
