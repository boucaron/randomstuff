# Why should you learn *a bit* of C ?

Ok just a little set of quick notes, not a babble.

I have nothing against new languages, but I am annoyed by some of the dogmatic discussions around them.

**Joke of the Day:** *You cannot fully appreciate high-level abstractions until you understand the mechanisms they abstract away. That is why you should learn some C.*

## When was C built, and what was it built for?

This is really fundamental, because the C language evolved from successive attempts to build a systems programming language, basically to build operating systems and more specifically Unix (not only of course).

It is important to remember that C is *not the final answer*; it is one successful attempt among many.

It is also interesting to remember that this period produced many foundational technologies. People working on these problems were directly exposed to the constraints of hardware and operating systems. There was less abstraction between the problem and the machine, which often forced a deeper understanding of the fundamentals.

## C as a Minimal Abstraction Set

C was created at a time when resources were limited. It was a balance between expressivity and a minimal set of abstractions suitable for its goal: building an operating system.

*It was never designed as the perfect language, but I would say an honest answer at the given time.*

## Memory Management and Computer Architecture

I think a basic computer architecture reading while learning the C language is an enabler.

You need to understand what these are :

- the call stack: how function calls work, and how they are represented conceptually on a CPU
- the heap and the memory allocator.

Then, with that in mind, it will enable further understanding and you can move on pointers and all the stuff around.

I would say this is typically the foundation that is missing in many C language courses. You should do both in parallel, it enables understanding in both ways.

## Being Exposed to Memory Problems

C does not provide arrays with the same kind of bounds checking that I experienced with Pascal.

Something else more important, more from a philosophy point of view, if you have never been exposed to the underlying problem, it is much harder to understand what a garbage collector is solving, or what a borrow checker is trying to guarantee. This does not mean you have to master all of it, but you need to have enough understanding to grasp the thing.

There are various kinds of memory problems, I will not really enumerate. But same story, you can easily understand the issue on small C programs.

# Control

With a garbage collector, the programmer usually does not decide the exact moment when memory reclamation happens. The runtime system manages that decision. You may give it a hint when to do the stuff, but ultimately the runtime decides. In C, the programmer explicitly calls the allocation and release operations (although the exact behavior depends on the allocation strategy being used).

A funny thing is that you can replace the traditional `malloc/realloc/free` allocator with a garbage collector behind a wrapper API. But at that point, you are mostly changing the memory management strategy, not the language itself.

In C, lifetime decisions are explicit in the code. You decide where allocation happens and where release happens. Other languages may provide safer mechanisms or automate these decisions, but they move the control point somewhere else.

## Static Allocation & Predictable Systems

I think Static Allocation is really an interesting case, and widely used in embedded systems, we don't want to repeatedly free and reallocate memory blocks that will be needed again shortly after, so the memory is allocated during initialization and kept for the lifetime of the program.

Simple, effective, and it offers determinism and nice invariants easy to reason about and to check it, either statically or during execution.

This is something not really explained in detail when performing a classic C course, but it is really important and useful, because it gives you another way to think about the way to build your program: instead of asking "when should I free this?", you sometimes design the program so that the question disappears.

## Boring Language

Boring is a nice property, it means it is stable, and it will not change too quickly, in infrastructure software boring is often a feature: it means the software has survived contact with reality.

If you want something that can run for decades with minimal maintenance, stability becomes a valuable property. My personal rule of thumb is that a language only starts to stabilize after at least a decade... I would say also this rule of thumb applies to most software too.

It means mostly no forced modernism: 'oh the feature banana is cool in the new language X, quick quick, let's integrate it because people will move to the new language ...'

Sometimes language evolution is driven not only by technical necessity but also by fashion, enthusiasm, or local optimization for specific use cases.

Learning C is not about rejecting newer languages. Quite the opposite: understanding what C exposes makes it easier to understand what newer languages are trying to improve.

The goal is not nostalgia; the goal is having a better mental model.

**Final joke of the day:** *I will continue to use C, because I like boring software.*
