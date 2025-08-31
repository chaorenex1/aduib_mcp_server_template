import mcp.types as types

from app import app


# @app.mcp.list_tools
async def handle_list_tools() -> list[types.Tool]:
    return []