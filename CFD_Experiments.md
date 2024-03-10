# CFD Experiments: Exploring Aerodynamics with InsightCAE

After exploring various options, I discovered InsightCAE, an accessible open-source software powered by OpenFOAM, perfect for conducting preliminary experiments in a Virtual Wind Tunnel.

[InsightCAE GitHub Repository](https://github.com/hkroeger/insightcae)

## Windows Installation and Setup

You can find the Windows binary [here](http://downloads.silentdynamics.de/ubuntu/). This installer includes an image for the Ubuntu Linux VM required to run the OpenFOAM backend.

Before installation, ensure that the Linux SubSystem is functioning correctly. Any missing components could lead to installation issues. Verify that Python 3.6 is the first version listed in your environment variable PATH if you have multiple versions installed.

The key component you'll be working with is the 'workbench', where you can create and manage analyses.

## Optimization for Efficiency

To expedite experiments, I often adjust the following parameters:

- **lxsurf**: Set to 2 (default is 4). While this creates coarse meshes, it suffices for basic experiments.
- **np**: Utilize all available CPU cores (e.g., 8 in my case), it does make the system lags.
- **v**: Default is 1 m/s; I set it to 83.3 m/s (roughly 300 km/h).

Though sacrificing some precision, this setup significantly reduces simulation time. Later, refine the mesh for more accurate results.

## Conducting Basic Experiments

Understanding complex designs like cars requires starting with simple experiments. Aerodynamic components like wings are particularly sensitive. A slight change in angle of attack can induce turbulence, affecting forces.

Components interact, offering potential advantages when combined. However, this requires careful optimization, as combining elements may not always yield superior results compared to individual optimization.

During simulations, monitor forces in the 'force' tab. Turbulences manifest as fluctuations in force, eventually stabilizing. Pausing the simulation ('Write + Stop') allows examination of turbulence effects on experimental components.

By refining these techniques and observations, deeper insights into aerodynamics can be gained.


### NACA Wings
As first step, I would suggest to check some NACA wings designs, then you go in your favorite CAD import the profile and extrude it. After, you can put some plates on the sides and see the effects of such elements, this is far from obvious, how such plates interacts with the wing.

### Diffusor
I created a small diffuser with basically a cube, on which is put two small end plate to prevent the diffuser to be on the ground and create the diffuser with a very simple line about 3 to 5 degrees max. It is very sensitive.
Then, you can create a spline with a smaller angle, but with a exit of the diffuser a bit more steep, of course you have to iterate to see how the flows goes. 








