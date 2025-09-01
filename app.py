import asyncio
import logging
from multiprocessing.spawn import freeze_support

from app_factory import create_app
from nacos_mcp import NacosMCP

app=create_app()
logger = logging.getLogger(__name__)


async def main(**kwargs):
    import uvicorn
    config = uvicorn.Config(app=app, host=app.config.APP_HOST, port=app.config.APP_PORT, **kwargs)
    if isinstance(app.mcp,NacosMCP):
        await app.mcp.register_service(app.config.TRANSPORT_TYPE)
    await uvicorn.Server(config).serve()


if __name__ == '__main__':
    freeze_support()
    asyncio.run(main())