from flojoy import flojoy, DataContainer, TextBlob
import pyvisa
from typing import Optional


@flojoy(
    deps={
        "pyvisa": "1.13.0",
        "pyusb": "1.2.1",
        "zeroconf": "0.102.0",
        "pyvisa_py": "0.7.0",
    }
)
def LIST_VISA(
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    """The LIST_VISA node lists all VISA instruments available.

    Returns
    -------
    DataContainer
        optional: The input DataContainer is returned.
    """

    rm = pyvisa.ResourceManager("@py")
    addresses = rm.list_resources()
    print("Available VISA instrument addresses: ", addresses, flush=True)
    instr_list = ", ".join(addresses)

    return TextBlob(text_blob=instr_list)
