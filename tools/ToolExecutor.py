class ToolExecutor:

    def __init__(self, registry):

        self.registry = registry

    async def execute(self, tool_name, **kwargs):

        tool = self.registry.get(tool_name)

        return await tool.execute(**kwargs)