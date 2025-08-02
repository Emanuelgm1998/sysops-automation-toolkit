import time, logging

logging.basicConfig(level=logging.INFO)

def simulate_backup():
    logging.info("Starting backup simulation...")
    time.sleep(1)
    logging.info("Backing up /home/user/documents...")
    time.sleep(1)
    logging.info("Backup completed successfully.")

if __name__ == "__main__":
    simulate_backup()
