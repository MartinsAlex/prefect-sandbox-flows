from prefect import flow, task, get_run_logger

@flow
def my_flow(message: str):
    logger = get_run_logger()
    logger.info(message)

if __name__ == '__main__':
    my_flow(message='Hello World!')