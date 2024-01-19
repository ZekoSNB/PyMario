import threading
import time

def my_thread_function(stop_event):
    while not stop_event.is_set():
        print("Thread is doing some work...")
        time.sleep(1)

    print("Thread is exiting.")

# Create an event to signal the thread to stop
stop_event = threading.Event()

# Create and start the thread
my_thread = threading.Thread(target=my_thread_function, args=(stop_event,))
my_thread.start()

# Run the thread for a certain duration
time.sleep(5)

# Set the event to signal the thread to stop
stop_event.set()

# Wait for the thread to finish
my_thread.join()

# Continue with the rest of the program...
