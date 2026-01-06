import time
import os
from datetime import datetime
from config import OUTPUT_DIR, PROCESSING_TIME_SECONDS


def process_job(job_id, input_data):
    print(f"[INFO] Job {job_id} started")

    # Simulate heavy computation
    time.sleep(PROCESSING_TIME_SECONDS)

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_file = f"{OUTPUT_DIR}/job_{job_id}_output.txt"

    with open(output_file, "w") as f:
        f.write(f"Job ID: {job_id}\n")
        f.write(f"Input Data: {input_data}\n")
        f.write(f"Processed At: {datetime.now()}\n")
        f.write("Status: SUCCESS\n")

    print(f"[INFO] Job {job_id} completed")
    return output_file


if __name__ == "__main__":
    job_id = int(time.time())
    input_data = "Sample user-submitted task"

    result = process_job(job_id, input_data)
    print(f"[INFO] Output saved at {result}")
