import queue
import time
import random

# Створення черги заявок
request_queue = queue.Queue()
request_id = 1  # Лічильник для унікальних ID заявок

def generate_request():
    global request_id
    request = f"Заявка №{request_id}"
    request_queue.put(request)
    print(f"[+] Створено: {request}")
    request_id += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[-] Обробляється: {request}")
        time.sleep(random.uniform(0.5, 1.5))  # Імітація обробки
        print(f"[✓] Завершено: {request}")
    else:
        print("[!] Черга пуста, немає заявок для обробки.")

# Головний цикл програми
try:
    while True:
        generate_request()
        time.sleep(random.uniform(0.5, 1.0))  # Імітація часу надходження нової заявки
        process_request()
        print("-" * 40)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\n[!] Програма завершена користувачем.") 