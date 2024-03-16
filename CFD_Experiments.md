# CFD Experiments: Exploring Aerodynamics with InsightCAE

After exploring various options, I discovered InsightCAE, an accessible open-source software powered by OpenFOAM, perfect for conducting preliminary experiments in a Virtual Wind Tunnel.

[InsightCAE GitHub Repository](https://github.com/hkroeger/insightcae)

## Windows Installation and Setup

You can find the Windows binary [here](http://downloads.silentdynamics.de/ubuntu/). This installer includes an image for the Ubuntu Linux VM required to run the OpenFOAM backend.

Before installation, ensure that the Linux SubSystem is functioning correctly. Any missing components could lead to installation issues. Verify that Python 3.6 is the first version listed in your environment variable PATH if you have multiple versions installed.

The key component you'll be working with is the 'workbench', where you can create and manage analyses.

## Optimization for Efficiency

To expedite experiments, I often adjust the following parameters:

- **lxsurf**: Set to 2 (or the default 4). While this creates coarse meshes, it suffices for basic experiments.
- **np**: Utilize all available CPU cores (e.g., 8 in my case), it does make the system lags.
- **v**: Default is 1 m/s; I set it to 50 m/s (roughly 180 km/h).

Though sacrificing some precision, this setup significantly reduces simulation time. Later, refine the mesh for more accurate results.

## Conducting Basic Experiments

Understanding complex designs like cars requires starting with simple experiments. Aerodynamic components like wings are particularly sensitive. A slight change in angle of attack can induce turbulence, affecting forces.

Components interact, offering potential advantages when combined. However, this requires careful optimization, as combining elements may not always yield superior results compared to individual optimization.

During simulations, monitor forces in the 'force' tab. Turbulences manifest as fluctuations in force, eventually stabilizing. Pausing the simulation ('Write + Stop') allows examination of turbulence effects on experimental components.

By refining these techniques and observations, deeper insights into aerodynamics can be gained.


### NACA Wings
As first step, I would suggest to check some NACA wings designs, then you go in your favorite CAD import the profile and extrude it. After, you can put some plates on the sides and see the effects of such elements, this is far from obvious, how such plates interacts with the wing.

### Diffuser
I created a small diffuser with basically a boxe with rounded fillets on the front, on which is put two small end plate one side to prevent the diffuser to be on the ground. The diffuser with a very simple line about a few degrees. It is very sensitive.
Then, you can create a spline with a smaller angle at the front, moving to the angle of the previous 'working' straight diffuser, but with a exit of the diffuser a bit more steep angle, of course you have to iterate to see how the flows goes.



# Tips

Sometimes the frontend crashes at the end of the process, you can still see a lot of things inside the VM.
First, you need to setup X11 in the VM, in order to be able to use ParaView (https://github.com/boucaron/randomstuff/blob/main/Tips/XServerWSL2.md)
Basically, you go in the VM and check what is the list file/directory modified
```bash
ls -ltr
```
Then you go in the directory and you can launch ParaView 
```bash
paraFoam
```
You must have it in your PATH for in /opt/insightcae/openfoam/OpenFOAM-v2112/bin/ (for instance)

Then inside ParaView, you select only the 'object' (to simplify).
Click on Accept
And you will see by default the pressure profile

For the postprocessing data, I do something like this:
```bash
user@DESKTOP:~/ir7a8QOE/postProcessing/forces/0$ head -5 force.dat 
# Force         
# CofR          : (0.00000000e+00 0.00000000e+00 0.00000000e+00)
#
# Time          	(total_x total_y total_z)	(pressure_x pressure_y pressure_z)	(viscous_x viscous_y viscous_z)
1               	(2.44967758e+02 1.43643379e+01 -7.85462943e+01)	(2.40824428e+02 1.43542494e+01 -7.87136763e+01)	(4.14333062e+00 1.00885312e-02 1.67381962e-01)
user@DESKTOP:~/ir7a8QOE/postProcessing/forces/0$ tail -5 force.dat 
996             	(1.69598242e+03 2.14530127e+01 -1.20015505e+03)	(1.64450063e+03 2.17805817e+01 -1.20847509e+03)	(5.14817939e+01 -3.27568950e-01 8.32003738e+00)
997             	(1.69573349e+03 1.97752124e+01 -1.20559961e+03)	(1.64428873e+03 2.01047213e+01 -1.21391597e+03)	(5.14447654e+01 -3.29508910e-01 8.31636126e+00)
998             	(1.69565379e+03 1.75971288e+01 -1.21495914e+03)	(1.64424491e+03 1.79292160e+01 -1.22327393e+03)	(5.14088820e+01 -3.32087179e-01 8.31478479e+00)
999             	(1.69509944e+03 1.52519969e+01 -1.22636925e+03)	(1.64372577e+03 1.55865072e+01 -1.23467735e+03)	(5.13736782e+01 -3.34510365e-01 8.30809700e+00)
1000            	(1.69415164e+03 1.32836955e+01 -1.23882678e+03)	(1.64280893e+03 1.36216493e+01 -1.24713012e+03)	(5.13427115e+01 -3.37953876e-01 8.30334096e+00)
```


Sometimes the frontend put an error message (kill something), because you use too much memory when using all the CPU cores you have.
Typically if you push too much, you will have an out of memory.
You can check this after in the VM by doing
```bash
dmesg
```
Typically, you will at the end something like out of memory.
When you run large experiment, put slightly less CPU cores if you do not have enough memory.
For instance I can run 8 cores with 32 GB of RAM in the VM, for the default settings.
If I increase by 2 order of magnitude the quality of the mesh (meaning quadrupling the size), I can only use safely 2 cores, and the simulation goes from a quick 20/30 minutes per experiment to nearly an afternoon.






