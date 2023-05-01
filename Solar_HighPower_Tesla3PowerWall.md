One of those interesting random walk on the 'net', trying to see what are the current updates on Solar Panels and associated tech

In Luxembourg, my house is having 380/400V Triphase electricity above 20KW

I am still thinking about setting up a combo including a 48V battery + hybrid Victron or equivalent on a phase to start. This should not really be a problem because I have only 3 really power angry resistive loads for the cooking and for the water heating. But it is not really nice from balancing point of view.

It seems there is an interesting hybrid inverter alternative for Triphase.
There are Triphase Fronius Symo Gen24 Plus hybrid inverters with Dual MPPTs.
Tt can works with a BYD High Voltage battery (400V), hopefully some talented guys managed to reverse engineer the protocol used with the BYD battery and use a Tesla Model 3 battery back instead. This is pretty cool stuff.

# Economics

- A commercial 48 V battery pack  will be about 8 to 12 K€ for about 10 to 12 kWh. ( 1 to 1.5 Wh per euro)
- A DIY 48V 16 Cells battery about 13 KWh will cost you about 3K€ with a descent BMS, fuse-box and all needed security (4.3 Wh per euro). 
- If you consider the Tesla Model 3 small capacity pack: for about 7K€ you will have about 50 kWh of capacity (7.8 Wh per euro)
- For a Tesla Model 3 75 kWh battery pack about 10 K€ (7.5 Wh per euro)


# Size matters
So for a 'large' installation (about 15 to 20KW of PV), it makes a ton of sense because the battery pack is by far the most expensive item in any solar installation.
But this is another kind of investment, you need to think first of the power you use.

The drawback is the cost of entry of this tech, there are no small 12 to 20 Kwh battery available to enable to use it on 4 to 8 KW of PV.
The minimum ticket for entry is either a Tesla Model 3 50 KWh pack or a Nissan Leaf one.
The target price of an equivalent 13 kWh battery should be around 1666 €, so let say nearly a 50 % reduction in price on a DIY made one.

But I think it is too big for a small or medium sized home, not sure the economics make sense for a heat-pump (depends on the house, climate...)
Still, I think it makes a lot of sense also for small/medium sized offices and small industrial companies.

# Technical Drawbacks

I do not think it is possible to attach more than one inverter to the Tesla battery pack. It would made sense to push and to get more load from the battery pack. You are limited about 10KW of power with existing line of Gen24 inverters. A 75 kWh Tesla Model 3 battery can push more than 400 A continuously so about 142 KW ! (assuming 355 V)
Clearly the inverter is the weakest link in the chain.


# Installation cost

- Let say about 5 KW PVs (2K€) + Victron 5KVA Hybrid Inverter (2.5K€) + DIY 13kWh Battery (3K€) will cost around 10 K€ (including all hardware for installion).
- Now a 12 KW PVs (4.8K€] + 10KVA Fronius Hybrid Inverter (3K€) + 50 kWh Tesla Battery Pack (7K€) will cost you around 20 K€ (including all hardware for installation). I think it is really interesting, but really the main limitating factor is the power of inverter that limits both the size of the PV array. If there was a 16 to 20 KVA version it will make more sense.

# Simulation 

Evaluation using https://re.jrc.ec.europa.eu/pvg_tools/en/ with Luxembourg using a non optimal slope of 20 deg and South-West orientation.
- 5 KW PV array, around 600 kWh from April to August included so a daily mean of 19.35 kWh daily (yearly 5000 kWh), a battery of 13 kWh is a bit undersized (of course depends on your load, it would cover nearly yearly my needs including aging of PV array, but this is not that simple ;)).
- 12 KW PV array, due to 10KVA limitation of the inverter a strong and steady 1250 kWh from April to September included (effect of oversizing the PV array, yearly above 11000 kWh), so a daily mean of 40 kWh, a battery of 50 kWh is better sized, it can cover few days of bad weather (depends on your load of course). If you are in Marbella (Spain) you just just need 10 KW of PV array to nearly fill the battery daily on the same period.
- A battery of 75 kWh will not make sense in this context due to the huge limitation of the 10 KVA inverter. You will need at least a 18 KW PV array and a 18 KVA inverter to be able to load the battery fully during a day (Lux latitude). If you are in Marbella (Spain) assuming a 17KW PV array/inverter but you will have a lot of power from nearly March to October (32 deg slope and -4 deg azimuth).

# Conclusion
I thought the 50 kWh battery was way too big for a small to a medium house, I am not sure sure about that anymore.
Let me explain, in a few years you will not be allowed to use fossil fuel to heat your house.
If you think about adding a heat-pump I think it is on the low side (depends on your location/your house/your load of course), with a big spoon even with good insulation renovation I think at least a 12/16 KW heat-pump will be needed. 
There are larger swings in temperature, even in end of April the temperature in Luxembourg can go down to 1°C during the night.

# Hack Links 

Videos:
	- https://www.youtube.com/watch?v=-s7lODLDOiQ
	- https://www.youtube.com/watch?v=NQGJymwPm0E

Battery protocol hack: 
	- https://gitlab.com/pelle8/gen24/-/blob/main/gen24_byd_registers.md
	- https://github.com/flodorn/TeslaBMSV2
