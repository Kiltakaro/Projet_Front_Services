from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBaseModel(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Nom d'utilisateur unique")
    email: EmailStr = Field(..., description="Adresse email de l'utilisateur")
    password: str = Field(..., min_length=8, max_length=128, description="Mot de passe de l'utilisateur")

    class Config:
        orm_mode = True  # Cela permet de convertir facilement le modèle en objet ORM pour les interactions avec la base de données.

# Exemple d'utilisation
# Utilisé lors de la création d'un utilisateur (reçoit un utilisateur avec des valeurs spécifiques).
class UserCreate(UserBaseModel):
    pass

# Modèle pour la réponse, où le mot de passe ne serait pas renvoyé
class UserResponse(UserBaseModel):
    id: int

    class Config:
        orm_mode = True
