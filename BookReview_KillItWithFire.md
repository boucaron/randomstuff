## Marianne Bellotti - Kill It With Fire

Personnal note:
Kind of cool to find people sharing similar stuff and thinking I experienced.
At least I am not too crazy.
I fully agree that software is a leaving stuff, and if you don't take care of it, it will die
Some small missing stuff, reduce dependencies: 
will the library tool you use be there is few years (at least), 
if it is managed by one guy on his spare time 

Few citations from the Book that I like:

<<
This is why maintaining technology long term is so difficult. Although
blindly jumping onto new things for the sake of their newness is danger-
ous, not keeping up to date is also dangerous. As technology advances,
it collects more and more interfaces and patterns. It absorbs them from
other fields, and it holds on to historic elements that no longer make
sense. It builds assumptions around the most deeply buried characteris-
tics. Keep your systems the way they are for too long, and you get caught
trying to migrate decades of assumptions.
>>

<<
When I’m working on a legacy system, I always start off by evaluating the
prospective users. Who will be maintaining this system long term? What
technologies are they comfortable with? Who will be using this system
the most? How do they expect the system to work?
>>

<<
Unfortunately, when confronted with the troubles of existing sys-
tems, engineering teams tend to build the most momentum around
starting from scratch. Initiatives to repair and restore operational excel-
lence gradually, much the way one would fix up an old house, tend to
have few volunteers among engineering teams. That’s because Zajonc’s
mere-exposure effect has an upper bound. There’s a point where famil-
iarity breeds contempt.
>>

<<
As an example, Node.js and
React.js are both forms of JavaScript. These two technologies look con-
sistent, but they do different things and are built upon different abstrac-
tions. The fact that they are both forms of JavaScript doesn’t give Node.js
an edge when interacting with React.js over any other backend language
that an engineering team might choose instead. An engineer’s skill in
one does not necessarily translate to the other.
Artificial consistency can bring value to nontechnical processes. For
example, standardizing on one programming language makes recruiting,
hiring, and, ultimately, sharing engineering resources much easier. But
when the principal purpose of a modernization effort is to provide tech-
nical value, be careful not to be seduced by the assumption that things
that look the same, or that we use the same words to describe, actually
integrate better.
>>


<<
For
all that people talk about COBOL dying off, it is good at certain tasks. The
problem with most old COBOL systems is that they were designed at a
time when COBOL was the only option. If the goal is to get rid of COBOL,
I start by sorting which parts of the system are in COBOL because COBOL
is good at performing that task, and which parts are in COBOL because
there were no other tools available. Once we have that mapping, we
start by pulling the latter off into separate services that are written and
designed using the technology we would choose for that task today.
>>

<<
Organizations tend to underestimate the amount of work and level
of investment modernization requires. An unfortunate consequence of
that assumption is that they do not seek out expertise until they are in
trouble.
>>


<<
To be effective when you’re coming into a project that has already started, your role
needs to adapt. First you need to stop the bleeding, and then you can do
your analysis and long-term planning.
>>

Red-flags
<<
Meetings with ever-expanding invite lists sug-
gest something is wrong in that area of the project.
>>
- Long meetings
- Urgent meetings
<< and then there are the people who spend the time they could be
helping drafting excuses that explain why the failure is not their fault. >>
The larger the project, the larger the set of persons on the excuse side

Compounding problems
<<
Projects are rarely doomed
by one critical error. It’s far more likely that the organization was drown-
ing in dysfunctional structures for months leading up to the failure.
>>

<<
Meetings slow down work, which almost always leads to more
meetings. Career-minded leaders claim failure was beyond their con-
trol, implicitly blaming the team. They make their employees feel unsafe,
which encourages them to avoid the problem areas as well.
>>
-->
<<
If a project is failing, you need to earn both the trust and respect of
the team already at work to course-correct. The best way to do that is by
finding a compounding problem and halting its cycle.
>>

Classical stuff:
<<Mess: Fixing Things That Are Not Broken
They assume new technology is more advanced than older
technology.
● They aspire to artificial consistency.
● They confuse success with quality.
● They optimize past the point of diminishing returns.
>>


Monolith advantages --> tightly coupled, low complexity and level of abstraction, if something is broken it is easier to spot it
Once you have some real understanding of what your services are, then move to this.
If you have service oriented arch: it involves much more work when you have a real change on the infra or the arch
It is a balancing act << Once again, focus on the balance between complexity and coupling >>


Small team, small organization -> Monolith

<<Large organizations do well when they transition their
monoliths to services, because the problems around communication and
knowledge sharing that need to be solved to make complex systems work
are problems that large organizations have to solve anyway.>>


<<
Fixing things that are not broken means you’re taking on all the risks
of a modernization but will not be able to find the compelling value add
and build the momentum that keeps things going. Nontechnical stake-
holders will see time and money spent and not understand what the
point of it was. This demoralizes engineers and violates trust with the
team. Fixing the wrong thing makes it harder to secure the resources to
finish and makes it much harder to sell the organization on future mod-
ernization efforts that might be more necessary.
>>

<<Decisions motivated by wanting to avoid rewriting code later are usu-
ally bad decisions. In general, any decision made to please or impress
imagined spectators with the superficial elegance of your approach is a
bad one.>>

<<
Set the expectation that all systems need to be rewritten even -
tually. Engineers at the highest level write programs that have to be
revised. No one is smart enough to anticipate every new use case or
feature, every advancement in hardware, or every adjustment or shift
that might require code to be rewritten. 
>>

<<
Technology doesn’t need to
be beautiful or to impress other people to be effective, and all technol-
ogists are ultimately in the business of producing effective technology.
>>

<<
Technical debt rarely effects performance
in a predictable way. A system could badly need a refactor but look fine
on a monitoring dashboard until the day it falls apart all at once. 
>>

When Does Breaking Up Add Value ?


<<Monoliths can be scaled, but depending on how activity is grow-
ing, they may be difficult to scale efficiently. For example, if one part of
the system is using more resources than other parts, it makes sense to
change to an architecture that allows that piece to be given additional
resources while not affecting the other parts of the system.>>

--> It depends on the amount of people working on the monolith, the more raises additional 
friction, communication and it slows down. 
Spliting it makes sense -> 
<<
Breaking up the monolith into services that roughly correspond
to what each team owns means that each team can control its own
deploys. Development speeds up. Add a layer of complexity in the form of
formal, testable API specs, and the system can facilitate communication
between those teams by policing how they are allowed to change down-
stream interactions.
>>


The Compounding Problem: Diminishing Trust

<<
A modernization effort needs buy-in beyond engineering to be successful.
Spending time and money on changes that will have no visible impact on
the business or mission side of operations makes it hard to secure that
buy-in in the future.
>>

<<
Monolith breakups and other large-scale redesigns offer an opportu-
nity to change process as well as change code. A silver lining in fixing
something that is not broken can be found in treating the fix as an
opportunity to experiment with and improve engineering practices. If
the organization lacks proper testing, take the opportunity to build out
and mature test suites. If the organization doesn’t have monitoring, con-
sider what tools might work for the new architecture. If the organization
has never done incident response or on-call rotations, use the creation of
new services to establish those practices.
>>
Formal methods too


Mess: Forgotten and Lost Systems

<< Large organizations lose systems. I don’t mean the systems go down; I
mean the organizations forget they have them and occasionally lose the
records of their existence. >>
<< At some point, an
organization likely will start to create divisions and delegate ownership,
but that’s a game of musical chairs that will often leave some parts of the
architecture without a seat when the music stops.>>
<<Trace the movements of those early engineers as the software was
originally being built. What did they touch, and who owns it now?>>
<<Another option is to follow the money. >>


<<When we encountered systems that had been forgotten and we
couldn’t figure out what they were doing, we would usually just turn
them off and see what happened. >>
<< That means better monitoring, better documenta-
tion, and better processes for restoring services, but you can’t improve
any of that if you don’t occasionally fail.>>
<< If no one complained, we tended just to leave the system off and
move on. Having one less component to modernize was still a win.  >>


Mess: Institutional Failures
<<If a bad pattern is used in one part of a system, it’s everywhere in the
system.>>
<<
Once you’ve found a problem, the next step is to determine whether
it’s a pattern or just a mistake. Security vulnerabilities from out-of-date
dependencies are obviously not a pattern. Accidentally removing some-
thing that was once in the code is not a pattern. Not escaping inputs, stor-
ing secrets in plaintext, returning more information than the requester
needs—those are patterns.>>
<<Code-checking software can sometimes be useful in tracking down
all the instances of a bad pattern. But some problems do not reveal them-
selves easily and require actual human beings. >>



The Compounding Problem: No Owners


<< Problems that impact multiple organizational units require coordi-
nation across those boundaries to fix. The more importance an organiza-
tion gives those boundaries—building budgets and hiring cycles around
them—the more people at the top of those units will police their bound-
aries. This sets up political battles that are often self-reinforcing.
>>

Solution: Code Yellow
<<Systemic problems almost always appear midstream. When we find
them, I like to document these issues for the wider organization as BOLOs
(for be on the lookouts). We send out a short announcement explaining the
problem in plain English, pointing to specific examples we have found
and establishing a point of contact on our team for other teams to reach
out to if they find similar issues.>>
<<Broadly, these techniques are part of a methodology called Code
Yellow, which is a cross-functional team created to tackle an issue
critical to operational excellence. >>

--> Code Yellow: Small team outside the regular chain of command, central point of the effort. 
Code Yellow leader can pull all resources needed for the Code Yellow effort.
No representatives from other teams, only people able to implement the solution.
This is a temporary team to fix the issue.
<<The temporary nature of a Code Yellow is what helps conquer the political
 rivalries that otherwise make systemic problems harder to solve. >>

Running a Code Yellow

<< However, the leader need not necessarily be from engi-
neering. Product managers can make excellent Code Yellow leaders, as
can staff engineers and principal engineers.>>


Mess: Leadership Has Lost the Room

<<Losing the room is a sports term. It means a coach has lost the respect
of his or her players. The team, instead of following orders and working
together, struggles to self-organize.>>

<<
The organization had also been leaning on them to produce more
and more while cutting their staff and restricting their resources. I took
over that team after their old manager was fired, and it was obvious from
our first few conversations that the problem wasn’t their engineering
skills. They had been asked to improve a piece of legacy technology that
had not been updated in a while. It had almost no testing, no monitoring,
and a complex deploy process.
The reason the legacy system had not been updated in a while was
because the organization had been regularly refusing requests to staff a
team for the task or invest anything significant in resources. To top it off,
the whole infrastructure for this system that processed millions of trans-
actions had been maintained for years by one person.
>>
--> Problem: testing and finding the root of the problem.

Solution: Murder Boards
<<The way a murder board works is you put together a panel of experts
who will ask questions, challenge assumptions, and attempt to poke
holes in a plan or proposal put in front of them by the person or group
the murder board exercise is intended to benefit. It’s called a murder
board because it’s supposed to be combative. The experts aren’t just
trying to point out flaws in the proposal; they are trying to outright
murder the ideas.>>
<<Murder boards have two goals. The first is to prepare candidates for a
stressful event by making sure they have an answer for every question,
a response to every concern, and mitigation strategy for every foreseeable
problem. The second goal of a murder board is to build candidates’ confi-
dence. If they go into the stressful event knowing that they survived the
murder board process, they will know that every aspect of their plan or
testimony has been battle-tested.>>
<< It is useful to set some boundaries with the board. We do not use the
murder board space to dredge up old failures or grudges. >>
--> << Murder boards build confidence because they are survived. >>


Stopping the Bleed
<< Legacy modernization projects do not fail because one mistake was
made or something went wrong once. They fail because the organiza-
tion deploys solutions that actually reinforce unsuccessful conditions. If
you’re coming into a project in the middle, your most important task as a
leader is figuring out where those cycles are and stopping them.
>>


Design as Destiny
<<The US Army/Marine Corps Counterinsurgency Field Manual
put it best when it advised soldiers:
“Planning is problem solving, while design is problem setting.”

Problem-solving versus problem-setting is the difference between
being reactive and being responsive. Reactive teams jump around aimlessly.
Setbacks whittle away their confidence and their ability to coordinate.
Momentum is hard to maintain. Responsive teams, on the other hand,
are calmer and more thoughtful. They’re able to sort new information as it
becomes available into different scopes and contexts. They’re able to change
approaches without affecting their confidence, because design thinking
gives them insight into why the change happened in the first place.
>>

More About Follow-ups: Why vs. How
<< Both why questions and how questions can be useful. Why questions
broaden the boundaries of the research field by allowing unseen factors
and forces to be introduced into the data. How questions put you in the
minds of users so you can see those factors as they understand them. Why
questions often lead to how questions.>>
--> Start with the Why


<<
Conway’s original paper outlined not just how organizational struc-
ture influenced technology but also how human factors contributed to
its evolution.>>

Individual Incentives

<<Organizations end up with patchwork solutions because the tech
community rewards explorers. Being among the first with tales of doc-
umenting, experimenting, or destroying a piece of technology builds an
individual’s prestige. Pushing the boundaries of performance by adopt-
ing something new and innovative builds it even more so.>>

<<Typically, this manifests itself in one of three different patterns:
● Creating frameworks, tooling, and other abstraction layers to make
code that is unlikely to have more than one use case theoretically
“reusable”
● Breaking off functions into new services, particularly middleware
● Introducing new languages or tools to optimize performance for
the sake of optimizing performance (in other words, without any
need to improve an SLO or existing benchmark)>>

<<Most of the systems I work on rescuing are not badly built. They
are badly maintained. >>

Minor Adjustments as Uncertainty

<<The problem is we’re most likely not judging the odds correctly.
We’re overemphasizing failure that may be rare and underestimating
both the time it will take to complete the rewrite and the performance
gains of the rewrite itself. We are swapping a system that works and
needs to be adjusted for an expensive and difficult migration to some-
thing unproven.>>

Structuring the Team to Account for Past Failure

<<Legacy modernizations are never about just one team or one leader. Legacy
systems survive because they are important; processes tend to grow around
important systems, and organizations tend to grow around those processes.>>



<<Instead, ask yourself who needs to collaborate with whom for various
stages of the modernization project to work, and pick a structure that
makes this communication easy.>>


Breaking Changes

<<But, I want to start with the concept of air cover. Business writers
sometimes refer to “psychological safety,” which is another great way to
describe the same concept. To do effective work, people need to feel safe
and supported. >>

Being Seen

<<Being seen is not about matching an organization’s
theoretical ideals, it’s about what your peers will notice.>>

Building Trust Through Failure

<<Under Castelfranchi and Falcone’s model, maintaining trust doesn’t mean estab-
lishing a perfect record; it means continuing to rack up observations of
resilience. If a piece of technology is so reliable it has been completely
forgotten, it is not creating those regular observations. Through no fault
of the technology, the user’s trust in it will slowly deteriorate.
>>

<<It’s not the lack of failure that makes a system more
likely to fail, it’s the inattention in the maintenance schedule or the fail-
ure to test appropriately or other cut corners. Whether the assumption
that a too reliable system is in danger is sensible depends on what evi-
dence people are calling on to determine the odds of failure.>>


HOW TO FINISH

<<When I was working for the United Nations (UN), my boss at
the time would regularly start conversations with the words
“When the website is done . . .” to which I would respond, “The website
is never done.” I count among my accomplishments the fact that by
the time I left the UN, people had bought in to the agile, iterative pro-
cess that treats software as a living thing that needs to be constantly
maintained and improved. They stopped saying “When the website is
done . . .” Technology is never done, but modernization projects can be. >>

Post Mortem
<< Postmortems establish a record about what really happened and how
specific actions affected the outcome. They do not document failure; they
provide context. Postmortems on success should serve a similar purpose. >>

War Rooms

Working Groups vs Commmittees

<<Working groups relax hierarchy to allow people to solve problems
across organizational units, whereas committees both reflect and rein-
force those organizational boundaries and hierarchies. >>
<<Working groups are internally facing; the customers for a working
group are the members of the working group itself. People join working
groups to share their knowledge and experience with peers. >>
<<Whereas the working group is open to those who consider themselves operating in the same
space as the working group’s topic area, committees are selected by the
entity they will be advising and typically closed off to everyone else.
That external authority decides the committee’s scope and goals. The
committee reports up to that external authority and exists solely for its
benefit.>>

Success Is Not Obvious If Undefined
<<Don’t assume that success is obvious. Different
members of your team may have different and competing visions of what
better looks like.>>
<<All technology is
imperfect, so the goal of legacy modernization should not be restoring
mythical perfection but bringing the system to a state where it is pos-
sible to maintain modern best practices around security, stability, and
availability.>>


FUTURE-PROOFING

<<Future-proofing isn’t about preventing mistakes; it’s about knowing how
to maintain and evolve technology gradually.>>
<<Scaling challenges are the change in usage type: we have more traffic or a different
type of traffic from what we had before. >>
<<Usage changes do not have a constant pace and are, therefore, hard to predict.>>
<<Deteriorations, on the other hand, are inevitable. They represent a nat-
ural linear progression toward an unavoidable end state. >>

Time

Classic stuff

Unescapable Migrations
<< The secret to future-proofing is making migrations and rede-
signs normal routines that don’t require heavy lifting.>>
<<Instead, managing deteriorations comes down to these two practices:
● If you’re introducing something that will deteriorate, build it to
fail gracefully.
● Shorten the time between upgrades so that people have plenty of
practice doing them.
>>

Failing Gracefully

<< How close is the error to a user interface? If the error is something
potentially triggered by user input, failing gracefully means catching the
error and logging the event but ultimately directing the user to try again
with a useful message explaining the problem. >>
<<  Will the error block other independent processes? >>
<< Is the error in one step of a larger algorithm?  >>
<< Will the error corrupt data? >>


Less Time Between Upgrades, Not More
<<I know from experience that the more
often engineers have to do things, the better they get at doing them, and
the more likely they are to remember that they need to be done and plan
accordingly.>>

A Word of Caution About Automation

<<Automation is more problematic when it obscures or otherwise encour-
ages engineers to forget what the system is actually doing under the hood.
Once that knowledge is lost, nothing built on top of those automated activ-
ities will include fail-safes in case of automation failure. The automated
tasks become part of the platform, which is fine if the engineers in charge
of the platform are aware of them and take responsibility for them>>

Building Something Wrong the Correct Way


<<Disaster comes from trying to build complex systems right away and
neglecting the foundation with which all system behavior—planned
and unexpected—will be determined.
A good way to estimate how much complexity your system can
handle is to ask yourself: How large is the team for this? Each addi -
tional layer of complexity will require a monitoring strategy and ulti-
mately human beings to interpret what the monitors are telling them.>>
<<Lots of teams model their systems after
white papers from Google or Amazon when they do not have the team to
maintain a Google or an Amazon>>

Don’t Stop the Bus

<<I once had a senior executive tell me, “You’re right about the seri-
ousness of this security vulnerability, Marianne, but we can’t stop the
bus.” What he meant by this was that he didn’t want to devote resources
to fixing it because he was worried it would slow down new develop-
ment. He was right, but he was right only because the organization had
been ignoring the problem in question for two or three years. Had they
Future-Proofing 215
addressed it when it was discovered, they could have done so with min-
imum investment. Instead, the problem multiplied as engineers copied
the bad code into other systems and built more things on top of it. They
had a choice: slow down the bus or wait for the wheels to fall off the bus.>>

CONCLUSION

<<Part of the reason legacy modernizations fail so often is that human
beings are incentivized to mute or otherwise remove feedback loops
that establish accountability. >>
<<Engineering organizations that maintain a separation
between operations and development, for example, inevitably find that
their development teams design solutions so that when they go wrong,
they impact the operations team first and most severely. Meanwhile, their
operations team builds processes that throw barriers in front of develop-
ment, passing the negative consequences of that to those teams. These are
both examples of muted feedback loops.>>
<<One of the reasons the DevOps and SRE movements have had
such a beneficial effect on software development is that they seek to
re- establish accountability>>
<<Making software engineers responsible for the health of their infrastruc-
ture instead of a separate operations team unmutes the feedback loop.>>
<<A high-functioning organization cannot have all feedback loops open
all the time. It must decide which loops have the biggest impact on oper-
ational excellence.>>
<<Meetings, reports, and dialogues are the least efficient feedback loops.
Feedback loops are most effective when the operator feels the impact,
rather than just hearing about it. >>
<<Designing a modernization
effort is about iteration, and iteration is about feedback. Therefore, the
real challenge of legacy modernization is not the technical tasks, but
making sure the feedback loops are open in the critical places and com-
munication is orderly everywhere else.>>
<<As a general rule, the discretion to make decisions should be dele-
gated to the people who must implement those decisions. If you are not
contributing code or being woken up in the middle of the night to answer
a page, have the good sense to remember that no matter how important
your job is, you are not the implementor. You do not operate the system,
but you can find the operators and make sure they have the air cover they
need to be successful. Empower the operators.>>
<<Technology advances in cycles with old paradigms constantly being
dusted off to capture neglected segments of the market. Newer is not
necessarily better. Good technology isn’t about having the most modern,
most scalable, fastest, or most secure implementation; it’s about serving
the needs of the user.>>
<<To most software engineers, legacy systems may seem like torturous
dead-end work, but the reality is systems that are not used get turned off.
Working on legacy systems means working on some of the most critical
systems that exist—computers that govern millions of people’s lives in
enumerable ways. This is not the work of technical janitors, but battle-
field surgeons. It has been the greatest honor to serve among them.>>







