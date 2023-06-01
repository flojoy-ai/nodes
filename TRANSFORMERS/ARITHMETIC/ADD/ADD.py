import numpy as np
from flojoy import flojoy, DataContainer

from nodes.node_utils import Reconciler


@flojoy
def ADD(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Add 2 or more numeric arrays, matrices, dataframes, or constants element-wise.
    When a constant is added to an array or matrix, each element in the array or
    matrix will be increased by the constant value. If 2 arrays or matrices of different
    sizes are added, the output will be the size of the larger array or matrix with
    only the overlapping elements changed.
    """

    if len(dc_inputs) < 2:
        raise ValueError(
            f"To add the values, ADD node requires two inputs, {len(dc_inputs)} was given!"
        )

    dc_reconciler = Reconciler()
    cur_sum = dc_inputs[0]
    for operand_n in dc_inputs[1:]:
        # reconcile the types of the inputs before calling numpy
        reconciled_lhs, reconciled_rhs = dc_reconciler.reconcile(cur_sum.y, operand_n.y)
        cur_sum = np.add(reconciled_lhs, reconciled_rhs)

    return DataContainer(x=dc_inputs[0].x, y=cur_sum)
