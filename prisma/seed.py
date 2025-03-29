from prisma import Prisma
import asyncio
import bcrypt

async def main():
    db = Prisma()
    await db.connect()

    # Função auxiliar para gerar hash da senha
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Senha em texto puro que será criptografada
    plain_password = "admin123"
    
    await db.user.create({
        "name": "Admin User",
        "email": "admin@example.com",
        "username": "admin",
        "password": hash_password(plain_password),  # Criptografando a senha
        "cep": "12345-678",
        "rua": "Rua Principal",
        "numero": "100",
        "bairro": "Centro",
        "cidade": "São Paulo",
        "estado": "SP",
        "isActive": True,
        "isAdmin": True
    })
    
    print(f"Usuário admin criado com sucesso! Senha em texto puro: {plain_password}")
    await db.disconnect()

if __name__ == "__main__":
    asyncio.run(main())