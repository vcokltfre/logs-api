from aioredis import create_redis_pool
from randutils import formatstring


class Storage:
    async def init(self):
        if not hasattr(self, 'pool'):
            self.pool = await create_redis_pool("redis://redis")

    async def set(self, key, data, timeout: int = 3600 * 24 * 7):
        await self.init()
        return await self.pool.set(key, data, expire=timeout)

    async def get(self, key):
        await self.init()
        return await self.pool.get(key)

    async def new(self, text: str, name: str = None, timeout: int = None):
        if not name:
            name = formatstring("xxxxxxxx-xxxxxxxxxxxxxxxx-xxxxxxxx")

        if not timeout:
            timeout = 86400 * 365 * 5 # 5 years should be long enough

        await self.set(name, text, timeout)

        return name