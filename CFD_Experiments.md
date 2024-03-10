** CFD Experiments

Finally I found a simple enough open-source software called InsightCAE using OpenFOAM as backend to conduct basic experiments with a Virtual Wind Tunnel.

Links: https://github.com/hkroeger/insightcae

# Windows Installation/Setup

The Windows binary is found here: http://downloads.silentdynamics.de/ubuntu/

For Windows it contains an installer with an image for the Ubuntu Linux VM used to run the backend with OpenFOAM.

First, check and be sure to make the Linux SubSystem working correctly before installing, if you are missing a few things it will cause an issue.
If you have multiple versions of Python installed, check that 3.6 version is the first one in your environment variable PATH.

The binary you are interested is called the 'workbench', you can create an analysis. 

# Speed 

To speed-up the experiments, I am modifying the following parameters most of the time:
- lxsurf: 2 (default value set to 4, it makes crude meshes but most of the time this is ok - in my case)
- np: 8 (I have a 8 cpu machine, so I use all of them and no lag on the system)
- v: 83.3 (default is set to 1, the unit is in m.s-1, for 83.3 it means around 300 km.h-1)

It may lacks precison, so after you need to refine further and the simulation takes way long time.
After you can first put back lxsurf to 4 as the default and refine further away.

# Small experiments for basic understanding

First I tried to create small experiments, it is quiet difficult to figure out what is going on a complex design such as car, without a prior knowledge, know-how of what is going on.

Wings or any other aerodynamics apparatus are quiet 'sensitive', an angle of attack about one more degree and you can see on the flow that it starts to create turbuleances, and you will see the effect on the forces.
Also, all objects arounds interacts to each other, it means you can gain an advantage by combining a diffusor and a wing together where each of them can improve more than each element, but as said before this is quiet sensitive, so you can may obtain a result that is less good than each element separated.

There is a force tab, when the simulation launches, let say this is a wing or diffuser I am testing, I am having a look to the force, if you have a lot of turbuleances, you will see the force going up and down, and after it will move to another 'plateau'. In general, I click on 'Write + Stop', to stop the simulation and see what is going on. In general, I can see such turluleances on the apparatus of the experiment.







