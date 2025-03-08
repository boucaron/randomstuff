# Microservices Patterns with examples in Java - Chris Richardson

## Intro 

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

## Decomposition Strategies

The chapter begins with a brief introduction to software architecture and its variations.

Following that, the author presents the following definitions:

 'A service is a standalone, independently deployable software component that implements some useful functionality'
'There are two types of operations: commands and queries. The API consists of commands, queries, and events.'
'A service’s API encapsulates its internal implementation. Unlike in a monolith, a developer can’t write code that bypasses its API. As a result, the microservice architecture enforces the application’s modularity.
'Each service in a microservice architecture has its own architecture and, potentially, technology stack. But a typical service has a hexagonal architecture. Its API is implemented by adapters that interact with the service’s business logic. The operations adapter invokes the business logic, and the events adapter publishes events emitted by the business logic.'
'All interaction with a service happens via its API, which encapsulates its implementation details. This enables the implementation of the service to change without impacting its clients. Loosely coupled services are key to improving an application’s development time attributes, including its maintainability and testability. They are much easier to understand, change,and test.'
'The requirement for services to be loosely coupled and to collaborate only via APIs prohibits services from communicating via a database'

This section presents an important aspect of microservices architecture: modularity. Services are designed to be independent, with each one exposing a clear API that acts as the only point of interaction. This decoupling encourages flexibility and scalability, enabling teams to work on different services without affecting each other’s work.

However, let’s shift the focus to the practical implications of this modular approach, particularly in terms of maintenance.

With a microservices-based application, business logic is distributed across multiple services. This means that instead of one centralized codebase, the knowledge about how the system works is diffused across various services. Consequently, if you need to replace a developer, there is a longer learning curve, as they must understand multiple services. Additionally, debugging can become more difficult, as the interaction between services may not always be straightforward.

Now, let’s talk about the API-only scheme that microservices rely on. While this decoupling offers many advantages, it also introduces challenges. First, the communication between services often relies heavily on APIs, and this can lead to data duplication and consistency issues. In a distributed system, ensuring data consistency across services becomes a complex task, especially as the number of services grows. This risk of inconsistency can arise even if teams are not actively thinking about it, making it a key concern in the maintenance and scalability of microservices-based systems.

### Defining an application’s microservice architecture

So we start from the fundamentals:

From the author:
'An application exists to handle requests, so the first step in defining its architecture is
to distill the application’s requirements into the key requests'
'A system operation is an abstraction of a
request that the application must handle. It’s either a command, which updates data,
or a query, which retrieves data. The behavior of each command is defined in terms
of an abstract domain model, which is also derived from the requirements. The system
operations become the architectural scenarios that illustrate how the services
collaborate.'
'The second step in the process is to determine the decomposition into services.
There are several strategies to choose from. One strategy, which has its origins in the
discipline of business architecture, is to define services corresponding to business
capabilities. Another strategy is to organize services around domain-driven design subdomains.
The end result is services that are organized around business concepts
rather than technical concepts.'
'The third step in defining the application’s architecture is to determine each service’s
API. To do that, you assign each system operation identified in the first step to a
service. A service might implement an operation entirely by itself. Alternatively, it
might need to collaborate with other services. In that case, you determine how the services
collaborate, which typically requires services to support additional operations.'

At least we can start to talk about potential issues:

'There are several obstacles to decomposition. The first is network latency. You
might discover that a particular decomposition would be impractical due to too many
round-trips between services. Another obstacle to decomposition is that synchronous
communication between services reduces availability.'
'The third obstacle is the
requirement to maintain data consistency across services.'
'The fourth and final obstacle to decomposition is socalled
god classes, which are used throughout an application. Fortunately, you can use
concepts from domain-driven design to eliminate god classes.'


First step 'CREATING A HIGH-LEVEL DOMAIN MODEL'

'The application won’t even have a
single domain model because, as you’ll soon learn, each service has its own domain
model. Despite being a drastic simplification, a high-level domain model is useful at
this stage because it defines the vocabulary for describing the behavior of the system
operations.'

Second step 'DEFINING SYSTEM OPERATIONS'

'There are two types of system operations:
- Commands—System operations that create, update, and delete data
-  Queries—System operations that read (query) data'

#### Defining services by applying the Decompose by business capability pattern

'An organization’s business capabilities capture what an organization’s business is.
They’re generally stable, as opposed to how an organization conducts its business, which
changes over time, sometimes dramatically.'


