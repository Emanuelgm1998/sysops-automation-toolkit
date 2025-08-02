import psutil, time

def monitor():
    print("[INFO] Monitoring system resources...")
    for i in range(3):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        print(f"[INFO] CPU: {cpu}%, Memory: {mem}%")
        if cpu > 80:
            print("[WARN] High CPU usage detected!")
        if mem > 80:
            print("[WARN] High Memory usage detected!")

if __name__ == "__main__":
    monitor()
