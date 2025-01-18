# Utiliser l'image officielle de Node.js
FROM node:18

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers package.json et package-lock.json pour installer les dépendances
COPY package.json package-lock.json ./

# Installer Angular CLI globalement
RUN npm install -g @angular/cli

# Installer les dépendances du projet
RUN npm install

# Copier le reste du code source de l'application
COPY . .

# Exposer le port 4200 pour le serveur Angular
EXPOSE 4200

# Lancer l'application Angular
CMD ["ng", "serve", "--host", "0.0.0.0"]

