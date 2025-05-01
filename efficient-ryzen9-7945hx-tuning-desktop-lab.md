# AMD Laptop Ryzen 9 Stuff

This is a tiny powerful tower that I built in March 2025.  
**Document date:** 27/04/2025

---

## Specs

- **Motherboard:** MinisForum AMD Ryzen 9 7945HX BD795M  
- **Memory:** Corsair CMSX64GX5M2A5200C44 (2 × 32 GB)  
- **SSD:** Lexar SSD NQ790 2 TB  
- **Watercooling:** Cooler Master MasterLiquid 360L Core ARGB  
- **Power Supply:** Tecnoware ATX 400W  
- **Case:** ASUS Prime AP201 Tempered Glass MicroATX Case (White)

---

## Issues

- **96 GB memory compatibility issue** with Crucial CL46 - CT2K48G56C46S5. I had to downgrade to 64 GB because those were not working.
- **Watercooling compatibility**: I returned the ARCTIC Liquid Freezer III Pro 360 due to mounting issues. Switched to Cooler Master kit that came with a backplate.
- **Cooler Master watercooling support screw issue**: The screws provided had excess tolerance; I had to file down the step to ensure proper clamping and alignment with the mounting holes.
- **Dead motherboard**: After just over a week of use, the first motherboard failed unexpectedly. No burn smell or visible damage. It was returned and replaced after significant back and forth.

---

## Testing

This testing was done on the second motherboard.

This isn't a short benchmark run. I run **real workloads** — specifically, **CFD simulations** — for several hours at a time. These tasks are memory-intensive and heavily multithreaded.

I use **HWinfo** for monitoring, which provides deep sensor visibility.

### First Day Results

- **Memory cooling is inadequate**: In a 20-hour session, the bottom DIMM reached **95.8°C** (!), while the upper one hit **79.8°C**. Additional cooling is clearly needed.
- **CPU thermals**: Despite the large AIO cooler, CPU temps reached **97.1°C**, while the plate itself wasn't excessively hot, implying sensor-based control quirks or hot spots.
- **iGPU max temp**: Just **44.9°C**, showing how little it's used.
- **CPU power draw**: ~100W according to HWinfo.
- **SSD top temp**: 58°C — and that’s with virtually no workload on the SSD.
- PassMark Cpu Benchmark in the 59000 mark, the massive watercooling makes it run above the average which is about high 54000.

---

## Tuning

After the first day's high temps, I found out this short article written by Brandon Lee [https://www.virtualizationhowto.com/2025/03/core-performance-boost-setting-speed-vs-power-consumption-in-home-lab/](https://www.virtualizationhowto.com/2025/03/core-performance-boost-setting-speed-vs-power-consumption-in-home-lab/)
So I went into BIOS and perform the following modifications:

- **Disabled Core Performance Boost**
- **Enabled Global C-state Control**

This step was a bit nerve-wracking — BIOS on this board is slow to apply changes, making reboots tense.

### Immediate Results

- Peak CPU power: **~46W**
- Peak CPU temp: **~45°C**
- Noise level: Significantly lower. Mostly just the water pump is audible.

Frankly, **this should be the out-of-the-box experience.**  
The system is now efficient, silent, and stress-free.
However it is slightly slower: PassMark Cpu Benchmark is down to the big 30000 mark instead of the initial 59000 mark.

---

# Efficient Performance Tuning for Ryzen 9 7945HX: A Balanced Approach

## Why Go Further?

While the above tweaks helped, it became clear that **even more control was needed** to balance thermal behavior, long-term durability, and performance.

The stock 7945HX profile is designed for maximum benchmark wins — not longevity or quiet operation. For anyone using this chip in:

- Compact desktop builds,
- Embedded workstations,
- Lab environments,
- Developer systems,

...you’ll benefit greatly from **limiting aggressive boost and current draw**.

## Core Problem

Out-of-the-box, the CPU was:

- Drawing **up to 160A** (peak),
- Peaking at **90–97°C** under load,
- **Kicking fans on full** based on short-term thermal spikes,
- Causing potential **VRM stress** and even early hardware failure (as I experienced firsthand).

## My BIOS-Level Fixes
 MinisForum AMD Ryzen 9 7945HX BD795M 
- **Enable Performance Boost**
- **Go in the Overclocking Menu**
- **TDP (PPT):** 60W  
- **TDC/EDC (current limits):** 80A  
- **Thermal Throttling limit:** 55°C  


This setup keeps performance tight, while improving acoustics and extending system life.

## Benchmark Table

| Profile                     | PassMark Benchmark Score | **Requested TDP** | **Requested Current (TDC/EDC)** | **Throttling Temp Limit** | **Peak CPU Temp** | **Peak TDP** | **Peak CPU Current** | Notes                                       |
|-----------------------------|--------------------------|-------------------|---------------------------------|---------------------------|-------------------|--------------|----------------------|---------------------------------------------|
| **Stock Performance Boost** | 59,000                   | 100W              | ? / 160A                        | 97°C (default)            | 97°C              | 100W         | ~160A                | High thermal load, high fan noise, max perf |
| **No Performance Boost**    | 30,000                   | 45W               | ? / ?A                          | 97°C (default)            | 46°C              | 46W          | ~69A                 | Super quiet, low power, lower performance   |
| **Custom (60W, 55°C)**      | 51,000                   | 60W               | 80A                             | 55°C                      | 63°C              | 73.6W        | ~89A                 | Quiet, cool, ~85% performance               |
| **Custom (60W, 75°C)**      | 52,000                   | 60W               | 80A                             | 75°C                      | 83°C              | 73.6W        | ~89A                 | Not so Quiet, higher temp, noisy, ~85% perf |


---

## Fan Behavior & Hidden Issues

The **fan curve is driven by the hottest core**, not average CPU temp. Even during **single-core workloads**, if the core spikes above 75°C, the fans go full tilt. This results in:

- Annoying fan ramp-ups,
- Noisy operation even under low load,
- Unstable acoustic profile.

By applying a **lower temp cap (55°C)** and restricting amps, you can prevent these spikes — resulting in a more pleasant user experience.

---

## Performance Boost Behavior

The **Performance Boost** feature is extremely aggressive. To control it, I set a very tight throttling temperature limit. Large temperature spikes typically lead to large voltage and current spikes, which I want to avoid to help extend the system’s lifespan.
Despite the tighter thermal throttling and imposed current limits, most of the performance is retained — while placing a solid safety margin around both temperature and peak current.
It's a bit like riding a high-performance motorbike: we allow rapid acceleration for performance, but we also apply strong braking when necessary to stay in control.


## Conclusion

Modern CPUs like the Ryzen 9 7945HX are extremely powerful — but come with aggressive thermal and power behaviors that **don't fit every use case**.

If you’re using this chip in a:

- **Quiet desktop build**
- **Small workstation or lab PC**
- **Development machine with long simulation workloads**

…then tuning for **power efficiency and thermal sanity** is a must.

- You’ll still retain **85% of peak performance**, with **quieter operation**, **longer hardware lifespan**, and **fewer surprises**.
- Peak measured temperature was down from 97C to 63C (-35%).
- Peak measured current was down from 160A to 89A (-44%).
- Peak measured TDP was down from 100W to 73.6W (-26%).

Sometimes, **it’s not about pushing harder — it’s about pushing smarter.**

---

*Feel free to contact me or contribute feedback if you’re building a similar setup.*





