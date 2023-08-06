import kernel
kernel.init()

while True:
    line = input(" admin > ")

    if line == "clock":
        kernel.clock()

    if line == "shutdown":
        kernel.shutdown()