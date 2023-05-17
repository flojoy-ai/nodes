from flojoy import flojoy, DataContainer, JobResultBuilder
import time


@flojoy
def TIMER(dc_inputs: list[DataContainer], params: dict) -> dict:
    print("executing timer")

    seconds: int = int(params["sleep_time"])
    time.sleep(seconds)

    return JobResultBuilder().from_inputs(dc_inputs).build()
