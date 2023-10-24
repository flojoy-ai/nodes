from flojoy import flojoy, DataContainer, OrderedPair, VisaConnection
from typing import Optional, Literal


@flojoy(inject_connection=True)
def EXTRACT_TRACE_DS1074Z(
    connection: VisaConnection,
    channel: Literal["ch1", "ch2", "ch3", "ch4"] = "ch1",
    default: Optional[DataContainer] = None,
) -> OrderedPair:
    """The EXTRACT_TRACE_DS1074Z node extracts the trace from an DS1074Z oscilloscope.

    The trace is defined by the x and y limits as seen on the instrument.

    Requires a CONNECTION_DS1074Z node at the start of the app to connect with
    the instrument. The VISA address will then be listed under 'connection'.

    This node should also work with compatible DS1000Z oscilloscopes

    Parameters
    ----------
    connection: VisaConnection
        The VISA address (requires the CONNECTION_DS1074Z node).

    Returns
    -------
    OrderedPair
        The trace of the oscilloscope.
    """

    rigol = connection.get_handle()
    channel = getattr(rigol.channels, channel)

    time = rigol.time_axis()
    trace = channel.trace()

    return OrderedPair(x=time, y=trace)
