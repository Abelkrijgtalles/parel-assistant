def iscommand(command):
    import os
    str(command)
    command = command.upper()
    output = "python3 commands/" + command + ".py"
    os.system(output)