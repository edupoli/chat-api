from prisma import Prisma
from src.models.user import User

class UserRepository:
    def __init__(self):
        self.db = Prisma()

    async def connect(self):
        await self.db.connect()

    async def disconnect(self):
        await self.db.disconnect()

    async def create(self, data: dict) -> User:
        await self.connect()
        prisma_user = await self.db.user.create(data=data)
        await self.disconnect()
        return User.from_prisma(prisma_user)

    async def find_by_id(self, user_id: str) -> User | None:
        await self.connect()
        prisma_user = await self.db.user.find_unique(where={"id": user_id})
        await self.disconnect()
        return User.from_prisma(prisma_user) if prisma_user else None

    async def find_all(self) -> list[User]:
        await self.connect()
        prisma_users = await self.db.user.find_many()
        await self.disconnect()
        return [User.from_prisma(user) for user in prisma_users]

    async def update(self, user_id: str, data: dict) -> User:
        await self.connect()
        prisma_user = await self.db.user.update(where={"id": user_id}, data=data)
        await self.disconnect()
        return User.from_prisma(prisma_user)

    async def delete(self, user_id: str) -> User:
        await self.connect()
        prisma_user = await self.db.user.delete(where={"id": user_id})
        await self.disconnect()
        return User.from_prisma(prisma_user)