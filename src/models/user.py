from prisma.models import User as PrismaUser
from typing import Optional

class User:
    def __init__(self, prisma_user: PrismaUser):
        self.id = prisma_user.id
        self.name = prisma_user.name
        self.phone = prisma_user.phone
        self.email = prisma_user.email
        self.username = prisma_user.username
        self.password = prisma_user.password
        self.cpfCnpj = prisma_user.cpfCnpj
        self.cep = prisma_user.cep
        self.rua = prisma_user.rua
        self.numero = prisma_user.numero
        self.bairro = prisma_user.bairro
        self.cidade = prisma_user.cidade
        self.estado = prisma_user.estado
        self.complemento = prisma_user.complemento
        self.isActive = prisma_user.isActive
        self.isAdmin = prisma_user.isAdmin

    @classmethod
    def from_prisma(cls, prisma_user: PrismaUser) -> 'User':
        return cls(prisma_user)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "cpfCnpj": self.cpfCnpj,
            "cep": self.cep,
            "rua": self.rua,
            "numero": self.numero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "complemento": self.complemento,
            "isActive": self.isActive,
            "isAdmin": self.isAdmin
        }