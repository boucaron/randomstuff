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
Bi-facial can be interesting if you are outdoor, bi-facial means there is a front and a back face, the back face is covered with a transparent glass. It can produce additional electricity, for instance the light reflect on the  grass in a garden which is captured by the back face.
You can also have partially transparent PV that can be useful for agriculture or pergola.
The bang for the buck for today PV around 400 to 500W (1700 mm to 2300 mm length, 770 mm large and 35 mm height) costing about 150 to 250 Euros (including VAT).



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
String-inverters  inverters having one, two or more MPP trackers where you attach a 'string' of PV panels connected together in serie. Most of the time they range from 3 KW to 30 KW.
Regarding pricing, it is not so obvious for some brands it is cheaper to put 2 times 5 KW inverter than to buy a single 10 KW.

### Hybrid inverters
Hybrid-inverter means this is an inverter coupled to a battery. The PV array can charge the battery and/or provide power to the load through the inverter. It is a versatile device, it can be connected to the grid, a generator ...etc... There are hybrid inverters for 12/24 and mostly 48V batteries (Victron for instance), there are some inverters for high voltage batteries (Fronius/Huawei for instance)

Offgrid inverter it is an hybrid inverter not connected to the grid.

## Batteries

Batteries are having various voltage and chemistry.
They are either build as low voltage from 12, 24 to 48V, or from high voltage about 400V and higher.
You can either buy commercial batteries with integrated BMS and/or integrated inverter, you can also build one yourself from cells, separate BMS, separate inverter.
A Tesla powerwall costs about 14 K€ for 13.5 kWh with a 5KW inverter.
A DIY battery about 13 kWh with a 150 A BMS costs about 2.5 to 3 K€, if you put a top-tiers hybrid inverter of 5KW (Victron Multiplus) 2K€, so about 5.5 K€ max.

## Battery Management System (BMS)

BMS is used to charge/discharge a battery and have various protection according to the kind of battery (under-voltage, over-voltage, current protection, temperature protection, cell-balancing ...etc...)

# Solar Estimating Tools

There are different tools available.
I found the most useful and complete is the free tool provided by the EC: https://re.jrc.ec.europa.eu/pvg_tools/en/ (PVGIS)
Basically you set the location, the orientation (slope, azimuth), the size of your PV array and it provides you an estimation of the production by month/year.
If you the tool handy to see how sensitive is the production with respect to the slope which is surprisingly not so critical.
What I found more interesting is the 'Daily Data' where you can really dig in when your production will run on the whole year and the hourly irradiance.

But do not forget this is just an estimation, it cannot take in account shadows due to trees, to buildings, to mountains ...etc...

## It is about details
Personally, based on where I plan to put my PVs, I spent some time to see where and when the sun comes and goes along the year.
I know for instance I can put some PV next to a wall (Azimuth -30 deg., Slope 90 deg.) and that from April to September, I will have some production from 7/8h to 14/15h but it will have a small irradiance about 200 to 600 W/m². So a 425W panel under 1000 W/m² irradiance will produce as much as 75 W at 200 W/m² irradiance to 240 W at 600 W/m². It is really important to know this details to have a realistic idea of the real production in your location.
Also it gives you an hint if you can put more panels on the inverter which is a costly equipment, the inverter can produce more early and 'clip' the excess production.



# Dimensionning is tricky

Solar panels, inverters, batteries, bms are coming as components with various 'size', but those sizes are discrete.
For instance you may need a 20 kWh battery but you cannot build one, you will be able to build two 13 kWh battery for instance and couple both together.
This is the same for inverters, you may need a 8KW inverter but you can either put a 10 KW, or 2 of 5 KW or 3 of 3 KW. 

## Storage is mandatory

Why so ?
Production is not during the same time as usage.
Electric companies are not buying back at an interesting price. Also you are going to sell for cheap during the day whay you need during the night. It does not make any sense.


## Basic idea

- 5 KW PV Array + 5 KW Inverter: about 5100 kWh in my place and specified orientation.
- Being pessimistic, I can remove November, December, January, Februrary: about 641 kWh less, so 4459 kWh, it is more or less my yearly power usage.
- I did not account for aging of the PV array on 25 years: -15% so 3790 kWh

But there are large peaks above 8 KW for the shower direct heaters: a single 5KW inverter cannot cope with such load.
Also, this inverter is a single phase and I have three phases.

With a big spoon let say it will cost 8 to 10 K€ with a 13.5 kWh DIY battery
During summer the PV array will generates about 18 to 22 kWh daily.
It means there is overproduction and the battery will be filled quickly.
Habits need to be changed to use the power of the PV array (April to August) for the washing machine and the dish washer.

## More batteries
The daily average power usage is about 12 kWh, the life span of the LiPo battery being filled fully and empty is pretty bad for its life time. An additional battery should be added, the current will be spread out on both when charging and discharging, it means less heat. Let say a single battery will be not empty less than 20%, two batteries will have more than 50% of their capacity after each day, slightly improving the life of both batteries. Of course, it is a 3 K€ additional increase from 11 to 13 K€ on the system cost, but for a 3 times life improvement on the batteries which is critical in my point of view. Actually due to the reduce heat/stress on the current used, it will also reduce aging on the capacity of the batteries.
According to https://batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries
- 80% DoD equals 900 cycles
- 40% DoD equals 3000 cycles 





# Improving habits

## Shower power saving
Shower is about 8 to 18 KW:
- 15 minutes is about 2 kWh to 4.5 kWh.
- 10 minutes is about 1.33 kWh to 3 kWh.
- 5 minutes is about 0.66 kWh to 1.5 kWh.
Speed matters.

Let say 2 showers a day during a year:
- At 3.3 kWh each: 2409 kWh
- At 2.2 kWh each: 1606 kWh
- At 1.1 kWh each: 803 kWh
5 minutes saved is about 803 kWh saved on the yearly bill.

## Washing machine/Dish washer

If a large enough PV array is installed and the battery is a on the short side for the storage, you will have overproduction during summer. The washing machine or the dish washer should be running in the middle of the morning or just after lunch using relatively short cycles to take full advantage of the full sun  still being able to fill the battery for the evening and night usage.


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

  

## Orientation/Placement

I took nearly a full-year to details where are the various shadow patterns including the hill, the trees and the buildings surrounding my place.
I know it sounds a bit crazy, but I am interested in covering all the potential places where I can put panels and to understand all the associated drawbacks and advantages.

Just putting panels on the roof of the house does not make sense to me from a cost, from a maintenance and also from a risk perspective.
Yes, your panels can develop a short-circuit due to aging (even super-branded name), create sparks and then burn your roof.

When you put your panel on your roof there is only one orientation possible. If you put your panels in the garden, it is possible to have one or more than one orientations, which makes possiblee to start the production earlier with an array of panels oriented more to the East and/or to make it runs later with an additional panel array more oriented to the West. By spreading out the production you will cover more of your electricity needs during the day, which is something important if you run with no battery or small batteries.

For instance during the summer, I know the sun kicks in the morning on my terrasse and shadows arrives around 14 to 15h due to a building. Similary the sun starts to kick in at back of the garden around 10h due to trees and shadows comes around 19 to 20h. Which means I can put a first panel array on the terrasse facing the East with a very high slope, and in the back of the garden facing South-West, allowing me to produce from 8 to 20 during the summer with a large peak of power from 10 to 14h.








  
 
