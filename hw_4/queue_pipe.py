from multiprocessing import Queue, Process
import time
import sys
from datetime import datetime
from codecs import encode


def get_time_string(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    return f"[{timestamp}] `{message}`"


def processA(queue_in, queue_out):
    while True:
        # if not queue_in.empty():
        message = queue_in.get()
        print(get_time_string(message) + " in Process A")
        message = message.lower()
        queue_out.put(message)
        time.sleep(5)


def processB(queue_in, queue_out):
    while True:
        # if not queue_in.empty():
        message = queue_in.get()
        print(get_time_string(message) + " in Process B")
        encoded_message = encode(message, 'rot_13')
        queue_out.put(encoded_message)


if __name__ == "__main__":
    queueMainA = Queue()
    queueAB = Queue()
    queueBMain = Queue()

    process_A = Process(target=processA, args=(queueMainA, queueAB,))
    process_B = Process(target=processB, args=(queueAB, queueBMain, ))

    process_A.start()
    process_B.start()

    for stdin in sys.stdin:
        stdin = stdin.strip()
        print(get_time_string(stdin) + " input in cmd")
        queueMainA.put(stdin)

        message = queueBMain.get()
        print(get_time_string(message) + " in MAIN")

    process_A.terminate()
    process_B.terminate()
