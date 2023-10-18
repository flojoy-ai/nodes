from flojoy import flojoy, DataContainer, TextBlob, VisaConnection
from typing import Optional, Literal


@flojoy(inject_connection=True)
def TRIGGER_CHANNEL_MDO3XXX(
    connection: VisaConnection,
    channel: int = 0,
    query_set: Literal["query", "set"] = "query",
    default: Optional[DataContainer] = None,
) -> TextBlob:
    """The TRIGGER_CHANNEL_MDO3XXX node sets the triggering channel (or queries it).

    Requires a CONNECTION_MDO3XXX node at the start of the app to connect with
    the instrument. The VISA address will then be listed under 'connection'.

    This node should also work with compatible Tektronix scopes (untested):
    MDO4xxx, MSO4xxx, and DPO4xxx.

    Parameters
    ----------
    connection: VisaConnection
        The VISA address (requires the CONNECTION_MDO3XXX node).
    channel: int
        The channel to set as the triggering channel (used if set=True).
    query_set: str
        Whether to query or set the triggering channel.

    Returns
    -------
    DataContainer
        TextBlob: The triggering channel (e.g. CH1).
    """

    tek = connection.get_handle()

    match query_set:
        case "query":
            s = tek.trigger.source()
        case "set":
            tek.trigger.source(f"CH{1 + channel}")
            s = f"CH{1 + channel}"

    return TextBlob(text_blob=s)
