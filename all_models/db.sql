-- Création de la base de données
drop database if exists Gestion_Stock_EPL;
CREATE DATABASE IF NOT EXISTS Gestion_Stock_EPL;
USE Gestion_Stock_EPL;

/*
-- Table Secrétaire Général
CREATE TABLE SecretaireGeneral (
    id_sec INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    mot_de_passe VARCHAR(255) NOT NULL, -- Utilisation de VARCHAR(255) pour stocker les hash de mot de passe
    departement VARCHAR(100) NOT NULL
);

-- Table Professeur
CREATE TABLE Professeur (
    id_prof INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    signature VARCHAR(50),
    mot_de_passe VARCHAR(255) NOT NULL -- Utilisation de VARCHAR(255) pour stocker les hash de mot de passe
);

-- Table Classe
CREATE TABLE Classe (
    id_classe INT AUTO_INCREMENT PRIMARY KEY,
    nom_licence VARCHAR(100) NOT NULL,
    niveau VARCHAR(50) NOT NULL,
    departement VARCHAR(100) NOT NULL
);

-- Table Secrétaire de Classe
CREATE TABLE SecretaireClasse (
    id_secc INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    mot_de_passe VARCHAR(255) NOT NULL, -- Utilisation de VARCHAR(255) pour stocker les hash de mot de passe
    id_classe INT,
    FOREIGN KEY (id_classe) REFERENCES Classe(id_classe) ON DELETE SET NULL
);



CREATE TABLE User  (
    `id` bigint AUTO_INCREMENT PRIMARY KEY,
    `password` varchar(128) NOT NULL,
    `last_login` datetime(6) NULL,
    `email` varchar(254) NOT NULL UNIQUE,
    `nom` varchar(150) NOT NULL,
    `prenom` varchar(150) NOT NULL,
    `role` varchar(23) NOT NULL,
    `auth_provider` varchar(10) NOT NULL DEFAULT 'email',
    `is_active` bool NOT NULL DEFAULT TRUE,
    `is_staff` bool NOT NULL DEFAULT FALSE,
    `is_verified` bool NOT NULL DEFAULT FALSE,
    `is_superuser` bool NOT NULL DEFAULT FALSE
);

CREATE TABLE Secretairegeneral (
    `id_sec` bigint AUTO_INCREMENT PRIMARY KEY,
    `user_id_sec` bigint NOT NULL UNIQUE,
    `departement` varchar(100) NOT NULL,
    CONSTRAINT `secretairegeneral_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`) ON DELETE CASCADE
);

CREATE TABLE Professeur (
    `id_prof` bigint AUTO_INCREMENT PRIMARY KEY,
    `user_id_prof` bigint NOT NULL UNIQUE,
    `signature` varchar(100) NULL,
    CONSTRAINT `professeur_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`) ON DELETE CASCADE
);

CREATE TABLE Secretaireclasse (
    `id_secc` bigint AUTO_INCREMENT PRIMARY KEY,
    `user_id_secc` bigint NOT NULL UNIQUE,
    `id_classe_id` bigint NULL,
    CONSTRAINT `secretaireclasse_user_id_fk` FOREIGN KEY (`user_id_secc`) REFERENCES `accounts_customuser` (`id`) ON DELETE CASCADE,
    CONSTRAINT `secretaireclasse_id_classe_id_fk` FOREIGN KEY (`id_classe_id`) REFERENCES `cahierdetexte_classe` (`id`)
);


-- Table UEs (Unités d'Enseignement)
CREATE TABLE UEs (
    id_UEs INT AUTO_INCREMENT PRIMARY KEY,
    code_UEs VARCHAR(50) NOT NULL UNIQUE,
    intitule_UEs VARCHAR(255) NOT NULL,
    id_prof INT,
    FOREIGN KEY (id_prof) REFERENCES Professeur(id_prof) ON DELETE SET NULL
);

-- Table Séance
CREATE TABLE Seance (
    id_seance INT AUTO_INCREMENT PRIMARY KEY,
    id_professeur INT,
    id_UEs INT,
    id_classe INT,
    sous_session_seance VARCHAR(1000),
    date_heure DATETIME NOT NULL,
    FOREIGN KEY (id_professeur) REFERENCES Professeur(id_prof) ON DELETE CASCADE,
    FOREIGN KEY (id_UEs) REFERENCES UEs(id_UEs) ON DELETE CASCADE,
    FOREIGN KEY (id_classe) REFERENCES Classe(id_classe) ON DELETE CASCADE
);

-- Table Cahier de Texte
CREATE TABLE CahierTexte (
    id_cahier INT AUTO_INCREMENT PRIMARY KEY,
    id_classe INT,
    id_secretaire INT,
    FOREIGN KEY (id_classe) REFERENCES Classe(id_classe) ON DELETE CASCADE,
    FOREIGN KEY (id_secretaire) REFERENCES SecretaireClasse(id_secc) ON DELETE CASCADE
);
-- Table Validation
CREATE TABLE Validation (
    id_validation INT AUTO_INCREMENT PRIMARY KEY,
    id_cahier INT,
    id_professeur INT,
    id_UEs INT,
    statut ENUM('validé', 'non validé') NOT NULL,
    id_seance INT,
    date_validation DATETIME NOT NULL,
    FOREIGN KEY (id_cahier) REFERENCES CahierTexte(id_cahier) ON DELETE CASCADE,
    FOREIGN KEY (id_professeur) REFERENCES Professeur(id_prof) ON DELETE CASCADE,
    FOREIGN KEY (id_UEs) REFERENCES UEs(id_UEs) ON DELETE CASCADE,
    FOREIGN KEY (id_seance) REFERENCES Seance(id_seance) ON DELETE CASCADE
);
-- Table Des fichier
CREATE TABLE Fichiers_Ue(
	id_Fichiers_Ue INT AUTO_INCREMENT PRIMARY KEY,
    id_UEs INT,
    Lien_Fichier VARCHAR(50),
    FOREIGN KEY (id_UEs) REFERENCES Ues(id_Ues) ON DELETE CASCADE
            );

-- Index pour optimiser les recherches
CREATE INDEX idx_email ON User (email);
CREATE INDEX idx_role ON User (role);
CREATE INDEX idx_is_active ON User (is_active);
CREATE INDEX idx_is_staff ON User (is_staff);
CREATE INDEX idx_is_verified  ON User (is_verified);

CREATE INDEX idx_user_id_prof ON Professeur(user_id);
CREATE INDEX idx_user_id_secc ON SecretaireClasse(user_id_secc);
CREATE INDEX idx_user_id_sec ON Secretairegeneral(user_id_sec);

CREATE INDEX idx_code_UEs ON UEs(code_UEs);
CREATE INDEX idx_date_heure ON Seance(date_heure);
CREATE INDEX idx_statut ON Validation(statut);*/

-- Création de la base de données
DROP DATABASE IF EXISTS Gestion_Stock_EPL;
CREATE DATABASE IF NOT EXISTS Gestion_Stock_EPL;
USE Gestion_Stock_EPL;

-- Table User
CREATE TABLE User (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME(6) NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    nom VARCHAR(150) NOT NULL,
    prenom VARCHAR(150) NOT NULL,
    role VARCHAR(23) NOT NULL,
    auth_provider VARCHAR(10) NOT NULL DEFAULT 'email',
    is_active BOOL NOT NULL DEFAULT TRUE,
    is_staff BOOL NOT NULL DEFAULT FALSE,
    is_verified BOOL NOT NULL DEFAULT FALSE,
    is_superuser BOOL NOT NULL DEFAULT FALSE
);

-- Table Classe
CREATE TABLE Classe (
    id_classe BIGINT AUTO_INCREMENT PRIMARY KEY,
    nom_licence VARCHAR(100) NOT NULL,
    niveau VARCHAR(50) NOT NULL,
    departement VARCHAR(100) NOT NULL
);

-- Table SecretaireGeneral
CREATE TABLE SecretaireGeneral (
    id_sec BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id_sec BIGINT NOT NULL UNIQUE,
    departement VARCHAR(100) NOT NULL,
    FOREIGN KEY (user_id_sec) REFERENCES User(id) ON DELETE CASCADE
);

-- Table Professeur
CREATE TABLE Professeur (
    id_prof BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id_prof BIGINT NOT NULL UNIQUE,
    signature VARCHAR(255) NULL,
    FOREIGN KEY (user_id_prof) REFERENCES User(id) ON DELETE CASCADE
);

-- Table SecretaireClasse
CREATE TABLE SecretaireClasse (
    id_secc BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id_secc BIGINT NOT NULL UNIQUE,
    id_classe_id BIGINT NULL,
    FOREIGN KEY (user_id_secc) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (id_classe_id) REFERENCES Classe(id_classe) ON DELETE SET NULL
);

-- Table UEs
CREATE TABLE UEs (
    id_UEs BIGINT AUTO_INCREMENT PRIMARY KEY,
    code_UEs VARCHAR(50) NOT NULL UNIQUE,
    intitule_UEs VARCHAR(255) NOT NULL,
    id_prof BIGINT,
    FOREIGN KEY (id_prof) REFERENCES Professeur(id_prof) ON DELETE SET NULL
);

-- Table Seance
CREATE TABLE Seance (
    id_seance BIGINT AUTO_INCREMENT PRIMARY KEY,
    id_professeur BIGINT,
    id_UEs BIGINT,
    id_classe BIGINT,
    sous_session_seance VARCHAR(1000),
    date_heure DATETIME NOT NULL,
    FOREIGN KEY (id_professeur) REFERENCES Professeur(id_prof) ON DELETE CASCADE,
    FOREIGN KEY (id_UEs) REFERENCES UEs(id_UEs) ON DELETE CASCADE,
    FOREIGN KEY (id_classe) REFERENCES Classe(id_classe) ON DELETE CASCADE
);

-- Table CahierTexte
CREATE TABLE CahierTexte (
    id_cahier BIGINT AUTO_INCREMENT PRIMARY KEY,
    id_classe BIGINT,
    id_secretaire BIGINT,
    FOREIGN KEY (id_classe) REFERENCES Classe(id_classe) ON DELETE CASCADE,
    FOREIGN KEY (id_secretaire) REFERENCES SecretaireClasse(id_secc) ON DELETE CASCADE
);

-- Table Validation
CREATE TABLE Validation (
    id_validation BIGINT AUTO_INCREMENT PRIMARY KEY,
    id_cahier BIGINT,
    id_professeur BIGINT,
    id_UEs BIGINT,
    statut ENUM('validé', 'non validé') NOT NULL,
    id_seance BIGINT,
    date_validation DATETIME NOT NULL,
    FOREIGN KEY (id_cahier) REFERENCES CahierTexte(id_cahier) ON DELETE CASCADE,
    FOREIGN KEY (id_professeur) REFERENCES Professeur(id_prof) ON DELETE CASCADE,
    FOREIGN KEY (id_UEs) REFERENCES UEs(id_UEs) ON DELETE CASCADE,
    FOREIGN KEY (id_seance) REFERENCES Seance(id_seance) ON DELETE CASCADE
);

-- Table Fichiers_Ue
CREATE TABLE Fichiers_Ue(
    id_Fichiers_Ue BIGINT AUTO_INCREMENT PRIMARY KEY,
    id_UEs BIGINT,
    Lien_Fichier VARCHAR(255),
    FOREIGN KEY (id_UEs) REFERENCES UEs(id_UEs) ON DELETE CASCADE
);

-- Index
CREATE INDEX idx_email ON User (email);
CREATE INDEX idx_role ON User (role);
CREATE INDEX idx_is_active ON User (is_active);
CREATE INDEX idx_is_staff ON User (is_staff);
CREATE INDEX idx_is_verified ON User (is_verified);