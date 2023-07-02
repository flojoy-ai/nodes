import json
from node_sdk.small_memory import SmallMemory
from flojoy import (
    DataContainer,
    flojoy,
    JobResultBuilder,
    DefaultParams,
    ParameterTypes,
)
from typing import Any
from dataclasses import dataclass

memory_key = "loop-info"


@dataclass(frozen=True)  # Multiple outputs
class LoopOutput:
    body: dict[str, str | list[str] | DataContainer] | DataContainer
    end: dict[str, str | list[str] | DataContainer] | DataContainer


class LoopData:
    def __init__(
        self,
        node_id: str,
        num_loops: int = -1,
        current_iteration: int = 0,
        is_finished: bool = False,
    ) -> None:
        self.node_id = node_id
        self.num_loops = int(num_loops)
        self.current_iteration = int(current_iteration)
        self.is_finished = bool(is_finished)

    def restart(self):
        self.current_iteration = 0
        self.is_finished = False

    def step(self):
        self.current_iteration += 1
        if self.current_iteration > self.num_loops:
            self.is_finished = True

    def get_data(self):
        return {
            "node_id": self.node_id,
            "num_loops": self.num_loops,
            "current_iteration": self.current_iteration,
            "is_finished": self.is_finished,
        }

    @staticmethod
    def from_data(node_id: str, data: dict[str, Any]):
        loop_data = LoopData(
            node_id,
            num_loops=data.get("num_loops", -1),
            current_iteration=data.get("current_iteration", 0),
            is_finished=data.get("is_finished", False),
        )
        return loop_data

    def print(self, prefix: str = ""):
        print(f"{prefix}loop Data:", json.dumps(self.get_data(), indent=2))


@flojoy(inject_node_metadata=True)
def LOOP(
    default: DataContainer,
    default_params: DefaultParams,
    num_loops: ParameterTypes.INT = -1,
) -> LoopOutput:
    """The LOOP node is a specialized node that iterates through the body nodes for a given number of times.
    To ensure proper functionality, the LOOP node relies on a companion node called the `GOTO` node.

    Parameters
    ----------
    num_loops : int
        number of times to iterate through body nodes default is `-1` meaning infinity.
    """
    node_id = default_params.node_id
    print("\n\nstart loop:", node_id)
    if num_loops == -1:
        print("infinite loop")
        return build_result(inputs=[default], is_loop_finished=False)
    loop_data: LoopData = load_loop_data(node_id, num_loops)
    loop_data.print("at start ")
    if loop_data.is_finished:
        loop_data.restart()
    else:
        loop_data.step()
    if not loop_data.is_finished:
        store_loop_data(node_id, loop_data)
    else:
        print("finished loop")
        delete_loop_data(node_id)
    print("end loop\n\n")
    return build_result([default], loop_data.is_finished)


def load_loop_data(node_id: str, default_num_loops: int) -> LoopData:
    data: dict[str, Any] = SmallMemory().read_memory(node_id, memory_key) or {}
    loop_data = LoopData.from_data(
        node_id=node_id, data={"num_loops": default_num_loops, **data}
    )
    return loop_data


def store_loop_data(node_id: str, loop_data: LoopData):
    SmallMemory().write_to_memory(node_id, memory_key, loop_data.get_data())
    loop_data.print("store ")


def delete_loop_data(node_id: str):
    SmallMemory().delete_object(node_id, memory_key)
    print("delete loop data")


def build_result(inputs: list[DataContainer], is_loop_finished: bool):
    return LoopOutput(
        body=JobResultBuilder()
        .from_inputs(inputs)
        .flow_by_flag(
            flag=is_loop_finished,
            false_direction=["body"],
            true_direction=["end"],
        )
        .build(),
        end=JobResultBuilder()
        .from_inputs(inputs)
        .flow_by_flag(
            flag=is_loop_finished,
            false_direction=["body"],
            true_direction=["end"],
        )
        .build(),
    )
