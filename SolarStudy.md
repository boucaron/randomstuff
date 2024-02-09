Few notes about Solar and Its Evaluation

When I was a kid, my grandparents had an off-grid farm in the South East of France.
During the mid 80's they setup a PV array with several large lead baterries for lighting purpose, they used to have a gaz lighting before.
The fridge was using a gaz bottle, if you can call that a fridge from a cold point of view, the performance was really bad.
Since then, the technology has slightly improved and it is becoming main stream.

# Evaluating Electrical needs

First I had a look to my yearly electrical bills.
We consumme around 4500 kWh yearly.
Electricity is not used for heating or cooling the house.
We use electricity to heat water for shower/bath and for cooking.

# Understanding your habits

We have smart meters installed, we can see 15 to 15 minutes the power usage we are having, this is really handy to understand.
Daily usage is about 12 to 18 kWh without really specific patterns from a season to another one. 
We have really high peak power usage about 12 to 18 KW for the direct heaters used for the shower/bath.
There is a minor seasonality aspect about that for winter, because the water is a few degrees lower.
Cooking in the morning, during the lunch and the evening.
Night load is really steady all over the year from let say midnight to 6 in the morning.
So nothing really special here.
The load of the washing machine or the dish washer are kind of intermittent. We do not really have a habit around that, so it is not really easy to spot on the power graph or the data.
An interesting part is when we are in vacation which is providing a pretty good evaluation of what are the loads of your fridge and other equipment that have to run all the time, in my case it is about 105W.

- Yearly power usage: 4500 kWh.
- Daily mean power usage = 12.32 kWh
- Daily Night power usage: 0.105 * 8 = 0.840 kWh
- Daily Evaluated "Regular" Usage from 8h to 24h: 0.4kW * 16 = 6.4 kWh
- Daily Vacation power usage: 0.105 * 24 = 2.520 kWh 
- Yearly 24 continuous power usage: 2.52 * 365 = 919.8 kWh, around 20% of the total usage.
- Yearly "Regular" Usage from 8h to 24h: 2336 kWh, around 51% of the total usage.
- Yearly "Remaining" Usage (including peak High power): 1244 kWh

- Most of the power peaks are:
  - Shower time 8 to 18 KW
  - Breakfast, Lunch, Dinner
  - Washing Machine and Dish Washer (2 to 4 KW when heating)


# Understanding the loads 

In my case, I consider about 105W for 24 continuous loads (Internet Box, Router ...)
The direct water heater are really power hungry beast toping about 12 to 18 KW.
The cooking is about 2 to 5 KW, it depends on how many things you turn on.
The washing machine and the dish washer about 2 to 4 KW.
PCs/Laptops are about 40 to 400 W.
TV/Large screen about 100W to 200W.



# Tech Overview

## Solar Panel

A Solar Panel (also called PV) is in general a large piece of silicon + glass generating DC electricity from the sun. 
Given an area, the PV generates an amount of electricity (in watt).
Technically speaking most of them are equals and more like a commodity, there is not any revolutionary technology from a manufacturer to another one.
Chinese manufacturers are leading the market.
You need to take in account the size, the power to surface/area ratio.
Bi-facial can be interesting if you are outdoor, bi-facial means there is a front and a back face, the back face is covered with a transparent glass. It can produce additional electricity, for instance the light reflect on the  grass in a garden which is captured by the back face. However, I think the real production advantage may be around 5 to 10%, which is not really interesting from a price point of view.
You can also have partially transparent PV that can be useful for agriculture or pergola.
The bang for the buck for today PV around 400 to 500W (1700 mm to 2300 mm length, 770 mm large and 35 mm height) costing about 150 to 250 Euros (including VAT).
Shadows can be a challenge, there are some difference with Half Cells and Shingle, I would say Half Cells are more consistent from a production point of view: in the case of Shingle when it reach 20 to 30% shadows, it does not produce anything (depends on the shadow configuration), while this is not the case for the Half Cells. Market Leaders are Chinese manufacturers, so far I do not know anything better from a price/performance point of view.



## Inverters
There are various inverters, micro-inverted, string-inverters, hybrid-inverters, offgrid-inverters and so on.

An inverter is a device transforming PV DC fluctuating voltage/current to either:
- DC to provide electricity to a battery
- AC to provide electricity to various loads and the grid.

### Micro inverters
Micro-inverters are small inverters that are attached to either one, two, four and up to six pannels. The main argument is that each micro-inverter is having one or more MPP trackers.
If there is a bit of shade on one panel, only the production of the pnale is affected because it has its own MPP tracker. You can one, two or four panels attached to a MPP tracker. They can range from 200W for single panel version to 2500W for six panel versions. Nearly all existing micro-inverters are grid connected, if the grid fails the production stops to avoid killing staff working on the grid. 
Price range from 130 € for single PV unit to 450 € for triple MPP with 6 PVs.
There is a price advantage to have at least two or more PVs attached to the micro-inverter, also regarding shading there is not too much advantage to have only one PV.


### String inverters
String-inverters  inverters having one, two or more MPP trackers where you attach a 'string' of PV panels connected together in serie. Most of the time they range from 1 KW to 30 KW.
Regarding pricing, it is not so obvious for some brands it is cheaper to put 2 times 5 KW inverter than to buy a single 10 KW.

### Hybrid inverters
Hybrid-inverter means this is an inverter coupled to a battery. The PV array can charge the battery and/or provide power to the load through the inverter. It is a versatile device, it can be connected to the grid, a generator ...etc... There are hybrid inverters for 12/24 and mostly 48V batteries (Victron for instance), there are some inverters for high voltage batteries (Fronius/Huawei for instance)

An off-grid inverter is a hybrid inverter that operates independently without being connected to the grid. Hybrid inverters offer different modes to meet various needs. However, for off-grid setups, it's crucial to understand the load requirements and the inverter's efficiency. The cost of the off-grid system depends on the battery size. Opting for a cheaper, less efficient inverter might lead to higher expenses on batteries and additional panels. On the other hand, investing in a reputable brand-name inverter (though more expensive upfront) can lead to overall cost savings by requiring fewer PVs and batteries. Finding the right balance is essential, and it's vital to consider future needs or expansions as well. You may want to do zero injection in the future but your inverter cannot do it and you may need to change your inverter.

### Metrics
Each inverter is associated with various metrics, and for an effective off-grid setup, it's essential to consider these factors. Having a smaller but more efficient inverter can be advantageous, especially if the majority of your loads are small.

The key metrics to consider are:

Max Load/Peak Power: This metric is crucial for off-grid systems because certain electric devices require higher current/power during startup. For example, the Victron Multiplus II 48/5000 has a max load of 10kVA, while its nominal power is around 5kVA. Similarly, the WKS Evo Circle 5.6 kVA peaks at 11kVA, and the Studer Xtender 3.5 kVA reaches 9kVA during peak. Cheaper inverters may handle only the nominal kVA, so it's important to choose wisely.

Efficiency: Inverters usually provide a max efficiency rating, but this is not very informative for off-grid setups where efficiency at various loads matters. Some inverters excel at small and medium loads but may have lower efficiency at high loads, making them suitable for off-grid installations. Conversely, some inverters are efficient only at middle to high loads, which could be beneficial for industrial loads like welding or running machines.

Zero Load Power: This metric is often overlooked but crucial for off-grid setups. It measures how much power the inverter consumes without any load. Lower zero load power is desirable as it reduces unnecessary energy consumption when the inverter is idle.

Here are examples of zero load power usage for some inverters:

(Data measured from https://www.youtube.com/watch?v=rnFXSEsfoaI)
- WKS Evo Circle 5.6 kVA 48V: Not provided (measured around 71W), 1.704 kWh daily, 622.386 kWh yearly.
- Victron Multiplus II 48/5000: 18W zero load (measured around 25W), 600 Wh daily, 219.150 kWh yearly.
- Xtender Studer XTM 3500-24: 12W zero load (measured around 16W), 384 Wh daily, 140.256 kWh yearly.
- Victron Multiplus II 12/3000 and 24/3000: 13W zero load (estimated around 18W), 432 Wh daily, 157.788 kWh yearly.
- Victron Multiplus II 48/3000: 11W zero load (estimated around 15W), 360 Wh daily, 131.490 kWh yearly.


## Batteries

Batteries are having various voltage and chemistry.
They are either build as low voltage from 12, 24 to 48V, or from high voltage about 400V and higher.
You can either buy commercial batteries with integrated BMS and/or integrated inverter, you can also build one yourself from cells, separate BMS, separate inverter.
A Tesla powerwall costs about 14 K€ for 13.5 kWh with a 5KW inverter.
A DIY battery about 13 kWh with a 150 A BMS costs about 2.5 to 3 K€, if you put a top-tiers hybrid inverter of 5KW (Victron Multiplus) 2K€, so about 5.5 K€ max.

## Battery Management System (BMS)

BMS is used to charge/discharge a battery and have various protection according to the kind of battery (under-voltage, over-voltage, current protection, temperature protection, cell-balancing ...etc...)

## Exploring Tools for PV Analysis

Various tools are available for analyzing photovoltaic (PV) systems. Among them, the most comprehensive and useful one I've found is the free tool offered by the European Commission: [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/). PVGIS allows you to input location data, system orientation (slope and azimuth), and array size, providing estimations of monthly and yearly production. While it's convenient to gauge production sensitivity in relation to the slope, surprisingly, this aspect is not as critical as one might assume.

The 'Daily Data' feature in PVGIS is particularly intriguing. It allows you to delve deep into the timing and duration of your production over the entire year, including hourly irradiance values. However, it's important to remember that PVGIS estimates are based on assumptions and cannot account for factors like shadows caused by trees, buildings, mountains, and more.

## Emphasizing the Importance of Details

Personally, I invested time in observing the sun's path throughout the year in the locations where I plan to install my PV panels. For example, I discovered that placing PV panels next to a wall (with an Azimuth of -30 degrees and a Slope of 90 degrees) would yield production from 7/8 AM to 2/3 PM between April and September. However, during this period, the irradiance remains relatively low, ranging from 200 to 600 W/m². Knowing this detail is crucial, as a 425W panel under 1000 W/m² irradiance generates only around 75W at 200 W/m² and up to 240W at 600 W/m². This awareness is key to accurately estimating actual production in your specific location.

Additionally, these insights can guide decisions about panel quantity for your inverter. While inverters are costly components, understanding that they can produce more power earlier in the day and manage excess production through "clipping" helps determine optimal panel-inverter ratios, considering inherent limitations.



## The Complexity of Dimensioning

Sizing solar systems involves intricate considerations. Components like solar panels, inverters, batteries, and BMS (Battery Management Systems) come in different 'sizes,' although these sizes are often discrete. For instance, you might require a 20 kWh battery, but constructing such a battery might be impractical. Instead, you might opt for two 13 kWh batteries, effectively coupled together. Similarly, when it comes to inverters, your need for an 8KW inverter might translate to using a 10 KW inverter, or perhaps two 5 KW inverters, or even three 3 KW inverters.

## The Imperative of Energy Storage

But why is energy storage so crucial?

The timing of energy production and consumption varies significantly. Solar production doesn't align perfectly with usage patterns. Electric companies don't typically offer compelling buyback rates, and selling surplus energy at a low price during the day while needing it at night doesn't make economic sense.


## The Core Concept

Let's break down the fundamental concept:

- A 5 KW PV Array combined with a 5 KW Inverter: Yields approximately 5100 kWh under the specific orientation and conditions of my location.
- Adopting a cautious approach, by excluding November, December, January, and February, we reduce the estimated output by around 641 kWh, resulting in 4459 kWh. Remarkably, this aligns quite closely with my annual power consumption.
- Factoring in the natural aging of the PV array over 25 years, at a rate of -15%, we arrive at a more conservative estimate of 3790 kWh.

However, challenges arise due to occasional high peaks exceeding 8 KW, mainly from direct shower heaters. Managing this load surpasses the capacity of a single 5KW inverter. Additionally, my three-phase setup necessitates an appropriate solution.

Broadly speaking, the investment could range from 8 to 10 K€, encompassing a 13.5 kWh DIY battery. During the summer period, the PV array is projected to generate approximately 18 to 22 kWh per day. This surplus power prompts swift battery charging. Adjusting daily habits to make optimal use of this abundant energy (from April to August) becomes essential, particularly for appliances like the washing machine and dishwasher.



## Expanding Battery Capacity

Considering battery capacity expansion:

On an average day, power consumption reaches about 12 kWh. However, the typical charging and discharging pattern of LiPo batteries – from full to empty – significantly impacts their lifespan. To mitigate this, an extra battery is recommended. By distributing the current between the batteries during charging and discharging, heat generation is reduced. This results in less strain on each battery, potentially extending their lives. Assuming each battery will never be discharged below 20%, this approach ensures that even after daily usage, both batteries will maintain over 50% of their capacity. 

Although this entails a 3 K€ additional expense, raising the overall system cost from 11 to 13 K€, the trade-off is a substantial improvement in battery longevity, a critical aspect. Furthermore, the reduction in heat and stress on the battery currents not only extends lifespan but also minimizes capacity aging.

As referenced from [Battery University](https://batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries):

- Discharging to 80% Depth of Discharge (DoD) results in around 900 cycles.
- Discharging to 40% DoD allows for approximately 3000 cycles.

## Setting for Battery Settings

- Absorption Voltage: 55.2 V, 3.45V/cell
- Absorption Time: 1h
- Float Voltage: 53.6 V, 3.35V/cell


PV Array evaluation for Various MPPT Controllers @ 55.2 V:
- 60 A -> 3.3 KW (8 @ 415W, 9 @ 385W)
- 70 A -> 3.86 KW (10 @ 415W, 10 @ 385W)
- 85 A -> 4.69 KW (12 @ 415W, 13 @ 385W)
- 100 A -> 5.52 KW (14 @ 415W, 15 @ 385W)


# Enhancing Energy-Saving Habits

## Efficient Shower Practices
Showers utilize a substantial amount of power, ranging from 8 to 18 kW, depending on the water heater's capacity. The duration of your shower significantly impacts your energy consumption:

- A 15-minute shower can consume around 2 to 4.5 kWh.
- A 10-minute shower uses roughly 1.33 to 3 kWh.
- A 5-minute shower requires about 0.66 to 1.5 kWh.

Notably, the speed at which you shower plays a pivotal role in energy efficiency. To put it into perspective, let's consider a scenario where you take two showers a day over the course of a year:

- Showers lasting 15 minutes each: Estimated annual energy consumption of 2409 kWh.
- Showers lasting 10 minutes each: Estimated annual energy consumption of 1606 kWh.
- Showers lasting 5 minutes each: Estimated annual energy consumption of 803 kWh.

By saving as little as 5 minutes per shower, you could potentially reduce your yearly energy usage by approximately 803 kWh.

## Optimizing Washing Machine and Dishwasher Usage

When your PV array is adequately sized, it's likely that you'll experience excess energy production during the sunniest summer months. To harness this surplus energy effectively, consider running your washing machine or dishwasher during mid-morning or immediately after lunch. Opting for shorter cycles during these peak sunlight periods allows you to maximize the benefits of ample sunlight. This strategy ensures that your battery is adequately charged to meet your energy needs throughout the evening and nighttime.



# Study Case

The main objective is to minimize electricity sent back to the grid in order to avoid overproduction and overinvestment. It is pointless to receive minimal compensation for the electricity we produce, which is then distributed to our neighbors by the electricity operator, who doesn't make any significant investment but benefits greatly from this arrangement.

I refer to the power consumption when no appliances are running during the night or when the house is unoccupied as the "ghost load." In my case, this load amounts to approximately 0.1 to 0.15 kW. The "steady daily load" refers to the power consumption throughout the day, from waking until nighttime, excluding power peaks. In my case, this load averages around 0.4 to 0.5 kW.

## No Battery Case

I believe that microinverters are the most cost-effective solution for addressing the "ghost load" and/or the "steady daily load." This means purchasing a few solar panels and one or a few microinverters to meet this demand. Microinverters now come with multiple options and are much cheaper than before.


### Ghost Load

To partially address the "ghost load" during April to September in my region, utilizing one or two 400W panels with a double microinverter proves sufficient. The estimated cost for this setup ranges from 700 to 900 €. Although this configuration might appear oversized for the ghost load, it effectively covers a substantial portion of the steady daily load.

**Return on Investment (ROI) Scenarios:**

| Electricity Cost (€/kWh) | Annual Savings (€) | Break-Even Point (Years) |
|--------------------------|--------------------|--------------------------|
| 0.25                     | 150 - 200          | 6 (under pessimistic assumptions) |
| 0.4                      | 240 - 320          | 4                        |
| 0.5                      | 300 - 400          | 3                        |

### Steady Daily Load

For meeting the "steady daily load" of around 0.4 to 0.5 kW (including the ghost load), approximately three to four 400W panels paired with a 4-way microinverter would be essential. The projected cost for this setup is about 1000 to 1200 €. Notably, the return on investment is more favorable in this case. The cost of a 4-way microinverter is lower, and factoring in packaging and shipping, having 4 panels becomes more cost-effective than opting for 2.

Moreover, despite its slight oversizing for the steady load, this configuration effectively mitigates peak usage during lunchtime when high-power appliances like cooking equipment, washing machines, and dishwashers are in operation. This leads to a peak power production of about 1.1 to 1.3 kW.

**Return on Investment (ROI) Scenarios:**

| Electricity Cost (€/kWh) | Annual Savings (€) | Break-Even Point (Years) |
|--------------------------|--------------------|--------------------------|
| 0.25                     | 300 - 400          | 4                        |
| 0.4                      | 480 - 640          | < 3                      |
| 0.5                      | 600 - 800          | 2                        |

Considering my specific context, the investment in additional panels and a larger 4-way microinverter appears to be worthwhile.

## Battery Case

The most cost-effective battery setup is a DIY 16S (48V) lithium iron phosphate (LiFePo4) battery using 3.2V cells with a capacity of 280 to 300A, along with a 100 to 200A/BMS (Battery Management System). Building this battery will cost less than 3000 € (at the time of writing). Using smaller cells is not recommended considering the balance between capacity and price.



## Battery Case

The most economically viable battery setup involves creating a DIY 16S (48V) lithium iron phosphate (LiFePO4) battery using 3.2V cells with a capacity of 280 to 300Ah, along with a 100 to 200A BMS (Battery Management System). The cost to construct this battery is estimated to be less than 3000 € (at the time of writing).



### Factors Affecting Battery Aging
Battery aging occurs due to several factors, including temperature resulting from loads and the environment, the number of charging cycles, and the extent of capacity utilized between charges. To prolong battery life, it is advisable to store them in a room with a consistent temperature throughout the year, such as a basement. Additionally, using larger battery capacities makes sense if you aim to extend their lifespan. For instance, a battery discharged to more than 50% capacity will endure 2 to 3 times more charging cycles compared to a battery discharged to 80% capacity. Certainly, the cost of the battery remains the most significant deciding factor in any off-grid or hybrid installation. However, in the long run, it proves to be a sensible investment.

### Offgrid case

Weather conditions pose a challenge, as extended periods without sunlight are possible in certain locations. It's crucial to address this scenario to prevent the occurrence of a blackout.


## Orientation/Placement

I dedicated a significant amount of time, spanning almost a full year, to meticulously analyze various shadow patterns. This investigation encompassed shadows caused by the surrounding hill, trees, and nearby buildings in close proximity to my location. While this might seem meticulous, I believe in thoroughly exploring all potential panel placement sites and comprehending the associated advantages and drawbacks.

Merely installing panels on the roof of my house doesn't align with my considerations encompassing cost-effectiveness, maintenance concerns, and risk assessment. Even panels from renowned brands can develop issues like short-circuits due to aging, leading to sparks and potential roof damage.

One critical aspect is that placing panels on the roof offers only a single orientation possibility. On the other hand, situating panels in the garden allows for multiple orientations. This flexibility facilitates commencing production earlier by orienting a panel array more towards the East, or extending production later by introducing an additional panel array oriented towards the West. This strategic distribution of production assists in fulfilling a substantial portion of daily electricity needs when relying on a limited battery capacity or no battery at all.

For instance, during summer, I've observed that the sun reaches my terrace in the morning, and shadows cast by a nearby building appear around 2pm to 3pm. Similarly, sunlight begins to reach the back of the garden around 10 am due to trees, while shadows emerge between 7pm and 8pm. Armed with this knowledge, I can strategically install a panel array on the terrace facing East with a steep slope and another at the back of the garden facing South-West. This setup empowers me to generate power from 8 am to 8 pm during summer, with a notable peak between 10 am and 2 pm.

## PV Arrays Study

This study explores various possibilities for PV arrays in different locations on the property.
xOn my latitude the optimal slope is about 35 to 36 degrees and the optimal azimuth about 0 to -1 degree.
This part I go in the details of the evaluation.


### Panels Configurations

Let's explore various panel configurations, with all prices inclusive of VAT.

| Panel W | Number | Unit Cost (€) | Link | Total Cost (€) | Total W |
|---------|--------|---------------|------|----------------|---------|
| 415W    | 8      | 119           | [Link](https://www.chocdiscount.com/panneaux-solaires/19175-panneau-solaire-ja-solar-415w-jam54s30-415mr-monocristallin-black-frame.html) | 952  | 3320   |
| 415W    | 10     | 119           | [Link](https://www.chocdiscount.com/panneaux-solaires/19175-panneau-solaire-ja-solar-415w-jam54s30-415mr-monocristallin-black-frame.html) | 1190 | 4150   |
| 545W    | 8      | 143.99        | [Link](https://autosolar.es/panel-solar-24-voltios/panel-solar-545w-ja-solar-mono-perc) | 1151.92 | 4360 |
| 385W    | 10     | 99.0          | [Link](https://www.chocdiscount.com/panneaux-solaires/25763-panneau-solaire-amerisolar-385w-as-6m120-hc-demi-cellules-black.html) | 990 | 3850   |
| 385W    | 12     | 99.0          | [Link](https://www.chocdiscount.com/panneaux-solaires/25763-panneau-solaire-amerisolar-385w-as-6m120-hc-demi-cellules-black.html) | 1188 | 4620   |
| 505W    | 8      | 136.34        | [Link](https://autosolar.es/panel-solar-24-voltios/panel-solar-longi-lr5-66hph-himo5-505w) | 1090 | 4040 | 





### Inverter Configuration

For a single 4KW to 5KW per phase setup, the [Victron Multiplus II/48/5000](https://www.victronenergy.com/inverters/48v-5000va) inverter is selected due to its versatility and reasonable standby power usage, making it a cost-effective choice. The cost of this inverter is approximately 1500 to 1900 € (including VAT).

For smaller loads ranging from 200 to 2 KW, there are microinverters available in various configurations, such as one, two, four, and even six ways. While these options are relatively new and their reliability might be a concern, they offer flexibility for specific applications. There are also compact inverters available with power outputs from 800 to 2.5 KW, although their prices tend to be higher. One particular 2KW inverter option stands out and it is detailed after.

### PV MPPT Controller Configurations

| Option | Controller Model | Capacity | Cost (€) | Notes |
|--------|------------------|----------|----------|-------|
| 1      | [SNRE 250V/70A](https://www.srnesolar.com/product/%E2%80%8Bmppt-solar-regulator-solar-charge-controller-mc48v60-70a) [NEW MODEL](https://fr.aliexpress.com/item/1005004674334241.html?spm=a2g0o.store_pc_groupList.8148356.6.2ea8c85balNkhS&pdp_npi=3%40dis%21EUR%21%E2%82%AC%20384%2C34%21%E2%82%AC%20295%2C94%21%21%21%21%21%40210318d116935871915486338e8d0a%2112000030061281026%21sh%21FR%21839344662)| 4S/2P and/or 5S/2P, 550W peak | around 350 | Cost-effective option |
| 1      | [SNRE 250/85A](https://www.srnesolar.com/product/%e2%80%8bmppt-solar-charge-controller-mc48v85-100a) [NEW_MODEL](https://fr.aliexpress.com/item/1005005369131585.html?spm=a2g0o.store_pc_groupList.8148356.15.2ea8c85bjfttRf&pdp_npi=3%40dis%21EUR%21%E2%82%AC%20559%2C04%21%E2%82%AC%20402%2C51%21%21%21%21%21%40210318d116935871915486338e8d0a%2112000032769315432%21sh%21FR%21839344662)| 4S/2P and/or 5S/2P, 550W peak | around 425 and 485 | More capacity, slightly more expensive |
| 1      | [SNRE 250/100A](https://fr.aliexpress.com/item/1005005369131585.html?spm=a2g0o.store_pc_groupList.8148356.15.2ea8c85bjfttRf&pdp_npi=3%40dis%21EUR%21%E2%82%AC%20559%2C04%21%E2%82%AC%20402%2C51%21%21%21%21%21%40210318d116935871915486338e8d0a%2112000032769315432%21sh%21FR%21839344662)| 4S/4P and/or 5S/3P, 550W peak | around 475 | More capacity, slightly more expensive not really appropriate |
| 2      | [Victron 250V/70A](https://www.victronenergy.com/solar-charge-controllers/smartsolar-mppt-ve.can?_ga=2.250982854.1958924882.1691273838-1387248659.1691273838) | - | - | Higher-end option |
| 2      | [Victron 250/85A](https://www.victronenergy.com/solar-charge-controllers/smartsolar-mppt-ve.can?_ga=2.250982854.1958924882.1691273838-1387248659.1691273838) | - | - | More capacity, higher-end option |
| 3      | [SNRE 150V/60A](https://www.ase-energy.com/1409-regulateur-de-charge-solaire-60a-mppt-12-24-48v-srne.html) | 2S/4P or 3S/3P | around 265 | Low Cost effective option | 

The dimensioning calculations for both options are based on battery voltage and used for computation. Given the price difference, choosing the SNRE 70A model to match the 4KW panel capacity seems sensible. The "communication issue" between the SNRE MPPT Controller and Victron can be resolved using available software solutions to retrieve data.


### Battery Configuration

For the battery configuration, the recommended approach is to go with a DIY setup. This involves creating a 13/14 kWh battery at 48V, which translates to a capacity of about 280 Ah to 300 Ah. This configuration includes a 150 A Battery Management System (BMS) with Active Balancing, along with all the necessary safety equipment.



### Terrase East Wall

A small array ranging from 800W to 2KW, consisting of 2 to 6 panels with power outputs between 350W to 550W each, is proposed for the Terrase East Wall. The primary objective is to harness morning to noon sunlight efficiently to cover power usage for low-demand devices and mitigate power peaks. However, despite its simplicity, this option might not provide the most favorable return on investment. Additionally, the presence of a hill may impact the system's early morning startup.

Here are the yearly energy production estimates (in kWh) for different configurations:

| Power Capacity | Slope (degrees) | Azimuth (degrees) | Yearly Energy Production (kWh) | My Estimation(kWh) |
|----------------|-----------------|------------------|--------------------------------|-------------------|
| 800W           | 90              | -20              | 588.19                         |  -125 kWh     463.19 kWh |
| 800W           | 90              | 0                | 590.28                         |  -125 kWh     465.28 kWh |
| 800W           | 90              | 20               | 582.23                         |  -125 kWh     457.23 kWh |
| 1.6KW          | 90              | -20              | 1177.38                        |  -250 kWh     927.38 kWh |
| 1.6KW          | 90              | 0                | 1180.57                        |  -250 kWh     930.58 kWh |
| 1.6KW          | 90              | 20               | 1164.45                        |  -250 kWh     914.45 kWh |
| 2KW            | 90              | -20              | 1470.47                        |  -300 kWh     1170.47 kWh |
| 2KW            | 90              | 0                | 1475.71                        |  -300 kWh     1175.71 kWh |
| 2KW            | 90              | 20               | 1455.57                        |  -300 kWh     1155.57 kWh |


**Estimated Production and Return on Investment**

My estimation is to exclude the months of January, February, November, and December from the production calculations. As observed, the azimuth angle does not significantly impact overall production. Therefore, for this setup, inexpensive micro-inverters with 2 or 4 ways, or a small 2KW or 2.5KW grid-tied inverter, are suitable for the inverter configuration.

### Potential Return on Investment:

| Power Capacity | Supplier Cost per kWh (€) | Invested Money (€) | Yearly Production kWh |  Yearly Saved Money (€) | ROI Time (years) |
|----------------|---------------------------|--------------------|-----------------------|----------------------|------------------|
| 800W           | 0.3                       | 800                | 460                   | 138                  | 5.8              |
| 800W           | 0.4                       | 800                | 460                   | 184                  | 4.4              |
| 800W           | 0.5                       | 800                | 460                   | 230                  | 3.5              |
| 800W           | 0.6                       | 800                | 460                   | 276                  | 2.9              |
| 800W           | 0.7                       | 800                | 460                   | 322                  | 2.5              |
| 800W           | 0.8                       | 800                | 460                   | 368                  | 2.2              |

| Power Capacity | Supplier Cost per kWh (€) | Invested Money (€) | Yearly Production kWh |  Yearly Saved Money (€) | ROI Time (years) |
|----------------|---------------------------|--------------------|-----------------------|----------------------|------------------|
| 1600W          | 0.3                       | 1250               | 930                   | 279                  | 4.5              |
| 1600W          | 0.4                       | 1250               | 930                   | 372                  | 3.4              |
| 1600W          | 0.5                       | 1250               | 930                   | 465                  | 2.7              |
| 1600W          | 0.6                       | 1250               | 930                   | 558                  | 2.3              |
| 1600W          | 0.7                       | 1250               | 930                   | 651                  | 2.0              |
| 1600W          | 0.8                       | 1250               | 930                   | 744                  | 1.7              |

Based on the analysis, it is evident that the return on investment improves with higher power capacities and lower supplier costs per kWh. Additionally, installing a 1600W array (4 panels) generally results in a better ROI compared to an 800W array (2 panels). These insights can guide decision-making to optimize the PV array setup and achieve the best return on investment.

### Daily Power Usage Hints

The Daily Evaluated "Regular" Usage is set to 0.4kW for 16 hours: 0.4kW * 16 = 6.4 kWh

Let say there is a production of 0.4 kW from 9 to 13: 0.4kW * 4 = 1.6 kWh
It means a reduction of 25% on the "Regular" usage.
Let say it works only during 6 month during the year and only 4 hours daily: 182.5 * 4 * 0.4 kW = 292 kWh
It removes about 6.48 % of the total bill, and 12.5 % of the Daily Evaluated "Regular" Usage.

Checking the Daily Charge there are patterns when you cook at lunch time from 11h to 13h, from 1KW to 3KW most of the time for 15 minutes at least to about 1 hour or bit more, in such case 4 panels may handle this, but you will 'loose' a lot of production. Moving from 2 panels to 4 panels is a 300 € to 400 € change. Adding a small battery with a hybrid inverter will make sense to cover both the lunch cooking time and the dining cooking time, however the budget is quiet different, I will discuss about this scenario later.

#### August 2023 Price Analysis


Upon revisiting this section, I've identified significant cost-saving opportunities. A new supplier offering budget-friendly PV panels has allowed for substantial reductions in expenses.
More or less add 150/200 € for an Electronic Box with Protections + the Earth Cable.

**2 Panels Configuration:**

- Hoymiles HMS-800 Micro Inverter: 231.93€ + EndKappe 6.90 € + Cable 69.90 € + 50€ Transport [Source](https://www.offgridtec.com/hoymiles-hms-800-2t-microinverter-modulwechselrichter.html): 358.73 €
- 2 * PV Panel 385W: 2 * 99€ [Source](https://www.chocdiscount.com/panneaux-solaires/25763-panneau-solaire-amerisolar-385w-as-6m120-hc-demi-cellules-black.html) + 128 € Transport: 326 €
- Total Price: 684.73 € 
   - Kit with the same inverter: [Link](https://www.offgridtec.com/offgridtec-balkonkraftwerk-solardirect-luxen-wifi-900w-hm-800.html) (800 € without transport)

- *Interesting kit 700W*: 2 375W Panels + Hoymiles HMS-700 Micro Inverter + Caps 399 € + Cable 10 m 37.7 + Transport 128€ : Total 564.70 €
  [Link](https://www.chocdiscount.com/kits-solaires-autoconsommation/21837-kit-solaire-750w-2-panneaux-dmegc-375w-autoconsommation-1-micro-onduleur-hoymiles-hm700-essentiel.html)
 

**4 Panels Configuration:**

- Hoymiles HM-1500 Microinverter: 278.86 + EndKappe 6.90 + Cable 69.90 € + 4 * 11.19 € MC4 2m + 50€ Transport [Source](https://www.offgridtec.com/hoymiles-hm-1500-microinverter-modulwechselrichter.html): 450,42 €
- 4 * PV Panel 385W: 4 * 99€ + 128 € including Transport [Source](https://www.chocdiscount.com/panneaux-solaires/25763-panneau-solaire-amerisolar-385w-as-6m120-hc-demi-cellules-black.html): 524 € 
- Total Price: 974.42 €
   - Kit with the same inverter: [Link](https://www.offgridtec.com/offgridtec-balkonkraftwerk-1700w-hm-1500-dtu-wlite-trina-vertex-s-425-mini-pv-solaranlage.html) (1130.38 € without transport)
   
** 4 Panels Configuration 2:**
- Hoymiles HMS-2000-4T Microinverter: 327.13 + EndKappe 6.90 + Cable 69.90 € + 4 * 11.19 € MC4 2m + 50€ Transport [Source](https://www.offgridtec.com/hoymiles-hms-2000-4t-microinverter-modulwechselrichter.html): 498,69 €
-  4* PV Panel: 4 * 143.99 + 128 € Transport: 703.96 [Source](https://autosolar.es/panel-solar-24-voltios/panel-solar-545w-ja-solar-mono-perc)
- Total Price: 1202.65 €

- *Interesting kit 1400W*: 4 375 Panels + 2 Hoymiles HMS-700 Micro Inverter + 2 * MC4 1m + Caps 798 €  + 2* 37.7 € Cable 10 m + 128 € Transport: 1001 € [Source](https://www.chocdiscount.com/kits-solaires-autoconsommation/23298-kit-solaire-1500w-4-panneaux-dmegc-375w-autoconsommation-2-micro-onduleurs-hoymiles-hm700-essentiel.html)
It is about the same price as the single 1500W configuration, the advantage is to have 2 small PV arrays that can be oriented differently (East, South for instance)

**Power Capacity Analysis:**

| Power Capacity | Supplier Cost per kWh (€) | Invested Money (€) | Yearly Production kWh | Yearly Saved Money (€) | ROI Time (years) |
|----------------|---------------------------|--------------------|-----------------------|----------------------|------------------|
| 770W           | 0.3                       | 690                | 450                   | 135                  | 5.1              |
| 770W           | 0.4                       | 690                | 450                   | 180                  | 3.8              |
| 770W           | 0.5                       | 690                | 450                   | 225                  | 3.1              |
| 770W           | 0.6                       | 690                | 450                   | 270                  | 2.6              |
| 770W           | 0.7                       | 690                | 450                   | 315                  | 2.2              |
| 770W           | 0.8                       | 690                | 450                   | 360                  | 1.9              |

**Power Capped by Micro Inverter:**

| Power Capacity | Supplier Cost per kWh (€) | Invested Money (€) | Yearly Production kWh | Yearly Saved Money (€) | ROI Time (years) |
|----------------|---------------------------|--------------------|-----------------------|----------------------|------------------|
| 1500W          | 0.3                       | 980                | 873                   | 261                  | 3.8              |
| 1500W          | 0.4                       | 980                | 873                   | 349                  | 2.8              |
| 1500W          | 0.5                       | 980                | 873                   | 436                  | 2.3              |
| 1500W          | 0.6                       | 980                | 873                   | 523                  | 1.9              |
| 1500W          | 0.7                       | 980                | 873                   | 611                  | 1.6              |
| 1500W          | 0.8                       | 980                | 873                   | 698                  | 1.4              |


**Power Capped by Micro Inverter Cfg. 2:**
| Power Capacity | Supplier Cost per kWh (€) | Invested Money (€) | Yearly Production kWh | Yearly Saved Money (€) | ROI Time (years) |
|----------------|---------------------------|--------------------|-----------------------|----------------------|------------------|
| 2000W          | 0.3                       | 1210               | 1164                  | 349                  | 3.5              |
| 2000W          | 0.4                       | 1210               | 1164                  | 465                  | 2.6              |
| 2000W          | 0.5                       | 1210               | 1164                  | 582                  | 2.1              |
| 2000W          | 0.6                       | 1210               | 1164                  | 698                  | 1.7              |
| 2000W          | 0.7                       | 1210               | 1164                  | 814                  | 1.5              |
| 2000W          | 0.8                       | 1210               | 1164                  | 931                  | 1.3              |



As you can see, attention to detail matters. If transportation can be sourced from the same place, additional savings can be achieved.
The 4-panel configuration, featuring the most economical PV panels and a 1.5KW microinverter, significantly enhances ROI. In fact, the improvement is nearly an order of magnitude compared to the previous setup.
A further improvement will be to have the 2KW microinverter and 4 * 550W panels, the ROI is a bit better.


#### 6 Panel Inverter Configuration
Let's explore another intriguing configuration:

**6 Panels Configuration:**

- Solax X1 Mini 2.0 2KW: 349 € + 19 € Transport ([Source](https://www.chocdiscount.com/onduleur-reseau/128-onduleur-solaire-reseau-solax-x1-mini-20-2000-watts-garantie-10-ans.html)) = 368 € (excluding cables, fuses, and other components)
- 6 * PV Panel 385W: 6 * 99 € ([Source](https://www.chocdiscount.com/panneaux-solaires/25763-panneau-solaire-amerisolar-385w-as-6m120-hc-demi-cellules-black.html)) + 128 € including Transport = 722 €
- Total Price: 1240 €

**Power Capped by the Inverter**

| Power Capacity | Supplier Cost per kWh (€) | Invested Money (€) | Yearly Production kWh | Yearly Saved Money (€) | ROI Time (years) |
|----------------|---------------------------|--------------------|-----------------------|----------------------|------------------|
| 2000W          | 0.3                       | 1250               | 1150                  | 345                  | 3.6              |
| 2000W          | 0.4                       | 1250               | 1150                  | 460                  | 2.7              |
| 2000W          | 0.5                       | 1250               | 1150                  | 575                  | 2.2              |
| 2000W          | 0.6                       | 1250               | 1150                  | 690                  | 1.8              |
| 2000W          | 0.7                       | 1250               | 1150                  | 805                  | 1.6              |
| 2000W          | 0.8                       | 1250               | 1150                  | 920                  | 1.4              |

The ROI should improve further due to the 2.310 KW PV array.

Opting for a more classic orientation (20 Slope, 20 Azimuth), yearly production increases to 2069 kWh (estimated 1809 kWh). This further enhances the ROI.

| Power Capacity | Supplier Cost per kWh (€) | Invested Money (€) | Yearly Production kWh |  Yearly Saved Money (€) | ROI Time (years) |
|----------------|---------------------------|--------------------|-----------------------|----------------------|------------------|
| 2000W          | 0.3                       | 1250               | 1800                  | 540                  | 3.33             |
| 2000W          | 0.4                       | 1250               | 1800                  | 720                  | 2.5              |
| 2000W          | 0.5                       | 1250               | 1800                  | 900                  | 2                |
| 2000W          | 0.6                       | 1250               | 1800                  | 1080                 | 1.66             |
| 2000W          | 0.7                       | 1250               | 1800                  | 1260                 | 1.43             |
| 2000W          | 0.8                       | 1250               | 1800                  | 1440                 | 1.25             |

Please note that since it's a grid-tied inverter, power should be consumed when produced. However, coupling this with the possibility of utilizing the Victron Multiplus II to store excess energy in the battery (with some additional losses) makes this a compelling option.
It is also possible to make the same interesting configuration with 4 * PV Panel 550W, which is in my opinion more interesting because you need less cables, and it takes less area.



#### November 2023 Price Update

There are a few price changes for November.
The interesting part is that there are affordable bifacial panels at 99 €: https://www.chocdiscount.com/panneaux-solaires/35301-panneau-solaire-jolywood-415w-full-black-ntype-bifacial-jw-hd108n.html (415W @ 1000W/m², 315W @ 800W/m²).
The price of few Victron inverters is lower too: less than 1300 € for Victron Multiplus 2/5000VA (https://allo.solar/convertisseur-chargeur-5000va-48v-70a-multiplus-ii-victron-energy.html) and less than 800 € for Victron Multiplus 2/3000VA (https://allo.solar/convertisseur-chargeur-3000va-48v-35a-multiplus-ii-victron-energy.html).
There is also a new 'middle' size panel of 460W (190 9mm * 1134 mm * 30 mm): https://www.chocdiscount.com/panneaux-solaires/49346-panneau-solaire-leapton-460w-cadre-noir-lp182182-m60-mh.html for 99 €, it is really interesting.



Various Configurations : for the 415W Bifacial panel (Yearly Evaluation removing from October to February)
- 8 * 415 W : 3320 W peak. 
  About 60A @ 55.2V for charging the battery.
  4S/2P: 175.7V / 118.3V.
  3287 kWh/Yearly @ Slope 10 deg/Azimuth 20 deg, eval 2700 kWh/Yearly.
  3435 kWh/Yearly @ Slope 20 deg/Azimuth 20 deg, eval 2800 kWh/Yearly.
- 9 * 415 W : 3735 W peak. 
  About 67A @ 55.2V for charging the battery.
  3S/3P: 131.8V / 88V.
  3698 kWh/Yearly @ Slope 10 deg/Azimuth 20 deg, eval 3067 kWh/Yearly.
  3865 kWh/Yearly @ Slope 20 deg/Azimuth 20 deg, eval 3142 kWh/Yearly.
- 10 * 415 W : 4150 W peak. 
  About 83A @ 55.2 V for charging the battery.
  5S/2P: 219.6V / 148.3V.
  4109 kWh/Yearly @ Slope 10 deg/Azimuth 20 deg, eval 3408 kWh/Yearly.
  4294 kWh/Yearly @ Slope 20 deg/Azimuth 20 deg, eval 3493 kWh/Yearly.
- 12 * 415 W : 4980 W peak. 
  About 90A @ 55.2 V for charging the battery. Split in 2 arrays of 6 panels, less than 60 A for each.
  3S/2P (*2): 131.8V / 86.6V.
  4931 kWh/Yearly @ Slope 10 deg/Azimuth 20 deg, eval 4089 kWh/Yearly.
  5153 kWh/Yearly @ Slope 20 deg/Azimuth 20 deg, eval 4191 kWh/Yearly.
  
Various Configurations : for the 460W panel   (Yearly Evaluation removing from October to February)
- 8 * 460 W : 3680 W peak
  About 66.7A @ 55.2V for charging the baterry. Taking in account cables, most likely about 73A.
  4S/2P: 192.9V / 132.2V
  3643 kWh/Yearly @ Slope 10 deg/Azimuth 20 deg, eval 3020 kWh/Yearly.
  3808 kWh/Yearly @ Slope 20 deg/Azimuth 20 deg, eval 3097 kWh/Yearly.
- 10 * 460 W : 4600 W peak
  About 83 A @ 55.2 V for charging the battery. Taking in account cables and low temperature, most likely about 91A.
  5S/2P: 241.2V / 165.7V
  4554 kWh/Yearly @ Slope 10 deg/Azimuth 20 deg, eval 3777 kWh/Yearly.
  4760 kWh/Yearly @ Slope 20 deg/Azimuth 20 deg, eval 3871 kWh/Yearly.
- 12 * 460 W : 5520 W peak
  About 50A @ 55.2V, 2 arrays of 6 panels for charging the battery.  Taking in account cables and low temperature, most likely about 54 A.
  3S / 4P (*2): 144.7V / 98.8V.
  5465 kWh/Yearly @ Slope 10 deg/Azimuth 20 deg, eval 4532 kWh/Yearly.
  5712 kWh/Yearly @ Slope 20 deg/Azimuth 20 deg, eval 4645 kWh/Yearly.
  
  
  
	
#### December 2023 Price Update

There are a few price changes for December, more specifically 24/12.
The most interesting one is the for the Victron inverters that are finally in the 1000 € (tax included) for the Victron Multiplus 2/5000VA (https://verkauf-bochum.de/en/products/multiplus-ii-48-5000-70-50).
Regarding the panels there is not a major change on the pricing.
The interesting panel from November 2003 is at 95 € instead of 99 € https://www.chocdiscount.com/panneaux-solaires/35301-panneau-solaire-jolywood-415w-full-black-ntype-bifacial-jw-hd108n.html (415W @ 1000W/m², 315W @ 800W/m²). The 'middle' size panel of 460 W however increased from 99 € to 139 €  https://www.chocdiscount.com/panneaux-solaires/49346-panneau-solaire-leapton-460w-cadre-noir-lp182182-m60-mh.html.
There is an interesting more efficient 'middle' size panel  with 500 W for 119 € https://autosolar.es/panel-solar-24-voltios/panel-solar-500w-tensite-monocristalino-perc, meaning with only 8 panels you have 4KW peak, if you can put longer panels it is an advantage with respect to the 400 W panels, you use less width. Sizing for the MPPT 250V/70A or 250V/85A to prevent a bit the clipping (4S/2P configuration, 90A at the lowest temperature and 72.2A at the max temperature, voltage  199.4V @ min temperature and 130.1V @ max temperature).  Actually a 70A is enough if you consider the aging of the panels.  You can add another panel in serie and go in 5S/2P, in this case you need more a MPPT 250V/85A or 250V/100A you really push the enveloppe on both the voltage at 249V @ min temperature and more than 100 A at the lowest temperature).
Another configuration in such case would be to run 2 MPPTs in 2S/2P with super-oversized 150V/60A (242€ each, that would be able to cope without any issue with 2S/3P, or 3S/2P), it adds a few more wires but less peak voltage and peak amps overall instead of putting a single 250V/100A MPPT controller. It is may be more versatile, you can start with 8 panels and update to 10 and 12 panels without majors changes on the installation.
Meaning starting from 4KW and ramp-up to 5KW then to 6KW, without change on the wires and the MPPT controllers (100V to 150V from 2S to 3S).
If you consider aging 4KW goes down to 3.4 KW, 5KW goes down to 4.25 KW and 5KW goes down to 5.1 KW after 20/25 years.

The affordability of the Victron inverter is a huge change, it drops from nearly 2000 € to 1000 € within a year.
Basically, it means you can buy the inverter with a 4 KW PV array for 2000 € (not including shipping and all other accessories needed, especially the battery and the MPPT controller). 

Regarding the MPPT controller, there is a small change on the price, for the SNRE 250/70A from 350 € to 290 €, the SNRE 250/85A from 430 € to 392 €, the SNRE 250/100A from 475 € to 450 €.


#### February 2024 Price Update

Following the issues in the Red Sea impacting the sea traffic: I think there will be an increase in price in the forthcoming months even if the stock is accumulating.
There is a small increase on the price of the Victron Multiplus 2/5000VA around 950 to 1100 € (https://verkauf-bochum.de/en/products/multiplus-ii-48-5000-70-50)
Regarding the panels, there are opportunities in the 375W range going down to 74 € (https://www.chocdiscount.com/panneaux-solaires/35512-panneau-solaire-dmegc-375w-dm375m6-60hsw-.html) and 78 € (https://www.chocdiscount.com/panneaux-solaires/55233-panneau-solaire-dmegc-375w-dm375m6-60hbb-full-black.html), with respectively 5.06 W per € and 4.68 W per €. Those are the most cost effective solutions on the market. 10 panels delivered are less than 1000 € (including VAT). Prices are crazy in Germany, the removal of the VAT tax has just increase the marging of the reseller and not reduced the price. Panels are cheaper in France and in Spain even if you include the VAT.
Another 460W panel may be worth with 119 € (https://www.chocdiscount.com/panneaux-solaires/82249-panneau-solaire-jolywood-460w-hd144n-460w-bifacial.html).

The efficient 'middle' size panel with 500 W is still at 119.79 € and now down to 113.14 € https://autosolar.es/panel-solar-24-voltios/panel-solar-500w-tensite-monocristalino-perc
which is less cost effective with about 4.17 W per €, than the small 375W panels.

For the grid-tied inverters, there is a good deal on the 1.5KW SOLAX X1 Mini around 278 € (https://www.chocdiscount.com/onduleur-reseau/127-onduleur-solaire-reseau-solax-x1-mini-15-1500-watts-garantie-10-ans.html). Personnaly, I think it is a better deal than any micro-inverter, also you can do zero injection on the grid with this inverter if you add a sensor. If you put the previous cheapest panels at 74€ a piece: you can build a small 4 panels system for about 1000 € (with all cables, required protections,the structure for the panels and the shipping).

460W Panel (https://www.chocdiscount.com/panneaux-solaires/82249-panneau-solaire-jolywood-460w-hd144n-460w-bifacial.html) study. This panel has nice dimensions : 2108 mm * 1042 mm * 30 mm. The height is a bit larger and the width is narrower, allowing me to put more panels and harvesting more power with less panels.
2S/3P, 20m cable 6 mm², PV max voltage @ min temperature -30C 118.5V, PV min voltage @ max temperature 40C 75.2V , Battery Inverter 150V/60A or 150V/70A: 2760 W peak. Cost more on the cables and the inverter a bit less, not really sure it is worth it. 30 € more on a 250V inverter with the same amps.
3S/2P, 20m cable 6 mm², PV max voltage @ min temperature -30C 177.8V, PV min voltage @ max temperature 40C 116.1V, Battery Inverter 250V/60A or 250V/70A: 2760 W peak. 
4S/2P, 20m cable 6 mm², PV max voltage @ min temperature -30C 237.1V, PV min voltage @ max temperature 40C 155.7V, Battery Inverter 250V/85A or 250V/100A: 3680 W peak. (70A is undersized a bit)
3S/3P,  20m cable 6 mm², PV max voltage @ min temperature -30C 177.8V, PV min voltage @ max temperature 40C 114.8V, Battery Inverter 250V/85A or 250V/100A: 4140 W peak. (70A is undersized a bit)
4S/3P, 20m cable 6 mm², PV max voltage @ min temperature -30C 237.1V, PV min voltage @ max temperature 40C 154.4V, Battery Inverter 250V/100A (clipping): 5520 W peak. Or change it in 2 * 3S/2P.


415W Panel (https://www.chocdiscount.com/panneaux-solaires/35301-panneau-solaire-jolywood-415w-full-black-ntype-bifacial-jw-hd108n.html) study. This is a good bang for the buck panel.
3S/2P, 20m cable 6 mm², PV max voltage @ min temperature -30C 131.8V, PV min voltage @ max temperature 40C 86.9V , Battery Inverter 150V/60A (or under): 2490 W peak. 
4S/2P, 20m cable 6 mm², PV max voltage @ min temperature -30C 175.7V, PV min voltage @ max temperature 40C 116.9V , Battery Inverter 250V/60A or 250V/70A: 3320 W peak. 
3S/3P,  20m cable 6 mm², PV max voltage @ min temperature -30C 131.8V, PV min voltage @ max temperature 40C 85.3V , Battery Inverter 150V/60A (clipping), 150V/70A (less clipping) or 250V/85A: 3735 W peak.
5S/2P, 20m cable 6 mm², PV max voltage @ min temperature -30C 175.7V, PV min voltage @ max temperature 40C 116.9V , Battery Inverter 250V/60A (clipping), 250V/70A (less clipping) or 250V/85A: 4150 W peak.
4S/3P,  20m cable 6 mm², PV max voltage @ min temperature -30C 175.7V, PV min voltage @ max temperature 40C 115.3V , Battery Inverter 250V/85A (clipping), 250V/100A (less clipping): 4980 W peak.

Length in portrait mode, to make a fence.

| 460W Panels | Length (mm) | Power Peak (W) | 
|-------------|-------------|----------------|
|   6         |  6252       |  2760          |
|   8         |  8336       |  3680          |
|   9         |  9378       |  4140          |
|  12         | 12504       |  5520          |

| 415W Panels | Length (mm) | Power Peak (W) |
|-------------|-------------|----------------|
|   6         |  6804       |  2490          |
|   8         |  9072       |  3320          |
|   9         |  10206      |  3735          |
|  10         |  11340      |  4150          |
|  12         |  13608      |  4980          |







#### Battery tied Configuration

I am interested also in battery based solutions and most of MPPT battery chargers are known for being effective from a conversion point of view.
I am investigating different array size and configuration, along with various MPPT controllers.

| MPPT Model | Amps (A) | Voltage (V) | PV Max Voltage (V) | Price (€) |
|------------|----------|-------------|--------------------|-----------|
| [SNRE MC4860N15](https://fr.aliexpress.com/item/1005004674334241.html?spm=a2g0o.store_pc_groupList.8148356.10.2fdbc85b74K4uY&pdp_npi=3%40dis%21EUR%21%E2%82%AC%20264%2C07%21%E2%82%AC%20203%2C33%21%21%21%21%21%402101f49a16936392187478334ea022%2112000030061281026%21sh%21LU%21839344662)           |    60      |     48      | 150 | 270 |
| [SNRE MC4870N15](https://fr.aliexpress.com/item/1005004674334241.html?spm=a2g0o.store_pc_groupList.8148356.10.2fdbc85b74K4uY&pdp_npi=3%40dis%21EUR%21%E2%82%AC%20264%2C07%21%E2%82%AC%20203%2C33%21%21%21%21%21%402101f49a16936392187478334ea022%2112000030061281026%21sh%21LU%21839344662) | 70 | 48 | 150 | 293 |
| [SNRE MC4860N25](https://fr.aliexpress.com/item/1005004674334241.html?spm=a2g0o.store_pc_groupList.8148356.10.2fdbc85b74K4uY&pdp_npi=3%40dis%21EUR%21%E2%82%AC%20264%2C07%21%E2%82%AC%20203%2C33%21%21%21%21%21%402101f49a16936392187478334ea022%2112000030061281026%21sh%21LU%21839344662) | 60 | 48 | 250 | 284.3 |
| [SNRE MC4860N25](https://fr.aliexpress.com/item/1005004674334241.html?spm=a2g0o.store_pc_groupList.8148356.10.2fdbc85b74K4uY&pdp_npi=3%40dis%21EUR%21%E2%82%AC%20264%2C07%21%E2%82%AC%20203%2C33%21%21%21%21%21%402101f49a16936392187478334ea022%2112000030061281026%21sh%21LU%21839344662) | 60 | 48 | 250 |  316 | 


Most of the time the first limiting factor is th PV input with 150 V and 250 V for such MPPT controllers, then of course the number of current that can be used to reload the battery.
For the cheap 385 W PV Array, I performed a few check with the Victron MPPT calculator, to check the limits at -30 C, 40 C and 80 C for the currents and voltage assuming 6 mm^2 and 10 m cable. Battery Voltage 48V, Floating voltage at 54V (may be a bit too much for 48V system, 52.5V may be more realistic)

Core configurations from where to derive all parallel configurations. Min temperature: max voltage and max current output, and of course Max Temperature: min voltage and min current output.
| Configuration | Array Peak Power (W) | Max/Medium/Min Current (A) | Max/Medium/Min Voltage (V) |
|---------------|----------------------|----------------------------|----------------------------|
|  2S/1P        |  770                 | 18.1 / 15.1 / 13.2         | 97.4 / 66.2 /  56.7        | 
|  3S/1P        | 1155                 | 27.7 / 22.6 / 19.8         | 146.1 / 99.6 / 85.4        | 
|  4S/1P        | 1540                 | 36.5 / 30.4 / 26.7         | 194.8 / 133.1 / 114.1      | 
|  5S/1P        | 1925                 | 45.7 / 38.0 / 33.3         | 243.5 / 166.5 / 142.8      | 

| Configuration | Array Peak Power (W) | MPPT Controller | Max/Medium/Min Current (A) | 
|---------------|----------------------|-----------------|----------------------------|
|  4S/2P        | 3080      | 250V/60A        | 60 / 60 / 53.3 (limited by temp) |
|  5S/2P        | 3850      | 250V/60A        | 60 / 60 / 60 (limited, a bit oversized array)       |
|  5S/2P        | 3850      | 250V/70A        | 70 / 70 / 66.6 (limited by temp)  |
|  2S/2P        | 1540      | 150V/60A        | 36.2 / 30.2 / 26.4 |
|  2S/3P        | 2310      | 150V/60A        | 54.3 / 45.3 / 39.6 |
|  3S/2P        | 2310      | 150V/60A        | 55.4 / 45.2 / 39.6 |
|  2S/4P        | 3080      | 150V/60A        | 60 / 60 / 52.8 ( limited by temp) |
|  2S/4P        | 3080      | 150V/70A        | 70 / 60.4 / 52.8 ( limited by cold temp) |
|  3S/3P        | 3465      | 150V/60A        | 60 / 60 / 59.4 ( limited, a bit oversized array) | 
|  3S/3P        | 3465      | 150V/70A        | 70 / 67.8 / 59.4 ( limited by cold temp) |


Investigating section of the cable and the cable length from the PV Array to the Controller, I am just checking the lowest voltage configuration.

| Configuration | Section (mm^2) | Length (m) | Min Voltage (V) |
|---------------|----------------|------------|-----------------|
| 2S/1P         | 4              | 5          |  56.9           |
| 2S/1P         | 4              | 10         |  56.4           |
| 2S/1P         | 4              | 15         |  55.9           |
| 2S/1P         | 4              | 20         |  55.4           |
| 2S/1P         | 4              | 25         |  54.9           |
| 2S/1P         | 6              | 5          |  57.1           |
| 2S/1P         | 6              | 10         |  56.7           |
| 2S/1P         | 6              | 15         |  56.4           |
| 2S/1P         | 6              | 20         |  56.1           |
| 2S/1P         | 6              | 25         |  55.7           |

Higher voltage is better to reduce voltage drop on the wiring.
For a 4 mm^2 there is too much voltage drop above 10 m for such 2S configuration and max 20 A per string, but it will work fine with at least 3S configuration and above.
For a 6 mm^2 it is better suited for 2S configuration, it will handles at most 30 A per string.
For short connection you can use 4mm^2 and for long connection use 6mm^2 or bigger.
Given the price of cables and connections, if you have long cables it is cheaper to go to high voltage, less cables, less connection. 
Anyway, you need to compute and to check what it is worth and possible for your cases.
For my own perspective, it is possible to connect with 4 mm^2 PV panels and for anything longer than 5 meters put at least a 6 mm^2 and if possible use high voltage configuration.


Of course, it is important to have the shortest cable length from the MPPT controller to the battery due to the low voltage of the battery (48V).

## Concerns Regarding Micro Inverters

### Efficiency Considerations
Most of the time there is no curve about the efficiency of the Micro Inverters with respect to the PV array power input, why so ?
My gut feeling is that it is not good, otherwise all producers will talk about such performances with respect to 'regular' MPPT controllers.

### Aging Challenges
Putting an electronic device outdoor is not something to do lightly, in direct sun light the metal case will go slightly above 60 C, and behind a PV panel it will be similar  what to expect ? Even if the device is protected and having a cast resin for protection, the resin will age. Also, since there are several cycles of expansion/contraction such barrier will fail for sure relatively quickly. Most concerning for me is the passive electronic components such as capacitors and resistors that will age very quickly in such harsh environment, also note that for cost purpose no premium components able to cope with high temperature are used in such micro inverters. Also, the plastic around the case will fail quickly even if premium plastic material having UV protection is used, such components become brittle and it fails within 10 years.



### Streamlining Battery Storage for Efficiency

Efficiency considerations suggest that the current chain of electricity conversion may not be the most sensible approach: PV DC -> Grid AC -> Battery DC -> Grid AC.

The Micro Inverter first converts DC to AC, with a specific efficiency ratio. Subsequently, a Battery Charger reverts the AC back to DC. Finally, an Inverter transforms the Battery DC back into Grid AC. Each added step in this process results in energy loss due to conversions.

Given that the primary goal is to store energy efficiently, it would make more sense to directly route energy from PV DC to Battery DC using a Battery Charger. For the conversion from Battery DC to Grid AC, an inverter is the necessary choice.



## Slope of wall mounted array
 Even a few degrees can improve your yearly production as shown after, assuming a 2KW PV Array/MicroInverter in the following tab
| Slope (degrees) | Yearly Production Upper Bound (kWh) |  Gain (%)            | Power to Optimal (%) | Offset from the Wall (mm) - Panel Length 2278mm |  Offset from the Wall (mm) - Panel Length 1756 mm | Offset from the Wall (mm) - Panel "Length" 1038 mm |
|-----------------|-------------------------------------|----------------------|----------------------|-------------------------------------------------|---------------------------------------------------|----------------------------------------------------|
| 90  (Vertical)  |  1455                               |  NA - Baseline       |        68.55         | 0                                               | 0                                                 | 0 |
| 85              |  1567                               |  7.69                |        73.88         | 198.54                                          | 153.05                                            | 90.47 mm  | 
| 80              |  1672                               |  14.91               |        78.83         | 395.57                                          | 304.95                                            | 180.25 mm |
| 75              |  1764                               |  21.23               |        83.16         | 589.59                                          | 454.49                                            | 268.65mm  |
| 70              |  1846                               |  26.87               |        87.03         | 779.12                                          | 600.59                                            | 355.02 mm |
| 65              |  1919                               |  31.89               |        90.47         | 962.17                                          | 742.12                                            | 438.65 mm |
| 60              |  1981                               |  36.15               |        93.39         | 1139.00                                         | 878.00                                            | 519.00 mm |
| 35 (Optimal)    |  2121                               |  45.77               |        NA - Baseline | 1866.03                                         | 1438.43                                           | 850.28 mm |


The table shows that even a small 10 degrees angle from the wall improve slightly the power production to nearly 80% from less than 70% (about 300 kWh more on the year), the offset is about 300 to 400 mm from the wall in portrait mode, the offset is about 200 mm for such angle in landscape mode: it means you can slightly improve the production for the same offset in landscape mode. An offset of about 400mm will be about about 70 and 65 degrees, achieving about 88.5% of the Optimal Power, or if you prefer increase about 30% the Production with respect to put it the Panel against the Wall. But in practice, it may depend on your configuration.

Let see numbers for a small 2 panel system with a 0.700 W micro inverter.
The Slope is 68 degrees and the Azimuth -40 degrees.
Yearly PV production 635.89 kWh (removing Jan. Feb. Nov. Dec: 99 kWh):  536.89 kWh.
Let assume it cost 600 € to build it.

| Supplier Price €/kWh |Money Saved |  ROI (Years) |
|----------------------|------------|--------------|
| 0.25                 | 134.20     |  4.47        |
| 0.30                 | 161.00     |  3.73        |
| 0.40                 | 214.75     |  2.79        |
| 0.50                 | 268.44     |  2.24        |
| 0.60                 | 322.13     |  1.86        |
| 0.70                 | 375.82     |  1.60        |
| 0.80                 | 429.51     |  1.40        |


### Backyard Garden - Power Shed

The Backyard Garden setup involves an array of 4KW to 5KW (8 to 10 panels with 400W to 550W each) arranged in two rows. The array will be located in a shed or at a low height in the garden to facilitate maintenance and improve the return on investment. An orientation angle of 20 degrees is chosen for the shed. 

| Panel W | Row Size | Row Number | Total Power KW |
|---------|----------|------------|----------------|
| 400     | 4        | 2          | 3.2            |
| 400     | 5        | 2          | 4              |
| 550     | 4        | 2          | 4.4            |
| 550     | 5        | 2          | 5.5            |

| Power Capacity | Slope (degrees) | Azimuth (degrees) | Yearly Energy Production (kWh) | My Estimation (kWh) |
|----------------|-----------------|-------------------|--------------------------------|---------------------|
| 4KW            | 20              | -20               | 4145.78                        | 3595.78             |
| 4KW            | 20              | 0                 | 4174.03                        | 3624.03             |
| 4KW            | 20              | 20                | 4139.33                        | 3589.33             |

My estimation is to remove Jan, Feb, Nov, and Dec from the Production. Increasing the optimal slope to 35 degrees would result in a 100 kWh increase, but it is not feasible as it would significantly raise the height of the shed. Considering the production level, it becomes essential to store a significant portion of the energy in batteries for later use during the afternoon, night, and early morning. Due to the exposure and surroundings, the PV array starts relatively late in the morning, making the Terrace East Wall PV Array an attractive idea.

Configurations:


| Cfg | Panels             | Inverter                      | MPPT Controller         | Cost without Battery (€) *      | €/W       |
|-----|--------------------|-------------------------------|-------------------------|---------------------------------|-----------|
| 1   |  3850 (10 * 385)   |  Victron Multiplus II/48/5000 | SNRE 250/70A  (5S/2P)   | 990+1500+350 + 700 = 3540       | 0.9194    |
| 2   |  4360  (8 * 545)   |  Victron Multiplus II/48/5000 | SNRE 250/85A  (4S/2P)   | 1151.2+1500+485 + 700 = 3836.2  | 0.8798    |
| 3   |  4620  (12 * 385)  |  Victron Multiplus II/48/5000 | SNRE 250/85A  (4S/3P)   | 1188+1500+485 + 700 = 3873      | 0.8383    |
| 4   |  3465 (9 * 385)    |  Victron Multiplus II/48/5000 | SNRE 150/60A  (3S/3P)   | 891+1500+265 + 700 = 3356       | 0.9685    |


* Added 700 € of fixed cost for cables, switch, fuses, electric panel and protections...
Adding few more panels will reduce further the cost per watt, it is possible to add 2 additional panels (but there is not enough room to do so.)


Now let's explore the figures with the addition of the DIY battery:

| Configuration | Cost with Battery (€) | €/W    |
|---------------|-----------------------|--------|
| 1             | 6540                  | 1.6987 |
| 2             | 6836.2                | 1.5679 |
| 3             | 6873                  | 1.4876 |
| 4             | 6356                  | 1.8343 |

Observing the results, it becomes evident that having a slightly larger panel configuration is more beneficial in the long run. The cost difference of around 10% between the low-cost 3.85 KW configuration and the 4.62 KW configuration justifies opting for the latter. The decision mainly hinges on the feasibility of accommodating larger panels within your setup. Additionally, a slight oversizing of panels can enhance performance, even accounting for some 'clipping'; this leads to increased energy production during periods of lower sunlight.

When evaluating the power-to-surface ratio, configuration 2 stands out by utilizing less surface area. This aspect is advantageous if you intend to add more panels or minimize the land's impact.

It's worth noting that while fixed costs for the shed need to be factored in, they are unlikely to alter the observed trends, as we've already discussed. Also note that adding panels increase the fixed cost for cables, screws and additional human work.


Using a 85A MPPT controller we would have the following figures:
| Voltage (V)  | PV Array Peak (KW) |
|--------------|--------------------|
| 57           |     4.845          |
| 54           |     4.590          |
| 52.5         |     4.462          |
Which means the configuration 2 and 3 will be correctly dimensionned (also after aging).

Using a 70A MPPT controller we would have the following figures:
| Voltage (V)  | PV Array Peak (KW) |
|--------------|--------------------|
| 57           |     3.990          |
| 54           |     3.780          |
| 52.5         |     3.675          |
Only the configuration 1 will work with the 70A MPPT controller.


Let's explore the mean daily production for Configuration 2, with a cap of 4.360 KW on the PV array. The yearly production is estimated at 3947 kWh (4511 - 564, removing Jan., Feb., Nov., Dec.)

| Month | Daily Mean Upper Bound (kWh) |
|-------|------------------|
|  Jan  |   3.95           |
|  Feb  |   7.03           |
|  Mar  |  12.22           |
|  Apr  |  17.76           |
|  May  |  18.54           |
|  Jun  |  19.96           |
|  Jul  |  19.51           |
|  Aug  |  17.16           |
|  Sep  |  14.76           |
|  Oct  |   8.90           |
|  Nov  |   4.63           |
|  Dec  |   3.41           | 

On average, the daily mean ranges between 12.3 kWh and 13.7 kWh (4500 to 5000 kWh yearly). It's important to acknowledge that while this single array theoretically provides adequate power from March to September, practical factors suggest a more realistic timeframe from April to mid-September. Unaccounted shadows can lead to diminished production during this period.
25 years, let assume 20% reduction so about 3.5 KW

Let's explore the mean daily production for Configuration 1, with a cap of 3.850 KW on the PV array. The yearly production is estimated at (3984 - 499 =  3485, removing Jan., Feb., Nov., Dec.)

| Month | Daily Mean Upper Bound (kWh) |
|-------|------------------|
|  Jan  |   3.48           |
|  Feb  |   6.21           |
|  Mar  |  10.77           |
|  Apr  |  15.66           |
|  May  |  16.38           |
|  Jun  |  17.63           |
|  Jul  |  17.22           |
|  Aug  |  15.16           |
|  Sep  |  13.03           |
|  Oct  |   7.83           |
|  Nov  |   4.10           |
|  Dec  |   3.03           |

Similarly the daily mean is covered on the same period, there is less 'overproduction' theoritically, but sometimes it more like 17 or 19 kWh on the daily basis. Also we do not take in account the efficiency of the battery charger and so on. My feeling tells me it is a bit undersized, but sometimes you do not have the choice.
25 years, let assume 20% reduction so about 3 KW



### Middle Garden

The Middle Garden setup shares similarities with the Power Shed configuration. It can feature either one or two rows of panels, adhering to the same specifications. The orientation and performance characteristics remain consistent, with the added benefit of a slightly earlier startup when compared to the Power Shed setup. Despite the potential advantages of bifacial panels, they are excluded from consideration due to their elevated cost and minimal power gain, which fails to justify the investment.

In instances where the inverter possesses sufficient capacity, a viable strategy involves placing only panels, the MPPT controller, and the battery. This approach leads to cost savings and reduces nighttime power consumption associated with an additional inverter. However, this method might lead to a slightly amplified overproduction during the summer months.

From a cost point of view, just putting a few pillars and beams, it is slightly more cost effective than the Power shed if the main purpose is to provide power. 

### House Roof

Mounting panels on the house roof is not the preferred choice, primarily due to the high associated costs and the impracticality of undertaking the installation independently. In Luxembourg, the cost factor acts as a significant deterrent, making it more financially viable to opt for a DIY three-phase 15KW system. This alternative stands out as a preferable choice, even considering potential government assistance.


  
 
# Offgrid case

# Reduce oversizing idea

Just exploring an idea.
I think the main issue in our latitudes is about optimizing the performance of the PV array for Winter in order to reduce overproduction.

Given a fixed azimuth, let's try to check what is the slope for Winter (assuming a 4KW PV array).

| Slope Angle | Month |  Production kWh | Min kWh |
|-------------|-------|-----------------|---------|
| 45          | Jan   |  137            |         |
| 45          | Feb   |  210            |         |
| 45          | Nov   |  154            |         |
| 45          | Dec   |  125            |  125    |
| 55          | Jan   |  141            |         |
| 55          | Feb   |  213            |         |
| 55          | Nov   |  158            |         |
| 55          | Dec   |  130            |  130    |
| 65          | Jan   |  142            |         |
| 65          | Feb   |  211            |         |
| 65          | Nov   |  159            |         |
| 65          | Dec   |  132            |  132    |
| 75          | Jan   |  139            |         |
| 75          | Feb   |  203            |         |
| 75          | Nov   |  155            |         |
| 75          | Dec   |  131            |  131    |

From 65 to 75 degrees for the slope, it seems we found a good range to optimize for the highest minimal production during the year.
Let's assume 65 degrees, with such orientation there is a flat power production from April to September with a monthly 400 kWh (mean of 13 kWh daily).

In any case December is the minimum production in this area, 132 kWh means about 4.25 kWh daily.

If you need loosely about 13 kWh daily in December, it means you need at least 12 KW of such panels, and you will overproduce monthly more than 1200 kWh from April to September (mean of 39 kWh daily), probably you need at least a buffer of 3 to 4 days at least: 39 to 52 kWh of battery. At least 4 DIY batteries: 4 * 3 K€  = 12 K€ at the bare minimum, with a usable capacity of 80 % with 280 Ah of storage: 0.8 * 48 * 280 * 4 =  43 kWh of effective use of the battery, it is a 3.3 day buffer, adding another battery move it to 4 short days for 15 K€.
A 12 KW PV array is about 24 to 36 panels costing about 3.5 K€ to 4.5 K€, this is small with respect to the battery needs.
Let say you have 3 times a 4 KW PV array, you need 3 MPPTs of 85 A, for the inverter it depends, ideally you want to minimize the zero load power sucked by the inverter(s).

# Multiple inverters with different power rating

I think it might be a good idea to have inverters with different zero load.
For instance, you can have a 'small 3KW' Victron Multiplus II that consumes nothing and it is enough for to the light, the computers, and small main loads.
The small 3KW will switch down the other inverters during the night to not have the zero load power of other inverters, since it is not efficient to run power angry devices during the night, even if there is a battery, because charging the battery is not efficient.
Of course, it will be very interesting to have an efficient power on demand device able to detect the need for lot of current and switch automatically on the inverters as needed and shut them down very quickly (actually it is possible and already implemented in all CPUs, that are pumping a lot of current...)


# Tips

## Identifying phase

Small trick to quickly find which plug in on which phase, I used my Devolo Power line adaptors.
If the home icon is not green and red, then you are not on the same phase.
Otherwise, if it is green,  you are on the same phase.





