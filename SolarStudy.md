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

To partially cover the "ghost load" from April to September at my latitude, one or two 400W panels with a double microinverter will suffice. The cost for this setup would be around 700 to 900 €. Although this configuration may be oversized for the ghost load, it will also cover a significant portion of the steady daily load.

Return on Investment (ROI):
- Assuming an electricity cost of 0.25 € per kWh, and a conservative production estimate of 600 to 800 kWh (accounting for panel aging), this setup would save approximately 150 to 200 € per year. In the worst-case scenario, the break-even point would be reached within 6 years (under very pessimistic assumptions).
- Assuming an electricity cost of 0.4 € per kWh, with the same production estimate, the savings would amount to 240 to 320 € per year, resulting in a break-even point within 4 years.
- Assuming an electricity cost of 0.5 € per kWh, with the same production estimate, the savings would be approximately 300 to 400 € per year, leading to a break-even point within 3 years.

### Steady Daily Load

To cover the "steady daily load" of about 0.4 to 0.5 kW (including the ghost load), approximately three to four 400W panels with a 4-way microinverter would be necessary. This setup would cost around 1000 to 1200 €. As you can see, the return on investment is better in this case. The cost of a 4-way microinverter is lower, and including packaging and shipping, having 4 panels is more cost-effective than having 2.

Additionally, despite being oversized for the steady load, this configuration would partially offset peaks during lunchtime when high-power appliances such as cooking equipment, washing machines, and dishwashers are in use, resulting in a peak power production of about 1.1 to 1.3 kW.

Return on Investment (ROI):
- Assuming an electricity cost of 0.25 € per kWh, and a production estimate of 1200 to 1600 kWh, the annual savings would be around 300 to 400 €, with a break-even point within 4 years.
- Assuming an electricity cost of 0.4 € per kWh, with the same production estimate, the savings would amount to 480 to 640 € per year, resulting in a break-even point in less than 3 years.
- Assuming an electricity cost of 0.5 € per kWh, with the same production estimate, the savings would be approximately 600 to 800 € per year, leading to a break-even point within 2 years.

Considering my context, it is worth investing a bit more in additional panels and a larger 4-way microinverter.

## Battery Case

The most cost-effective battery setup is a DIY 16S (48V) lithium iron phosphate (LiFePo4) battery using 3.2V cells with a capacity of 280 to 300A, along with a 100 to 200A/BMS (Battery Management System). Building this battery will cost less than 3000 € (at the time of writing). Using smaller cells is not recommended considering the balance between capacity and price.


### Factors Affecting Battery Aging
Battery aging occurs due to several factors, including temperature resulting from loads and the environment, the number of charging cycles, and the extent of capacity utilized between charges. To prolong battery life, it is advisable to store them in a room with a consistent temperature throughout the year, such as a basement. Additionally, using larger battery capacities makes sense if you aim to extend their lifespan. For instance, a battery discharged to more than 50% capacity will endure 2 to 3 times more charging cycles compared to a battery discharged to 80% capacity. Certainly, the cost of the battery remains the most significant deciding factor in any off-grid or hybrid installation. However, in the long run, it proves to be a sensible investment.

### Offgrid case

Meteo is a problem, you can have several days without any sun according to your place, you need to take in account this case to avoid having a blackout.


## Orientation/Placement

I took nearly a full year to detail the various shadow patterns, including those caused by the hill, trees, and surrounding buildings near my place. It may sound a bit crazy, but I am interested in covering all the potential places where I can put panels and understanding all the associated drawbacks and advantages.

Just putting panels on the roof of the house does not make sense to me from a cost, maintenance, and risk perspective. Yes, your panels can develop a short-circuit due to aging (even super-branded name), create sparks, and then burn your roof.

When you put your panel on your roof, there is only one orientation possible. If you put your panels in the garden, it is possible to have one or more than one orientations, which makes it possible to start the production earlier with an array of panels oriented more to the East and/or to make it run later with an additional panel array more oriented to the West. By spreading out the production, you will cover more of your electricity needs during the day, which is something important if you run with no battery or small batteries.

For instance, during the summer, I know the sun kicks in the morning on my terrace, and shadows arrive around 2pm to 3pm due to a building. Similarly, the sun starts to kick in at the back of the garden around 10 am due to trees, and shadows come around 7pm to 8pm. This means I can put a first panel array on the terrace facing the East with a very high slope and in the back of the garden facing South-West, allowing me to produce from 8 am to 8 pm during the summer with a large peak of power from 10 am to 2 pm.



## PV Arrays Study

This study explores various possibilities for PV arrays in different locations on the property.
On my latitude the optimal slope is about 35 to 36 degrees and the optimal azimuth about 0 to -1 degree.
This part I go in the details of the evaluation.


### Panels Configurations

Let see a few panels, all prices are including VAT.
|Panel W| Number |Unit Cost (€) | Link | Total Cost (€) | Total W |
|-------|--------|--------------|------|----------------|---------|
| 415W  | 8      | 119          | https://www.chocdiscount.com/panneaux-solaires/19175-panneau-solaire-ja-solar-415w-jam54s30-415mr-monocristallin-black-frame.html | 952 | 3320 |
| 415W  | 10     | 119          | https://www.chocdiscount.com/panneaux-solaires/19175-panneau-solaire-ja-solar-415w-jam54s30-415mr-monocristallin-black-frame.html | 1190 | 4150 |
| 545   | 8      | 143.99| https://autosolar.es/panel-solar-24-voltios/panel-solar-545w-ja-solar-mono-perc | 1151.92 | 4360 |
| 545   | 10     | 143.99| https://autosolar.es/panel-solar-24-voltios/panel-solar-545w-ja-solar-mono-perc | 1439.90 | 5450 |
| 385   | 10     |  99.0 | https://www.chocdiscount.com/panneaux-solaires/25763-panneau-solaire-amerisolar-385w-as-6m120-hc-demi-cellules-black.html | 990 | 3850 |
| 385   | 15     |  99.0 |   https://www.chocdiscount.com/panneaux-solaires/25763-panneau-solaire-amerisolar-385w-as-6m120-hc-demi-cellules-black.html | 1485 | 5775  |
 


### Inverter Configuration

For a single 4KW to 5KW per phase setup, the [Victron Multiplus II/48/5000](https://www.victronenergy.com/inverters/48v-5000va) inverter is chosen for its versatility and reasonable standby power usage, providing the best value for the investment.
It cost about 1500 to 1900 € (including VAT).

For small load around 200 to 2 KW, there are microinverters in one, two, four and even six ways. This is a kind of new, so I am not sure about the reliability of such items. There are also small inverters from 800 to 2.5 KW, but the price is relatively high most of the time, except one with 2K that is also detailed.

### PV MPPT Controller Configurations

There are two options for the PV MPPT Controller:

1. The cost-effective [SNRE 250V/70A](https://www.srnesolar.com/product/%E2%80%8Bmppt-solar-regulator-solar-charge-controller-mc48v60-70a) (around €350) and/or [250/85A](https://www.srnesolar.com/product/%e2%80%8bmppt-solar-charge-controller-mc48v85-100a) (around €485) for 5S/2P in 550W peak.
2. The more expensive [Victron 250V/70A](https://www.victronenergy.com/solar-charge-controllers/smartsolar-mppt-ve.can?_ga=2.250982854.1958924882.1691273838-1387248659.1691273838) and/or [250/85A](https://www.victronenergy.com/solar-charge-controllers/smartsolar-mppt-ve.can?_ga=2.250982854.1958924882.1691273838-1387248659.1691273838).

The dimensioning calculations for both options are provided based on the battery voltage and used for computation. Considering the price difference, it makes sense to opt for the SNRE 70A model to match the 4KW panel capacity. The "communication issue" with the SNRE MPPT Controller to the Victron can be resolved using available software solutions to retrieve data.

### Battery Configurations

DIY is the way to go: let say 3000 € for 13/14 kWh @ 48V so about 280 Ah to 300 Ah of capacity with a 150 A BMS with Active Balancing + all needed stuff around the battery to make it safe.
The battery is the most costly part of the installation.


### Terrase East Wall

A small array ranging from 800W to 2KW, consisting of 2 to 6 panels with power outputs between 400W to 550W each, is proposed for the Terrase East Wall. The primary objective is to harness morning to noon sunlight efficiently to cover power usage for low-demand devices and mitigate power peaks. However, despite its simplicity, this option might not provide the most favorable return on investment. Additionally, the presence of a hill may impact the system's early morning startup.

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

#### August 2023 Price Analysis


Upon revisiting this section, I've identified significant cost-saving opportunities. A new supplier offering budget-friendly PV panels has allowed for substantial reductions in expenses.

**2 Panels Configuration:**

- Hoymiles HMS-800 Micro Inverter: 231.93€ + EndKappe 6.90 € + Cable 69.90 € + 50€ Transport [Source](https://www.offgridtec.com/hoymiles-hms-800-2t-microinverter-modulwechselrichter.html): 358.73 €
- 2 * PV Panel 385W: 2 * 99€ [Source](https://www.chocdiscount.com/panneaux-solaires/25763-panneau-solaire-amerisolar-385w-as-6m120-hc-demi-cellules-black.html) + 128 € Transport: 326 €
- Total Price: 684.73 € 
   - Kit with the same inverter: [Link](https://www.offgridtec.com/offgridtec-balkonkraftwerk-solardirect-luxen-wifi-900w-hm-800.html) (800 € without transport)

**4 Panels Configuration:**

- Hoymiles HM-1500 Microinverter: 278.86 + EndKappe 6.90 + Cable 69.90 € + 4 * 11.19 € MC4 2m + 50€ Transport [Source](https://www.offgridtec.com/hoymiles-hm-1500-microinverter-modulwechselrichter.html): 450,42 €
- 4 * PV Panel 385W: 4 * 99€ + 128 € including Transport [Source](https://www.chocdiscount.com/panneaux-solaires/25763-panneau-solaire-amerisolar-385w-as-6m120-hc-demi-cellules-black.html): 524 € 
- Total Price: 974.42 €
   - Kit with the same inverter: [Link](https://www.offgridtec.com/offgridtec-balkonkraftwerk-1700w-hm-1500-dtu-wlite-trina-vertex-s-425-mini-pv-solaranlage.html) (1130.38 € without transport)

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



As you can see, attention to detail matters. If transportation can be sourced from the same place, additional savings can be achieved.
The 4-panel configuration, featuring the most economical PV panels and a 1.5KW microinverter, significantly enhances ROI. In fact, the improvement is nearly an order of magnitude compared to the previous setup.


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


| Cfg | Panels  | Inverter                      | MPPT Controller         | Cost without Battery (€) *      | €/W       |
|-----|---------|-------------------------------|-------------------------|---------------------------------|-----------|
| 1   |  3850   |  Victron Multiplus II/48/5000 | SNRE 250/70A            | 990+1500+350 + 700 = 3540       | 0.9194    |
| 2   |  5450   |  Victron Multiplus II/48/5000 | SNRE 250/85A            | 1439.90+1500+485 + 700 = 4124.9 | 0.7568    |
| 3   |  4150   |  Victron Multiplus II/48/5000 | SNRE 250/70A            | 1190+1500+350 + 700 = 3740      | 0.9012    |
| 4   |  5450   |  Victron Multiplus II/48/5000 | SNRE 250/70A            | 1439.90+1500+350 + 700 = 3989.9 | 0.7320    |
| 5   |  4360   |  Victron Multiplus II/48/5000 | SNRE 250/70A            | 1151.92+1500+350 + 700 = 3701.91| 0.8490    |
| 6   |  5775   |  Victron Multiplus II/48/5000 | SNRE 250/85A            | 1485+1500+485 + 700 = 4170 | 0.7220    |


* Added 700 € of fixed cost for cables, switch, fuses, electric panel and protections...


Now let's explore the figures with the addition of the DIY battery:

| Configuration | Cost with Battery (€) | €/W    |
|---------------|-----------------------|--------|
| 1             | 6540                  | 1.6987 |
| 2             | 7124.9                | 1.3073 |
| 3             | 6740                  | 1.6240 |
| 4             | 6989.9                | 1.2825 |
| 5             | 6701.91               | 1.5371 |
| 6             | 7170                  | 1.2415 |

Observing the results, it becomes evident that having a slightly larger panel configuration is more beneficial in the long run. The cost difference of around 10% between the low-cost 3.85 KW configuration and the 5.45 KW configuration justifies opting for the latter. The decision mainly hinges on the feasibility of accommodating larger panels within your setup. Additionally, a slight oversizing of panels can enhance performance, even accounting for some 'clipping'; this leads to increased energy production during periods of lower sunlight.

Configuration 4 appears to be on the edge, where the MPPT Controller is undersized for cost reduction (57 * 70 = 3990 W). The panel array is oversized at 136.5%, possibly more than necessary. Considering configuration 2, with 57 * 85 = 4845 W, might be a more balanced choice.

Configuration 6 offers an interesting alternative—incorporating 5 more panels leads to a slight improvement in ROI.

When evaluating the power-to-surface ratio, configuration 2 stands out by utilizing less surface area. This aspect is advantageous if you intend to add more panels or minimize the land's impact.

It's worth noting that while fixed costs for the shed need to be factored in, they are unlikely to alter the observed trends, as we've already discussed.



Let's explore the mean daily production for Configuration 2, with a cap of 4.845 KW on the MPPT controller. It's important to highlight that the actual production should ideally surpass the observed figures. While the yearly production is estimated at 5013 kWh, a 5.45 KW PV Array generates a higher 5639 kWh annually.

| Month | Daily Mean - High and Upper bound (kWh) |
|-------|------------------------|
|  Jan  |   4.22 - 4.93          |
|  Feb  |   7.80 - 8.78          |
|  Mar  |  13.70 - 15.29         |
|  Apr  |  19.73 - 22.2          |
|  May  |  20.61 - 23.19         |
|  Jun  |  22.20 - 24.96         |
|  Jul  |  20.54 - 24.41         |
|  Aug  |  19.06 - 21.45         |
|  Sep  |  16.43 - 18.46         |
|  Oct  |   9.90 - 11.5          |
|  Nov  |   5.13 - 5.61          |
|  Dec  |   3.80 - 4.29          |

On average, the daily mean ranges between 12.3 kWh and 13.7 kWh. It's important to acknowledge that while this single array theoretically provides adequate power from March to September, practical factors suggest a more realistic timeframe from April to mid-September. Unaccounted shadows can lead to diminished production during this period.


### Middle Garden

The Middle Garden setup shares similarities with the Power Shed configuration. It can feature either one or two rows of panels, adhering to the same specifications. The orientation and performance characteristics remain consistent, with the added benefit of an earlier startup when compared to the Power Shed setup. Despite the potential advantages of bifacial panels, they are excluded from consideration due to their elevated cost and minimal power gain, which fails to justify the investment.

In instances where the inverter possesses sufficient capacity, a viable strategy involves placing only panels, the MPPT controller, and the battery. This approach leads to cost savings and reduces nighttime power consumption associated with an additional inverter. However, this method might lead to a slightly amplified overproduction during the summer months.

### House Roof

Mounting panels on the house roof is not the preferred choice, primarily due to the high associated costs and the impracticality of undertaking the installation independently. In Luxembourg, the cost factor acts as a significant deterrent, making it more financially viable to opt for a DIY three-phase 15KW system. This alternative stands out as a preferable choice, even considering potential government assistance.


  
 
