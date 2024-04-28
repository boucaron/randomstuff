# JPA Hibernate Usage


I recently began working on a project with a suboptimal database (DB) backend implementation, to put it lightly — perhaps even a failed one. As a software developer, it's imperative to discern the disparity between having a DB schema and implementing a DB mapping for your backend.

What I mean by this is that you must comprehend the DB schema you're utilizing; you're not merely mimicking or replicating this schema for the DB mapping required by your backend. Instead, you're creating a DB mapping to execute specific tasks/queries pertinent to your business case. Additionally, most of the time, you can augment the DB schema to align with your needs.

For instance, consider a table with multiple foreign keys to other tables. Do you truly need these foreign keys to be resolved as joins when mapping this table? The succinct and correct answer is: No! Why? Because enforcing the foreign keys may compel JPA/Hibernate to retrieve additional data that you don't require. Moreover, fetching this data could be highly inefficient, potentially overburdening both the DB server and your backend. Now, envision the repercussions when dealing with strongly connected components in the foreign key chains. This scenario results in bursts of queries being sent and irrelevant data being retrieved, which adds no value to your concerns. Furthermore, despite the availability of Lazy loading features, if the data is even indirectly mapped, it will be fetched.

# Understanding Latency in Database Queries
Let's delve into the latency issue. Imagine there's a 1 ms latency between your application server and your DB server. Consider a scenario where you have a table A mapped with a foreign key joined to another table B.

When you fetch 1000 records from table A with a single query, an additional challenge arises: retrieving the foreign keys. For each of the 1000 records, a separate query is sent to the DB to fetch the associated foreign keys from table B.

In essence, while you have 1 SQL query to fetch the records from table A, you now have 1000 SQL queries to fetch the foreign keys. This translates to a round-trip latency of 1 ms each way for every single SQL query sent to retrieve the foreign keys. Therefore, the total latency becomes (1 + 1) * 1000 = 2000 ms, resulting in at least 2 seconds solely due to latency.

Moreover, this spike in latency also escalates the CPU load on both the application and DB servers. The increased number of context switches at the OS level, necessary to handle numerous single and short requests, adds to the computational overhead.



# Static Mapping and Query Complexity
It's crucial to grasp that database mapping is static; each table is mapped to a class. When requesting a foreign key, it's retrieved for each query. Although lazy loading can mitigate this, it requires discipline, and oversight is common, especially buried deep within a call stack.

In most cases, we don't anticipate all queries throughout a project's lifespan. Therefore, requesting the foreign key every time is often a mistake.

Consider the complexity introduced by multiple foreign keys. Fetching them systematically becomes nonsensical; the necessity varies based on the query. Sometimes none are needed, other times specific ones, or perhaps all. Consequently, the query nature and style differ significantly. Using a join here poses a substantial performance risk.

Now, contemplate the insert/update scenario. Suppose a person's table is mapped with multiple addresses fetched via a join. Each time you update the person, you may potentially update the addresses. Even if the query isn't sent, JPA/Hibernate undertakes numerous checks on various data fields before contacting the DB server.

To optimize performance, simplify maintenance, and facilitate testing, adhere to the principle of simplicity: avoid mapping a table with its foreign keys.

# Customizing Join Handling
You might wonder how to handle joins effectively. The solution lies in managing them at the query level. This entails creating tailored calls in your DAO, service, and controller to address specific cases.

In certain scenarios, creating database views and employing different mapped objects to cater to your specific requirements can be advantageous. This approach helps prevent the influx of calls sent to the DB, as previously discussed.

While it may require more time to set up initially, the long-term benefits are significant. By investing effort upfront in crafting these solutions, you ultimately streamline operations and enhance efficiency over time.


# Enhanced Control and Maintenance
Utilizing specific APIs offers increased control over the structure of your backend, making your needs and intentions more transparent. This level of specificity empowers maintenance personnel to introduce custom queries to manage requirements and ensure optimal performance.

By eschewing join tables in mapping, you create a backend that is tailored to your needs, fostering a deeper understanding of the system's architecture. This approach facilitates the introduction of custom queries without compromising the integrity of other project components.

Furthermore, having distinct business objects, controllers, and services closely aligned with the nature of the query enables seamless modification and optimization. This flexibility ensures that adjustments can be made without adverse effects on other project areas.

In essence, refrain from using join tables in mapping unless their necessity is unequivocal throughout the project's lifecycle. By doing so, you construct a backend that is both adaptable and resilient, free from performance bottlenecks inherent in unnecessary mapping complexities.

As a developer, it's essential to possess the capability to write SQL queries and comprehend your database schema rather than solely depending on the database mappings created by others.





