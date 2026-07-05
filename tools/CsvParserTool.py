import pandas as pd
from tools.BaseTool import BaseTool


class CsvParserTool(BaseTool):

    def __init__(self):
        super().__init__("CSV File Parser Tool")

    async def execute(self, file_path):

        df = pd.read_csv(file_path)

        return df.to_dict("records")