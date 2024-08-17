from prefect import flow, task, get_run_logger
import time
import random

@task
def extract():
    seconds = random.randint(1,10)
    time.sleep(seconds)
    return seconds

@task
def load(data):
    seconds = random.randint(1,10)
    time.sleep(seconds)
    return seconds

@flow
def main():
    logger = get_run_logger()
    data = extract()
    load(data)



