import threading
import time as tm

total = 0

def print_numbers():
    global total
    id = threading.get_ident()
    for i in range(1, 60000000):
        #print(f'{i}@{id}')
        total = total + i
        #tm.sleep(0.025)

threads = []
for I in range(5):
    thread = threading.Thread(target=print_numbers)
    threads.append(thread)
    thread.start()  # Start the thread
for I in range(5):    
    threads[I].join()   # Wait for the thread to finish

#print_numbers()
print(total)