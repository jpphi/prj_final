#----------------------------------------------------------------------------
#
# Création et sélection de la base de donnée
#
#----------------------------------------------------------------------------
CREATE DATABASE prj_co

USE prj_co

#----------------------------------------------------------------------------
#
# Création de tables
#
#----------------------------------------------------------------------------

# Création de la table utilisateur
CREATE TABLE utilisateur
(
	id_utilisateur INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    mdp VARCHAR(50),
    id_type_utilisateur INT
)

# Création et remplissage de la table type d'utilisateur
CREATE TABLE type_utilisateur
(
	id_type_utilisateur INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	type_utilisateur VARCHAR(20)
)

INSERT INTO type_utilisateur (type_utilisateur)
	VALUES ('Visiteur'),('Utilisateur'),('Super-utilisateur');


# Création et remplissage de la table connexion
CREATE TABLE connexion
(
	id_connexion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	date_connexion DATETIME,
	id_evenement INT,
	id_utilisateur INT
)

# Création et remplissage de la table evenement
CREATE TABLE evenement
(
	id_evenement INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	type_evenement VARCHAR(100)
)

INSERT INTO evenement (type_evenement)
	VALUES ('Connexion'),('Connexion à la page 1'),('Connexion à la page 2'),
			('Activation bouton 1 page 1'),('Déconnexion');

# Création de la table tentative_connexion
CREATE TABLE tentative_connexion
(
	id_tentative_connexion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    mdp VARCHAR(50),
    date_tentative_connexion DATETIME
)

#----------------------------------------------------------------------------
#
# Ajout des contraintes clé étrangère
#
#----------------------------------------------------------------------------

# Définir id_type_utilisateur comme clé étrangère à la table utilisateur
ALTER TABLE utilisateur 
	ADD FOREIGN KEY (id_type_utilisateur) REFERENCES type_utilisateur(id_type_utilisateur)
	
# Définir id_evenement comme clé étrangère à la table connexion
ALTER TABLE connexion 
	ADD FOREIGN KEY (id_evenement) REFERENCES evenement(id_evenement)
	
# Définir id_evenement comme clé étrangère à la table connexion
ALTER TABLE connexion 
	ADD FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur)
	

#----------------------------------------------------------------------------
#
# Remplissage de table
#
#----------------------------------------------------------------------------

# Remplissage de la table utilisateur
INSERT INTO utilisateur (nom, prenom, mdp, id_type_utilisateur)
	VALUES ('Phi', 'jp', 'jpphi',3), ('Toto', 'Alfred', 'TotoA',1), ('Bonnot','Jean','BonnotJ',2);
	
	
####################################################################

use	Netflix_python;

-- SELECT show_id, nt.title , ns.title FROM netflix_titles nt
-- INNER JOIN netflix_shows ns 
-- ON nt.title = ns.title;

-- SELECT * FROM netflix_shows ns ;


-- # Doublons dans les tables
-- SELECT   COUNT(*) AS nbr_doublon, title, rating, ratingLevel 
-- FROM     netflix_shows
-- GROUP BY title,rating 
-- HAVING   COUNT(*) > 1;

--  # Suppression des doublons dans la table netflix_shows 
-- DELETE 
-- FROM   netflix_shows
-- WHERE  netflix_shows.title IN (
--                        SELECT ns.title 
--                        FROM   netflix_shows as ns 
--                        GROUP BY ns.title
--                        HAVING COUNT(ns.title) > 1
--                       )

# Suppression des doublons dans la table netflix_titles
-- DELETE
-- FROM   netflix_titles
-- WHERE  netflix_titles.show_id IN (
--                        SELECT MAX(nt.show_id) 
--                        FROM   netflix_titles as nt 
--                        GROUP BY nt.title, nt.`type` ,nt.release_year, nt.director,nt.duration
--                        HAVING COUNT(nt.title) > 1
--                       )
                      
-- SELECT   COUNT(*) AS nbr_doublon, show_id ,title, nt.`type` ,release_year 
-- FROM     netflix_titles nt 
-- GROUP BY title, nt.`type`,release_year 
-- HAVING   COUNT(*) > 1;
-- 
-- SELECT   COUNT(*) AS nbr_doublon, title, ns.`release year` 
-- FROM     netflix_shows ns 
-- GROUP BY title, ns.`release year` 
-- HAVING   COUNT(*) > 1;

# Création de vue avec les doublons
-- CREATE view vue1 (titre,annee,class) AS
-- SELECT   title, ns.`release year` , ns.rating
-- FROM     netflix_shows ns 
-- where title IN(
-- 	SELECT title from netflix_shows ns2 
-- 	group by ns2.title, ns2.`release year`, ns2.rating 
-- 	HAVING   COUNT(title)> 1 )
-- ORDER by title ASC;
-- 
-- SELECT *, COUNT(*) as cpt FROM vue1 v group by titre,annee,class HAVING cpt >1
-- 
-- CREATE VIEW vue2 (titre2, annee2, class2, cpt) as
-- SELECT *, COUNT(*) FROM vue1 v 
-- group by titre, annee, class 
-- 
-- SELECT titre2, annee2, class2,  COUNT(titre2) as cpt from vue2 v 
-- group by titre2 , annee2 
-- having cpt>1

# Creation de la table show sans doublon (préférable que de supprimer les doublons dans la table original)
-- CREATE TABLE shows AS
-- SELECT * FROM netflix_shows ns
-- WHERE ns.title IN (
-- 	SELECT title from netflix_shows
-- 	group by title , `release year` , rating 
-- 	HAVING COUNT(title) = 1)
-- ORDER BY title ASC ;


# Creation de la table titles sans doublon (préférable que de supprimer les doublons dans la table original)
-- CREATE TABLE title AS
-- SELECT * FROM netflix_titles nt 
-- WHERE nt.title IN (
-- 	SELECT title from netflix_titles nt 
-- 	group by nt.title , 
-- 	HAVING COUNT(nt.title) = 1)
-- ORDER BY title ASC ;

# creation table sans doublon netflix_titles 
-- CREATE TABLE titles AS
-- select * from netflix_titles nt 
-- where nt.title in(
-- 	SELECT title from netflix_titles nt2
-- 	group by title, `type` , director, release_year
-- 	HAVING COUNT(title)= 1)
-- ORDER by nt.show_id ASC 

# creation d'une clé primaire
#ALTER TABLE shows ADD num int not null AUTO_increment primary key;

# change nom colonnes
# ALTER TABLE shows CHANGE num show_id int;

#ALTER TABLE shows change liste_in listed_in VARCHAR(80)

#ALTER TABLE shows CHANGE `release year` release_year int

# union des tables
-- create TABLE tout as
-- select `type`, title, director, `cast`, country, date_added, release_year,
-- rating, duration, listed_in, description, ratingLevel,ratingDescription, user_rating_score,
-- user_rating_size FROM  shows s 
-- union
-- select  `type`, title, director, `cast`, country, date_added, release_year,
-- rating, duration, listed_in, description, ratingLevel,ratingDescription, user_rating_score,
-- user_rating_size from titles t 
-- 
-- select * from tout 
-- where tout.title IN (
-- 	SELECT tout.title from tout
-- 	group by title
-- 	having count(title)> 1)
-- order by title ASC 

-- SELECT * 
-- FROM shows 
-- WHERE shows.title IN (
-- 	SELECT title from shows
-- 	group by title , `release year` , rating 
-- 	HAVING COUNT(title) > 1)
-- ORDER BY title ASC ;


-- DELETE 
-- FROM shows 
-- WHERE shows.title IN (
-- 	SELECT title from shows
-- 	group by title , `release year` , rating 
-- 	HAVING COUNT(title) > 1);

#DELETE from shows WHERE num= 34



#films communs à shows et titles
/*
CREATE VIEW vue3 ( `type`, title, director, `cast`, country, date_added, release_year ,
rating, duration, listed_in, description, ratingLevel, ratingDescription, user_rating_score,
user_rating_size ) as
	SELECT DISTINCT  t.`type` , t.title, t.director, t.`cast`, t.country, t.date_added, t.release_year ,
	s.rating, t.duration, t.listed_in, t.description, s.ratingLevel, s.ratingDescription, s.user_rating_score,
	s.user_rating_size 
	from titles as t
	join shows as s
	WHERE t.title = s.title 
	and t.release_year = s.release_year  #and t.rating = s.rating quelques différences d'écriture nous conduise à prendre le rating de shows 
	order by t.title ASC 
*/


#titre communs à vue3 et titles mais release_year différent
/*
CREATE VIEW vue4 ( `type`, title, director, `cast`, country, date_added, release_year ,
rating, duration, listed_in, description, ratingLevel, ratingDescription, user_rating_score,
user_rating_size ) as
SELECT DISTINCT  t.`type` , t.title, t.director, t.`cast`, t.country, t.date_added, t.release_year , 
v3.rating, t.duration, t.listed_in, t.description, v3.ratingLevel, v3.ratingDescription,
v3.user_rating_score, v3.user_rating_size 
from titles as t
join vue3 as v3
WHERE t.title = v3.title 
and t.release_year != v3.release_year  #and t.rating = s.rating quelques différences d'écriture nous conduise à prendre le rating de shows 
order by t.title ASC 
*/
	
#titre communs à vue3 et shows mais release_year différent
/*
CREATE VIEW vue5 ( `type`, title, director, `cast`, country, date_added, release_year ,
rating, duration, listed_in, description, ratingLevel, ratingDescription, user_rating_score,
user_rating_size ) as
SELECT DISTINCT  s.`type` , s.title, s.director, s.`cast`, s.country, s.date_added, s.release_year , 
v3.rating, s.duration, s.listed_in, s.description, v3.ratingLevel, v3.ratingDescription,
v3.user_rating_score, v3.user_rating_size 
from shows as s
join vue3 as v3
WHERE s.title = v3.title 
and s.release_year != v3.release_year  #and t.rating = s.rating quelques différences d'écriture nous conduise à prendre le rating de shows 
order by s.title ASC 
	
# creation de vue345 union de vues3 vue4 et vue5
CREATE VIEW vue345 ( `type`, title, director, `cast`, country, date_added, release_year ,
rating, duration, listed_in, description, ratingLevel, ratingDescription, user_rating_score,
user_rating_size ) as
select * FROM vue3
union
select * FROM vue4
union
select * FROM vue5
*/


#vue 6 titre ou release ou rating différent entre vue543 et titles
#BEAUCOUP TROP DE LIGNE CR2ER.....!!!!
-- CREATE VIEW vue6 ( `type`, title, director, `cast`, country, date_added, release_year ,
-- rating, duration, listed_in, description, ratingLevel, ratingDescription, user_rating_score,
-- user_rating_size ) as
-- SELECT DISTINCT  t.`type` , t.title, t.director, t.`cast`, t.country, t.date_added, t.release_year , 
-- v543.rating, t.duration, t.listed_in, t.description, v543.ratingLevel, v543.ratingDescription,
-- v543.user_rating_score, v543.user_rating_size 
-- from titles as t
-- join vue543 as v543
-- WHERE t.title != v543.title 
-- OR t.release_year != v543.release_year 
-- OR t.rating = v543.rating #quelques différences d'écriture nous conduise à prendre le rating de shows 
-- order by t.title ASC 

# Union des tables vue6, titles et shows
/*
CREATE VIEW vue6 ( `type`, title, director, `cast`, country, date_added, release_year ,
rating, duration, listed_in, description, ratingLevel, ratingDescription, user_rating_score,
user_rating_size ) as
select * FROM vue543
union
select `type`, title, director, `cast`, country, date_added, release_year ,
rating, duration, listed_in, description, ratingLevel, ratingDescription, user_rating_score,
user_rating_size FROM titles
union
select `type`, title, director, `cast`, country, date_added, release_year ,
rating, duration, listed_in, description, ratingLevel, ratingDescription, user_rating_score,
user_rating_size FROM shows


#Création de la vue7= vue6 sans les doublons
CREATE VIEW vue7 ( `type`, title, director, `cast`, country, date_added, release_year ,
rating, duration, listed_in, description, ratingLevel, ratingDescription, user_rating_score,
user_rating_size ) as
select * from vue6 v 
WHERE title in (
	SELECT title from vue6
	group by title, release_year
	HAVING COUNT(*) = 1)
	and ( ISNULL(ratingLevel) OR ISNULL(country) ) 

# cretion de la table tout à partir de la vue7
CREATE TABLE tout AS
select * from vue7 v
order by title 

# creation d'une clé primaire dans tout
ALTER TABLE tout ADD show_id int not null AUTO_increment primary key;

#### création des tables à partir de tout 

# creation de m_type + clé primaire
CREATE TABLE m_type AS
select distinct t.`type` from tout as t
order by t.`type` 

#PK
ALTER TABLE m_type ADD num_type int not null AUTO_increment primary key;

# creation de m_director + clé primaire
CREATE TABLE m_director AS
select distinct t.director from tout as t
order by t.director 

#PK
ALTER TABLE m_director ADD num_director int not null AUTO_increment primary key;

# creation de m_country + clé primaire
CREATE TABLE m_country AS
select distinct t.country from tout as t
order by t.country 

#PK
ALTER TABLE m_country ADD num_country int not null AUTO_increment primary key;

# creation de m_rating
CREATE TABLE m_rating AS
select distinct t.show_id, t.rating, t.ratingLevel, t.ratingDescription from tout as t
order by t.show_id # qq doublon ont été retiré à la main: même rating mais description null

# IL FAUT déclarer show_id en clé étrangère
ALTER TABLE m_rating
ADD CONSTRAINT show_id2 # la contrainte show_id existait déja !
  FOREIGN KEY (show_id)
  REFERENCES m_doc_diff(show_id)



# creation de m_rating_user
CREATE TABLE m_rating_user AS
select distinct t.show_id, t.user_rating_score, t.user_rating_size from tout as t
order by t.show_id # qq doublon ont été retiré à la main: même rating mais description null

# IL FAUT déclarer show_id en clé étrangère
ALTER TABLE m_rating_user
ADD CONSTRAINT show_id
  FOREIGN KEY (show_id)
  REFERENCES m_doc_diff(show_id)

# creation de la table doc_diff.... les valeurs type country et director seront supprimé
#  aprés création de clé étragère
CREATE TABLE m_doc_diff AS
select distinct t.show_id, t.title, t.`cast`, t.date_added, t.release_year, t.description, 
t.listed_in, t.duration,
t.`type`, t.director, t.country 
from tout as t
order by t.show_id # qq doublon ont été retiré à la main: même rating mais description null

# Ajout clé primaire  doc_diff
ALTER TABLE m_doc_diff ADD CONSTRAINT show_id  PRIMARY KEY (show_id)


#### Pour la liason avec la table m_type

# Ajout de la colonne qui contiendra la clé étragère
ALTER TABLE m_doc_diff ADD num_type int

# Ajout de clé étrangère
ALTER TABLE m_doc_diff
ADD CONSTRAINT num_type
  FOREIGN KEY (num_type)
  REFERENCES m_type(num_type)

# Update num_type 
UPDATE m_doc_diff SET num_type = 1
UPDATE m_doc_diff SET num_type = 2 WHERE `type` IN ("Movie")
UPDATE m_doc_diff SET num_type = 3 WHERE `type` IN ("TV Show")

# Suppression de la colonne type
ALTER TAble m_doc_diff drop `type`


#### lien table m_director m_doc_diff 

# Ajout de la colonne qui contiendra la clé étragère
ALTER TABLE m_doc_diff ADD num_director int

# Ajout de clé étrangère
ALTER TABLE m_doc_diff
ADD CONSTRAINT num_director
  FOREIGN KEY (num_director)
  REFERENCES m_director(num_director)

# mise à jour des valeurs de la clé étrangère
UPDATE m_doc_diff as mdd
join m_director as md
SET mdd.num_director = md.num_director 
WHERE mdd.director = md.director 

# On vérifie que les valeurs sont correctes
Select mdd.director, md.director ,md.num_director ,mdd.num_director 
from m_doc_diff as mdd 
join m_director md 
WHERE mdd.num_director != md.num_director and mdd.director = md.director 

# Suppression de la colonne director
ALTER TAble m_doc_diff drop director


#### lien table m_country m_doc_diff 

# Ajout de la colonne qui contiendra la clé étragère
ALTER TABLE m_doc_diff ADD num_country int

# Ajout de clé étrangère
ALTER TABLE m_doc_diff
ADD CONSTRAINT num_country
  FOREIGN KEY (num_country)
  REFERENCES m_country(num_country)

# mise à jour des valeurs de la clé étrangère
UPDATE m_doc_diff as mdd
join m_country as mc
SET mdd.num_country = mc.num_country 
WHERE mdd.country = mc.country 

# On vérifie que les valeurs sont correctes
Select mdd.country , mc.country ,mdd.num_country ,mc.num_country 
from m_doc_diff as mdd 
join m_country mc 
WHERE mdd.country = mc.country  and mdd.num_country != mc.num_country 

# Suppression de la colonne country
ALTER TAble m_doc_diff drop country











-- SELECT nt.title ,nt.release_year , ns.`release year`, nt.rating, ns.rating 
-- from netflix_titles as nt
-- join netflix_shows as ns
-- WHERE nt.title = ns.title 
-- and nt.rating != ns.rating 

# film differents
-- SELECT title FROM netflix_shows as ns 
-- WHERE ns.title NOT IN(
--    SELECT nt.title FROM netflix_titles as nt)
-- ORDER BY ns.title ASC;

# films communs
-- SELECT   COUNT(*) AS nbr_doublon, nt.show_id ,nt.title, nt.`type` ,release_year 
-- FROM     netflix_titles nt 
-- GROUP BY nt.title, nt.`type`, nt.release_year 
-- HAVING   COUNT(*) > 1
-- ORDER by nt.title ASC ;

-- SELECT    nt.show_id ,nt.title, nt.`type` ,release_year 
-- FROM     netflix_titles nt 
-- join netflix_shows ns 
-- WHERE nt.title = ns.title
-- ORDER by nt.title ASC ;

*/


