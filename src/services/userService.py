import bcrypt
from prisma.errors import UniqueViolationError
from fastapi import HTTPException
from src.repositories.userRepository import UserRepository
from src.schemas.userSchema import UserCreate, UserResponse, UserUpdate
from src.models.user import User

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    async def create_user(self, user_data: UserCreate) -> UserResponse:
        data = user_data.dict()
        data['password'] = self.hash_password(data['password'])
        try:
            user: User = await self.repository.create(data)
            return UserResponse(**user.to_dict())
        except UniqueViolationError as e:
            # Verifica qual campo causou a violação de unicidade
            if "email" in str(e):
                raise HTTPException(
                    status_code=400,
                    detail="O email informado já está registrado."
                )
            elif "username" in str(e):
                raise HTTPException(
                    status_code=400,
                    detail="O nome de usuário informado já está registrado."
                )
            elif "cpfCnpj" in str(e):
                raise HTTPException(
                    status_code=400,
                    detail="O CPF/CNPJ informado já está registrado."
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Um valor único já está registrado no sistema."
                )

    async def get_user(self, user_id: str) -> UserResponse | None:
        user: User = await self.repository.find_by_id(user_id)
        return UserResponse(**user.to_dict()) if user else None

    async def get_all_users(self) -> list[UserResponse]:
        users: list[User] = await self.repository.find_all()
        return [UserResponse(**user.to_dict()) for user in users]

    async def update_user(self, user_id: str, user_data: UserUpdate) -> UserResponse:
        data = {k: v for k, v in user_data.dict().items() if v is not None}
        if 'password' in data:
            data['password'] = self.hash_password(data['password'])
        user: User = await self.repository.update(user_id, data)
        return UserResponse(**user.to_dict())

    async def delete_user(self, user_id: str) -> UserResponse:
        user: User = await self.repository.delete(user_id)
        return UserResponse(**user.to_dict())