I am used to MinGW to have most of my 'unix' tools inside Windows.
It has few drawbacks because you have a kind of intermediate layer.
Several programs are having a really native Windows version and a variant for Linux and other Unix flavors.
Sometimes you may have to use the Native or the MinGW 'flavor' of the same program. It is always the same story, go the website, find out the version, download it, click click and so on...


So I discovered recently another way with Scoop https://scoop.sh/

It is kind of pretty neat.
Easy to install and well integrated inside 'Powershell'
The 'Powershell' is not my cup of tea, but it is an improvement with respect to the classic Cmd.
I like the way the packaging mechanism is implemented.
For 'common' usage it is very similar to 'pacman/apt/dnf':
- scoop search whatever
- scoop install ...
- scoop uninstall ..

The number of apps and the maturity seems descent, so I started to add dependencies from it when creating some stuff in Python.

For me:
- git
- 7zip
- emacs
- sts (Spring Tools for Eclipse)

For anything related to my C/C++ development, it not up to date for me: I don't use it for that.







