# JPA Hibernate Usage

I started recently to work on a project with pretty poor DB Backend Implementation, to avoid to say a failed DB Backend Implementation.
As a software developper it is your job and your concern to understand the difference there is between having a DB schema and implementing a DB Mapping for your backend. 
What I mean by that is that you have to understand the DB schema you are using, you are not mimicking or copying this schema to the DB mapping your need for your backend. 
You are creating a DB Mapping to perform some tasks/queries for your business case. 
Also, most of the time, you can add things in the DB Schema to suit your need. 

Motivating example, you have a table with several foreign keys to other tables. The question is do you really need to have those foreign keys being resolved as Join when you map this table. The quick and good answer is No ! Why ? Simply forcing the foreign keys may force JPA/Hibernate to fetch additional data you do not need. Also, the fetch of those data may be very inefficient, and can litteraly kills both the DB server and your Backend. Now, I let you imagine what happens when you have strongly connected components in the foreign key chains. It means you are sending burst of queries and retrieving data that are not meaningful at all for your concern. Also, the mapping is static, even if you have Lazy loading features, if the data is mapped even indirectly... it will be fetched.


# Latency ! 
Let me explain the latency issue. Let say you have a 1 ms latency between your application server and your DB server. 
Example, you have a mapped table A with a foreign key mapped as a Join to another table B. 
You retrieve 1000 records from a single query, but what happens you have another 1000 queries that are sent to the DB to retrieve the foreign keys. In other words, you have 1 sql query to fetch the records for the mapped table A, BUT you have also 1000 sql queries to fetch those foreign keys.
This means you have 1 ms in one way and 1 ms in the other way for each single sql query sent to fetch the foreign keys: so (1 + 1) * 1000 = 2000 ms, so you have at least 2 s just due to the latency and of course increased CPU load on both the application and the DB server due to amount of context switches at the OS level to handle all those single and short requests.

# Static Mapping/Various Queries 
What is really important to undestand is the DB mapping is static (you map a table to a class). If I asked to retrieve a foreign key, it will be done for each query (actually you can use lazy loading to prevent, but it needs a lot discipline, and it is pretty easy to forget about it, especially it is hidden deeply in a call-stack). 
In the general case, we do not know all the queries that will be performed during the life of project. So asking all the time the foreign key is most of the time a mistake.

Let us extend to the context of having multiple foreign-keys, it will make even less sense to fetch those systematically: it depends on the query, sometimes you need no foreign key, sometimes a specific one, sometimes both of them and so on. From this perspective, the nature and the style of the query is very different. So it is very dangerous from a performance perspective to use a Join there.

Let think about the insert/update case. Let say you have a person mapped table with multiple addresses that are fetched as a Join. Each time you update the person, you can potentially update the addresses. Even if the query is not sent: you will have JPA/Hibernate under the hood performing several checks on various data fields that are not concerned, before sending the queries to the DB server.

So keep things simple and stupid: if you want performance, simplify the maintenance and the testing: do not map a table with its foreign keys.

# Handling Join

So you will tell, ok I need to handle the join. Yes, no problem you can handle it at the Query level. 
It means you are going to create specific calls in your DAO, your service and your controller to handle those cases.
In some case, it makes totally sense to create DB views and having different mapped objects to address your specific needs and to prevent having burst of calls being sent to the DB as we discussed earlier.
Yes, it takes a bit more time to create, but on the long run, it wins.

# Control and Maintenance
Having specific apis  mean you will have more control on how the things are structured in your backend, your needs and intentions are more exposed.
So, if you have someone doing the maintenance on the project, the person will understand that she/he can introduce custom queries to manage the need and to ensure good performance.
You will not have a simpler backend but something adapted on your needs where you have control.
This means you can have different business objects, controllers, services that are really linked to the nature of the query, and you can modify and optimise those without causing anything harm to other parts of the project. The mapped tables are simple and systematically free from any performance bottleneck by construction.

So, do not use Join tables in your mapping if you are not really sure you need them all the time along the life of your project !





