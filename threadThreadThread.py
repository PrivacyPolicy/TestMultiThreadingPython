import threading

def codeToRunConcurrently(start, end):
    for i in range(start, end):
        print(i)

thread = threading.Thread(
    group=None,
    target=codeToRunConcurrently,
    name="Gabe",
    args=(30, 109),
    kwargs={})
thread1 = threading.Thread(
    group=None,
    target=codeToRunConcurrently,
    name="Gabr",
    args=(),
    kwargs={'start': 30, 'end': 119})
thread2 = threading.Thread(
    group=None,
    target=codeToRunConcurrently,
    name="Gabri",
    args=(30, 10109),
    kwargs={})
thread3 = threading.Thread(
    group=None,
    target=codeToRunConcurrently,
    name="Gabrie",
    args=(30, 10119),
    kwargs={})
thread4 = threading.Thread(
    group=None,
    target=codeToRunConcurrently,
    name="Gabriel",
    args=(30, 11009),
    kwargs={})

# Start threads
thread.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
# Prevent below code from running until after threads are done
thread.join()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
# "Code Below"
print('Done!')
