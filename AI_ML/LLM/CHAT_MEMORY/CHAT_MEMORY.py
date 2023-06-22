from flojoy import flojoy, DataContainer
from flojoy.langchain.chat_models import ChatOpenAI
from flojoy.langchain.chains import ConversationChain
from flojoy.langchain.memory import ConversationBufferMemory, ConversationTokenBufferMemory, ConversationSummaryMemory
import numpy as np
import pandas as pd


@flojoy
def CHAT_MEMORY(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The CHAT_MEMORY node outputs the buffer storing conversation held with the chat language model in the form of string wrapped in dataframe.

    Parameters
    ----------
        prompt : str
        memory_type : 'ConversationBufferMemory' | 'ConversationTokenBufferMemory' | 'ConversationSummaryMemory', default='ConversationBufferMemory'


    Returns:
    --------
    DataContainer:
        type 'dataframe' containing the conversation

    """
    prompt : str = params["prompt"]
    memory : str = params["memory_type"]


    llm = ChatOpenAI(temperature=0.0)
    memory = ConversationBufferMemory()
    
    conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
    )

    conversation.predict(input=prompt)



    df_pred = pd.DataFrame.from_records([(pred,)], columns=["output"])

    return DataContainer(type="dataframe", m=df_pred)
