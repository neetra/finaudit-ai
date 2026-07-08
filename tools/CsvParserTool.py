from agent_framework import tool
import pandas as pd


@tool
async def parse_csv( file_path):

        df = pd.read_csv(file_path)

        return df.to_dict("records")