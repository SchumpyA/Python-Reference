# Python multithreading allows a program to run multiple threads concurrently within a single process,
# improving efficiency and responsiveness for tasks that involve waiting for external resources

import threading
import time

def task(name):
    print(f"Thread {name}: starting...")
    time.sleep(2) # Simulate an I/O operation
    print(f"Thread {name}: finishing.")

# Create a thread
my_thread = threading.Thread(target=task, args=("A",))

# Start the thread
my_thread.start()

print("Main thread: doing other work.")

# Wait for the thread to finish
my_thread.join()
print("Main thread: all done.")
print()

# Python threads achieve concurrency (tasks appear to run at the same time by taking turns using a single CPU core)
# but not true parallelism (tasks running simultaneously on multiple CPU cores)

# Python's multiprocessing module allows for true parallelism in CPU-bound tasks by leveraging multiple processor cores,
# effectively bypassing the Global Interpreter Lock (GIL). This differs from multithreading,
# which is limited to concurrency within a single process in standard Python interpreters

import multiprocessing

def print_square(num):
    """Function to print the square of a number."""
    print(f"Square: {num * num}")

def print_cube(num):
    """Function to print the cube of a number."""
    print(f"Cube: {num * num * num}")

# This block is essential for multiprocessing on Windows and other platforms
if __name__ == "__main__":
    # Create process objects
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))

    # Start the processes
    p1.start()
    p2.start()

    # Wait until both processes are finished
    p1.join()
    p2.join()

    print("Done!")
print()

# Python asynchronous programming is a concurrency model best suited for I/O-bound tasks
# (e.g., network requests, file operations, database queries) where the program would otherwise spend a lot of time waiting.
# It uses a single thread and an event loop to manage multiple tasks concurrently,
# achieving high efficiency without the overhead of threads or multiprocessing

import asyncio

async def fetch_data(delay):
    print(f"Started fetching data with {delay}s delay")
    await asyncio.sleep(delay) # Non-blocking sleep, yields control
    print("Finished fetching data")
    return f"Data after {delay}s"

async def main():
    print("Starting main")
    # Schedule two tasks concurrently
    task1 = asyncio.create_task(fetch_data(2))
    task2 = asyncio.create_task(fetch_data(1))

    # Wait until both tasks complete
    result1, result2 = await asyncio.gather(task1, task2)
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")

if __name__ == "__main__":
    asyncio.run(main()) # Entry point to run the event loop

# To better see the difference run code with
# python Levels/multiThreadingAndProccessing.py

