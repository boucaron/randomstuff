One of those interesting random walk on the 'net', trying to see what are the current updates on Solar Panels and associated tech

My house in Luxembourg has 380/400V Triphase electricity above 20KW. I am considering setting up a 48V battery + hybrid Victron or a similar device on one phase to help with balancing, even though I only have three power-hungry resistive loads for cooking and water heating. However, I have found an interesting alternative in the form of Triphase Fronius Symo Gen24 Plus hybrid inverters with Dual MPPTs. These inverters can work with a BYD High Voltage battery (400V), and some people have even managed to use a Tesla Model 3 battery pack instead by reverse engineering the protocol.

# Economics

- A commercial 48V battery pack with 10-12 kWh of energy will cost around 8-12 K€ (1-1.5 Wh per euro).
- A DIY 48V battery with 16 cells and 13 kWh of energy, including a BMS and safety features, will cost about 3K€ (4.3 Wh per euro).
- The Tesla Model 3 small capacity battery pack, costing approximately 7K€, has a capacity of about 50 kWh (7.8 Wh per euro).
- The cost of a Tesla Model 3 75 kWh battery pack is around 10 K€ (7.5 Wh per euro).


# Size matters
For a solar installation with a capacity of around 15 to 20KW, it makes sense to invest in a large battery pack because it is typically the most expensive component. However, it is important to consider your power usage needs before making this investment.

The downside is that this technology has a high cost of entry, with no small batteries (12 to 20 KWh) available for use with 4 to 8 KW of PV. The minimum entry point is either a Tesla Model 3 50 KWh pack or a Nissan Leaf one. The ideal target price for an equivalent 13 kWh battery would be around 1666 €, which represents almost a 50% reduction in price compared to a DIY battery.

However, for small or medium-sized homes, the battery pack may be too large and may not make economic sense for a heat pump (depending on the house and climate). Nevertheless, it could be a smart investment for small/medium-sized offices and small industrial companies.


# Technical Drawbacks

It's not possible to connect multiple inverters to the Tesla battery pack, which limits the amount of power that can be drawn from it. While a 75 kWh Tesla Model 3 battery can continuously output more than 400 A, providing up to 142 KW of power (assuming 355 V), the existing line of Gen24 inverters can only handle up to 10KW of power. Therefore, the inverter is the weakest point in the system.

# Installation cost

A solar installation consisting of 5 KW PVs (2K€), a Victron 5KVA Hybrid Inverter (2.5K€), and a DIY 13kWh Battery (3K€) will cost around 10 K€ including all necessary hardware for installation.

However, a larger 12 KW PV system (4.8K€), a 10KVA Fronius Hybrid Inverter (3K€), and a 50 kWh Tesla Battery Pack (7K€) will cost around 20 K€, including all hardware for installation. While this option is interesting, the main limiting factor is the power of the inverter, which restricts both the size of the PV array and the battery pack. If a 16 to 20 KVA version were available, it would make more sense.

# Simulation 

The evaluation was conducted using https://re.jrc.ec.europa.eu/pvg_tools/en/ for Luxembourg with a non-optimal slope of 20 degrees and South-West orientation. A 5 KW PV array would generate around 600 kWh from April to August, with a daily average of 19.35 kWh (yearly 5000 kWh). A 13 kWh battery would be undersized, depending on your load. 

A 12 KW PV array, due to the 10KVA inverter limitation, would generate a strong and steady 1250 kWh from April to September, with a daily average of 40 kWh (yearly above 11000 kWh). A 50 kWh battery would be better sized and can cover a few days of bad weather, depending on your load.

However, a 75 kWh battery would not make sense due to the inverter's huge limitation. You would need at least an 18 KW PV array and an 18 KVA inverter to fully load the battery during a day (Lux latitude). If you are in Marbella (Spain), a 17 KW PV array/inverter would suffice, but you will have a lot of power from nearly March to October (32 deg slope and -4 deg azimuth).


# Conclusion
Initially, I believed that a 50 kWh battery would be too large for a small or medium-sized house. However, I am reconsidering this viewpoint due to the future ban on fossil fuel usage for heating homes. In this scenario, a heat-pump may be necessary and a 50 kWh battery could be appropriate depending on location, house size, and energy needs. Larger heat-pumps may also be required due to temperature fluctuations, with temperatures in Luxembourg potentially dropping to 1°C even in late April.

# Hack Links 

Videos:
	- https://www.youtube.com/watch?v=-s7lODLDOiQ
	- https://www.youtube.com/watch?v=NQGJymwPm0E

Battery protocol hack: 
	- https://gitlab.com/pelle8/gen24/-/blob/main/gen24_byd_registers.md
	- https://github.com/flodorn/TeslaBMSV2
