
-- Ajouter MD5 pour sécuriser les passwords
CREATE TABLE User (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(50),
    password VARCHAR(32)
);