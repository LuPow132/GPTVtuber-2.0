import time

def run_function1():
    print("Function 1 called.")

def run_function2():
    global start_time
    start_time = time.time()
    print("Function 2 called.")

start_time = time.time()

# Wait for 5 seconds
time.sleep(5)

if time.time() - start_time >= 5:
    run_function1()
else:
    run_function2()
