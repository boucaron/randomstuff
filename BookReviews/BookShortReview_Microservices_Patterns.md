# Microservices Patterns with examples in Java - Chris Richardson

Microservices have been a trending topic for a few years, often discussed alongside Agile. In the introduction, the author acknowledges that microservices are not a ‘silver bullet.’ However, in the list of cons, he does not fully address the real costs in terms of both infrastructure and communication overhead. A true microservices architecture demands more computational resources and introduces additional communication complexity—not just in system interactions but also in coordination between teams.

For smaller applications with fewer than a thousand peak concurrent users, a monolithic approach is often the better choice. Alternatively, a hybrid architecture can provide a middle ground, where specific functionalities—such as email notifications—are offloaded to independent services like a queue-based microservice, preventing the monolith from being slowed down by non-critical tasks.

How your company or institution is organized and how it handles communication is critical, as it will have a significant impact—particularly on responsibility and decision-making. If your organization operates in silos with minimal communication, adopting a microservices architecture will be challenging.

In many cases, a small, cross-functional team (often two to three people) is responsible for managing a microservice end-to-end, ensuring smooth operation and accountability. However, if your company is structured with separate departments handling different aspects of development and operations, you may face increased delays, fragmented knowledge, and reduced ownership. While some level of specialization is unavoidable in larger organizations, fostering efficient cross-team communication and clear responsibility is essential to mitigating these drawbacks.

Being lean is crucial—you don’t want to introduce unnecessary complexity too early due to design decisions made prematurely. That’s why measuring what’s happening in your application is essential; you need to face reality, adapt quickly, and iterate often.

While many architectural patterns are valuable, the ultimate goal is to solve real problems, not to create artificial ones for the sake of technical novelty. Some engineers can prioritize unnecessary complexity for the sake of technical novelty, which can lead to increased costs and decreased efficiency.

For example, with modern SSDs and multi-gigabit network interfaces, a single database server today can handle significantly more data and computation than the mainframes that processed an entire country’s tax system 40 years ago.

Scalability is important, but it requires the right balance. That’s why it’s crucial to deeply understand and measure how your application or service is actually being used. Without real insights, you risk over-engineering or making premature optimizations that add unnecessary complexity.

These optimizations can make future redesigns either prohibitively expensive or extremely difficult, locking you into decisions that may no longer be optimal as your needs evolve.

The author references the classic Mythical Man-Month issue, emphasizing that teams should remain small—ideally under ten people. Following this, he suggests that each microservice should typically be managed by a team of two to three people.

However, I would argue that the number of microservices is just as critical as team size. As the number of microservices increases, system complexity grows exponentially, much like how a larger team becomes harder to manage. To avoid unnecessary overhead, it's essential to take a lean approach when designing and scaling microservices.

