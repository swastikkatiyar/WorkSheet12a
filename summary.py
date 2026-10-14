import sys
with open("demo_logs.log",'r') as file:
    for line in file:
        if "ERROR" in line:
            with open('Error.log', 'a') as f:
                f.write(line)
        elif "INFO" in line:
            with open('Info.log', 'a') as f:
                f.write(line)