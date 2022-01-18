# SLQ & Docker 

## Set SQL container 


Pull the latest mysql from the docker hub 

```
docker pull mysql:latest
```

Run the container with proper flag 

```
docker run --name=user_mysql_1 --env="MYSQL_ROOT_PASSWORD=root_password" -p 3306:3306 -d mysql:latest
```

or with the following `Dockerfile`

```
FROM mysql

ENV MYSQL_DATABASE=mysqlsampledatabase \
    MYSQL_ROOT_PASSWORD=root_password

EXPOSE 3306
```

check it with `docker ps` command. 

## Create and populate database 

Access mysql docker container 

```
docker exec -it user_mysql_1 mysql -uroot -proot_password
```

## With a sql init file is better

```
FROM mysql

ENV MYSQL_DATABASE=mysqlsampledatabase \
    MYSQL_ROOT_PASSWORD=root_password

ADD init.sql /docker-entrypoint-initdb.d

EXPOSE 3306
```


### Generate data 
You can use : https://www.generatedata.com

## Create user and access the database 

First show mysql users: 
 
```
mysql> select host, user from mysql.user;
```

create a user name `newuser`

```mysql
mysql> CREATE USER 'newuser'@'%' IDENTIFIED BY 'newpassword';
```

puis 

```mysql
mysql> GRANT ALL PRIVILEGES ON my_database.* to 'newuser'@'%';
```

show users privileges

```
mysql> SHOW GRANTS;
```

show privileges for user_name

```
mysql> SHOW GRANTS FOR 'user_name';
```



## Écrire un script python afin de se connecter au container et effectuer les opération CRUD





## Querries 

1. Préparez une liste de bureaux triés par pays, état, ville.
- Combien d'employés y a-t-il dans l'entreprise?
- Quel est le total des paiements reçus?
- Dressez la liste des lignes de produits contenant des «Voitures».
- Déclarez le total des paiements pour le 28 octobre 2004.
- Déclarez les paiements supérieurs à 100 000$
- Énumérez les produits de chaque gamme de produits.
- Combien de produits dans chaque gamme de produits?
- Quel est le paiement minimum reçu?
- Répertoriez tous les paiements supérieurs à deux fois le paiement moyen.
- Quelle est la majoration moyenne en pourcentage du PDSF sur buyPrice?
- Combien de produits distincts ClassicModels vend-il?
- Indiquer le nom et la ville des clients qui n'ont pas de représentants commerciaux?
- Quels sont les noms des cadres avec VP ou Manager dans leur titre? Utilisez la fonction CONCAT pour combiner le prénom et le nom de l'employé dans un seul champ pour le reporting.
- Quelles commandes ont une valeur supérieure à 5 000 $?
- Afficher le représentant du compte pour chaque client ()
- Afficher le total des paiements pour Atelier graphique.
- Afficher le total des paiements par date
- Afficher les produits qui n'ont pas été vendus.
- Afficher le montant payé par chaque client.
- Indiquez le nombre de commandes «On Hold» (en attente) pour chaque client.
- Listez les produits commandés un lundi.
- Afficher tous les produits achetés par Herkku Gifts.
- Pour les commandes contenant plus de deux produits, indiquez les produits qui constituent plus de 50% de la valeur de la commande. 

----- 


## TP 

### Expected output
```
 - - - MySQL Docker Container Python connection ok - - - 

 - - - docker ps info - - - 
b'CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES\nffeb1104c6f1        sqlc:01             "docker-entrypoint.s\xe2\x80\xa6"   5 days ago          Up 5 days           0.0.0.0:3306->3306/tcp   hardcore_kilby\n'
 - - - MySQL Database `classicmodels` connection ok - - - 

 - - - Data Mapping OK - - - 

 - - - Tables into database - - - 

		 - offices
		 - payments
		 - productlines
		 - employees
		 - products
		 - customers
		 - orders
		 - orderdetails

 - - - Selection of PAYMENTS Table - - - 

	 Type : <class 'sqlalchemy.sql.schema.Column'>

	 Columns : ['customerNumber', 'checkNumber', 'paymentDate', 'amount']


### All Payments with date > 01 June 2005:
242 payed 12432.3200000000 on 2005-06-03
353 payed 46656.9400000000 on 2005-06-09


 - - - Connection Close - - - 
```


## Ressources : 

- SQLAlchemy doc : https://docs.sqlalchemy.org/
- https://www.richardtwatson.com/dm6e/Reader/ClassicModels.html 
- git : https://github.com/harsha547/ClassicModels-Database-Queries/tree/master/challenges
- NICE BLOG ON SQLALCHEMY : https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/?utm_source=medium&utm_medium=sc&utm_campaign=sqlalchemy_python



