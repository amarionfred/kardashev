# KARDASHEV

---

## Note to the reader

This is a white paper, not a pitch. It argues a position, shows the arithmetic behind it, and states what is not yet known. It is written for people who will check the numbers: engineers, scientists, and investors who have seen enough space presentations to distrust adjectives.

Three conventions apply throughout.

**Ranges, not points.** Where a value is measured, it is cited. Where it is modelled, it is labelled. Where it is assumed, the assumption is visible. A single number without a status is a defect. Section 6 explains why this document, and this programme, move at startup speed.

**The unit is the kilogram of delivered product.** Not the tonne of regolith moved, not the watt installed, not the headline resource. A mine is a machine for converting capital and energy into a saleable kilogram. That conversion is the only thing that matters.

**Failures stay in the record.** The programme behind this paper keeps its own failed designs. One of them is described in section 5. A plan that cannot survive its own falsification is not a plan.

All numbered sections have had internal fresh-context reviews (requirement fit, citation screening, prose, and a technical pass) on 12–13 November 2026. The document as a whole has not been independently verified, peer-reviewed, or checked against hardware. It is a working document, not an offer or a solicitation. The scalar-check appendix arithmetic is published with the source at the project repository: https://github.com/amarionfred/kardashev

---

## 1. The ladder

**Civilisation climbs by converting energy into capability. The next rung is not a larger rocket. It is a first off-Earth industrial base.**

In 1964, Nikolai Kardashev proposed a scale for civilisations based on the power they can command. Type I uses the energy incident on its planet. Type II uses the output of its star. Type III uses the output of its galaxy. The scale is logarithmic; in Sagan's version, each type is ten orders of magnitude above the last. The scale therefore measures a change in kind, not degree.

The numbers depend on the convention [1][2]. Kardashev's original Type I threshold was about 4×10^12 W. Carl Sagan's logarithmic version, which is the one in common use, puts Type I at 10^16 W [1][2]. Humanity's primary energy use is about 620 EJ per year, or 2×10^13 W [3]. On Sagan's scale we are at 0.73. Reaching Type I requires roughly five hundred times the power we currently use.

Five hundred is a large number, but it is not the interesting one. The interesting one is that energy is not the only input. A civilisation that wants five hundred times the power must build five hundred times the machines, and those machines must come from somewhere. Earth's biosphere, its ore bodies, and its launch capacity are finite. At some point the mass fraction that must be lifted out of Earth's gravity well becomes the binding constraint, not the fuel.

The Moon is the first place where that constraint can be tested. It is close enough for a return trip measured in days. It has no atmosphere, so a launch from its surface does not pay the same penalty as a launch from Earth. It has no global magnetic field, so the solar wind has reached its surface for most of its history. And it has no biosphere to protect, which means industrial experiments there are not automatically environmental questions.

The destination, stated plainly, is an industrial arc that moves the Moon from a visited outpost to a worked site. The reasoning, set out in the 2017 video essay Industrializing the Moon, runs as follows. The Moon's composition is close to Earth's crust: silicon, oxygen, aluminium, iron and, in its mare basalts, titanium, plus water ice in shadowed polar craters. Shipping mass from the lunar surface to Earth orbit costs less than lifting the same mass from Earth's surface. The Moon is already, in that account's phrase, a warehouse pre-positioned next to the expansion front: raw mass and fuel for expanded space operations. Once ore handling and fuel production exist, the same feedstock and the same base can tow O'Neill-class rotating habitats into orbit instead of down into Earth's gravity well. The same account's construction ballpark is about a million person-years per habitat, with centuries to run in, starting from modest thousand-person installations [26].

That framing is the motive for the company, and it is a vision, not a schedule. This paper does not claim any of that is near. It claims that the first rung is a measured kilogram of helium-3, sold, and that everything above it is earned, one gate at a time.

The industrial case is not that the Moon is closer than Mars. It is that the mass budget compounds. Every tonne of structure, propellant, or shielding made on the Moon is a tonne not lifted from Earth. Every tonne not lifted is propellant not burned, and every kilogram of propellant not burned is mass available for something else. The Moon's vacuum also removes the cost of vacuum chambers, and its shallow gravity well makes return cheap. Those advantages are real, but they compound only once a base exists. The first industry has to pay for the base before the base can pay for anything else.

None of this makes the Moon a destination. It makes it a test. The first lunar industry will be judged on the same terms as any terrestrial one: mass in, product out, energy per kilogram, capital per kilogram, and time.

The rest of this paper is about one product, chosen because it is the best first test of that chain.

---

## 2. The reserve

**The Moon is not short of helium-3. It is short of concentration.**

Helium-3 is a light isotope of helium with one proton and two neutrons. It is primordial, produced in the first minutes after the Big Bang and in stellar interiors. Earth has very little of it: the atmosphere's helium is about one part per million helium-3, and the isotope is lost to space over geological time. The Moon has no global magnetic field and almost no atmosphere, so the solar wind, which carries helium-3 at a few hundred parts per million of its helium, has struck its surface directly for most of its history. The ions implant into the top tens of nanometres of regolith grains, and they stay there.

The result is a resource with a strange shape. The total inventory is large. Model-based estimates put roughly 6.5×10^8 kg in the upper regolith [5]. That is hundreds of thousands of tonnes of a material whose terrestrial price is measured in millions of dollars per kilogram. The estimate follows an orbital abundance model rather than any single crop of samples; it is quoted as a model, not a measurement, and it is theirs, not re-derived here.

The concentration is the problem. Measured samples span 2.4 to 26 parts per billion by mass. Apollo 11 sample 10084, the bulk sample collected by Armstrong, averaged 11.8 ppb across analyses, with a range of 9.22 to 17.9 ppb [6][7]. Two Apollo 17 samples in the programme's design basis measure 4.66 and 11.21 ppb [8]. The highest values correlate with ilmenite and titanium-rich mare basalts, because ilmenite retains implanted helium better than other minerals [9][10]. That correlation is why the candidate sites are a short list of titanium-rich maria rather than the whole Moon.

| Quantity | Value | Status |
|---|---:|---|
| He-3 grade, measured samples | 2.4–26 ppb | Measured, sample-specific |
| Apollo 11 sample 10084 | 11.8 ppb (9.22–17.9) | Measured, sample-specific |
| Apollo 17 72501,27 | 4.66 ppb | Measured, sample-specific |
| Apollo 17 70011,18 | 11.21 ppb | Measured, sample-specific |
| He-3/He-4 ratio, lunar | 2.7–2.9×10^-4 | Derived from assays [6][7] |
| He-3/He-4 ratio, terrestrial | 1.4×10^-6 | Reference value |
| Global inventory, upper regolith | ~6.5×10^8 kg | Model estimate |

Two conclusions follow, and they pull in opposite directions.

The first is that the resource is real. The measurements are not speculative; they come from returned samples, and the mechanism is understood. A mine would not be chasing a phantom.

The second is that a resource map is not a mine. The global inventory is a model. The grade at any specific site is an interpolation between sample points and orbital remote sensing, not a measured assay. The difference between 5 and 15 ppb is a factor of three in the size of every machine downstream. So the first payload in the sequence is a prospecting instrument, not an excavator.

The programme's design basis treats the grade as an unknown with a range, not a fact. That is the correct status. Anyone who tells you the grade of their mine before they have measured it is selling something other than a mine.

---

## 3. The arithmetic

**Heat is cheap on the Moon. Mass is not. The machine is a heat exchanger with a mining problem attached.**

The extraction chain is simple to state and hard to execute. Regolith is excavated, sorted, heated, and the evolved gas is captured, cleaned, and separated into helium-3 and helium-4. Each step has a loss. The product is the product of all of them.

```
regolith → excavate → sort → heat → release → capture → clean → separate → store → deliver
             ↑          ↑       ↑        ↑         ↑        ↑         ↑
           losses     losses  losses   losses    losses   losses    losses
```

The first number is the feed ratio. At 10 ppb and 100% recovery, one kilogram of helium-3 is implanted across 100,000 tonnes of regolith. At 50% overall recovery, it is 200,000 tonnes. At 5 ppb, it is 400,000 tonnes. The ratio is the mine.

The second number is the heat. The programme has checked a published heat-capacity fit for the FJS-1 lunar soil simulant over its measured range, 313 to 570 K. The integral is 226,744 J per kilogram, confirmed by two numerical routes to a relative difference of 3×10^-9; both routes integrate the same published fit, so this checks the arithmetic, not the fit itself [11][12]. Heating to 800 °C, where published release experiments report about 95% of implanted helium released [7], roughly triples that figure; the extension above 570 K is an assumption, and it is labelled as one.

Put the two together. At 10 ppb, 50% overall recovery, and roughly 0.5 to 0.7 MJ per kilogram of feed, one gram of helium-3 costs 100 to 140 GJ of heat. That is 28 to 39 MWh. With 85% recuperation, a figure claimed by the published Mark-III extraction concept in Olson 2021 [7], the net figure falls to 4 to 6 MWh per gram.

| Case | Feed per gram | Heat per gram | Net heat at 85% recuperation |
|---|---:|---:|---:|
| 10 ppb, 50% recovery | 200 t | 100–140 GJ | 4–6 MWh |
| 10 ppb, 30% recovery | 333 t | 165–235 GJ | 7–10 MWh |
| 5 ppb, 50% recovery | 400 t | 200–280 GJ | 8–12 MWh |

The energy is not the obstacle. At a generous $100 per MWh, 30 MWh is $3,000 per gram, or 15% of a $20,000 per gram sale price. With recuperation it is about 2%. The thermodynamics are affordable. The capital is not yet.

The third number is the night. The lunar day is 29.5 Earth days, so the night is 14.75 days long. Equatorial surface temperatures reach about 400 K at noon and fall below 100 K before dawn, so the thermal cycle is not a small perturbation [24]. A plant that runs on solar power must either stop, store, or find a site with near-continuous illumination. Stopping halves the calendar output. Storing is worse: a 1.4 MW plant needs about 500 MWh to run through the night, which at 250 Wh/kg is roughly 2,000 tonnes of batteries. That is an enormous mass item, plausibly exceeding the plant itself (indicative; no plant exists to compare against). A thermal store is lighter for heat than a battery is for electricity, but it is still a mass item, and it has its own losses.

The fourth number is the separation. Lunar helium is isotopically enriched relative to terrestrial helium by a factor of about 200, because it comes from the Sun rather than from radioactive decay in the Earth. That is a real advantage, not a solution. Helium-3 boils at 3.19 K and helium-4 at 4.22 K. Separating them at 99% purity requires a cryogenic distillation column or a quantum-sieving process (preferential low-temperature adsorption of the lighter isotope) operating near 2 K, with the refrigeration penalty that implies. The programme's design basis carries the separation energy as an unknown, not a number, because no public measurement supports a defensible value for a lunar plant.

The fifth number is heat rejection. A plant that consumes megawatts must reject megawatts. At 300 K, a black body radiates about 460 W per square metre; with emissivity 0.9 and two sides, roughly 800 W per square metre. One megawatt therefore needs about 1,200 to 2,200 square metres of radiator, before dust and view-factor penalties. Heat rejection is not a detail. It is a structure.

The arithmetic does not say the mine is impossible. It says where the difficulty lives: in the mass of the machine, the length of the night, and the fraction of the gas that survives the chain. Those are engineering problems, and they are the ones the programme is built to solve.

---

## 4. The machine

**A mine that can survive the night is a different machine from a mine that works for fourteen days.**

The programme has carried four extraction routes as explicit alternatives, not as a favourite and three straw men.

1. **Thermal reference.** Heat selected feed and capture the evolved gas, with heat recovery from the processed solids to the incoming feed. This is the most transparent published architecture, and the baseline against which the others are judged.
2. **Warm preheat.** Recover heat from the gas and the solids at a lower temperature, reducing the radiative loss that dominates at high temperature. The trade is residence time and release fraction.
3. **Mechanical release.** Agitate or mill the regolith to release gas without heating the bulk. Published simulant experiments removed 70% and 96% of implanted helium-4 at two small flow rates without heating above room temperature [7]. The experiment used helium-4 in a simulant, not helium-3 in lunar regolith, and it measured retained gas, not captured product. It is a lead, not a result.
4. **Hybrid.** Capture the early mechanical release, then heat the residual feed. This is a candidate, not a claimed improvement. It adds equipment mass and failure points, and the programme treats those as costs to be weighed, not details to be waved away.

The architecture that follows from the arithmetic is modular. A single 100 tonne per hour plant produces about 0.5 grams per hour at 10 ppb and 50% recovery, or 4.4 kilograms per year if it runs continuously. A 10 tonne per hour unit produces a tenth of that. The smaller unit is easier to launch, easier to test, easier to replace, and easier to sell into a market measured in kilograms. A fleet of small units also fails gracefully: one jammed excavator does not stop the mine.

This is not a claim that small is always better. It is a claim that the first unit should be expendable, and that the fleet architecture should be chosen after the first unit has measured the things a model cannot.

The programme has built a parameterised design basis for this machine [13]. It contains 157 traced quantities (F1 design-basis records), each labelled as measured, sourced, assumed, or unknown, and each tied to a source or an explicit assumption. It has two candidate architecture allocations with common interfaces, CAD/STEP assemblies whose pinned snapshots hash-verify byte-identical (716 of 716) at file scope, and a finite-cycle resource ledger that accounts for power, heat, storage, service, and time. Geometry-to-parameter binding remains unproven and is deferred to F3. It does not have a demonstrated machine. The distinction matters, and the paper keeps it.

What the design basis has already produced is a list of the things that break. The 256 K cold-feed case falls outside the measured heat-capacity range, so the low-temperature relation is an open gap, not an extrapolation. A stowed equipment recess leaves 12 unwaived penetrations at the current envelope. A funded design closure for one part of the extraction chain was falsified by a deterministic simulation at 0.263 s of model time (see section 5). None of these is a surprise in a first design. All of them are recorded, owned, and carried into the next phase rather than smoothed out of the presentation.

That is the machine's real state: an architecture with a traceable basis, a set of named defects, and no hardware. A white paper that claimed more would be overclaiming.

---

## 5. The ledger

**The programme keeps the failures. The failures are the reason to trust the process.**

A technical claim has four possible states. It can be measured, modelled, assumed, or unknown. Space-resource presentations often collapse the last three into the first. This paper does not.

| Claim | Status | What would settle it |
|---|---|---|
| He-3 grade at a candidate site | Unknown; sample range 2.4–26 ppb | A prospecting payload with a calibrated gas assay |
| Release fraction at 500–800 °C | Measured on Apollo sample 10084; not reproduced | Bench test on lunar-derived or well-characterised simulant |
| Capture efficiency | Unknown | Bench test with a sealed gas train and mass balance |
| Heat recovery | Modelled at 85% in a published concept | Measured recuperation on a sub-scale exchanger |
| Separation energy at 99% purity | Unknown | Cryogenic column test with measured power |
| Night survival | Modelled | Thermal-vacuum test of the storage and radiator |
| Dust wear on seals and bearings | Unknown | Long-duration simulant test |
| Robotic service | Requirement, not design | Executable service procedure with a robot |
| Cost per kilogram | Unknown; published estimates $20–100M/kg [4] | A costed pilot with real supplier quotes |

The method behind the table is deliberately boring. One work item per defect. A written question, a resource budget, a checkpoint, and a stop condition. Three attempts per defect, no silent renaming, no widening of tolerances to make a run pass. An independent reviewer who does not edit the producer's files. A status record that separates a passed job from an accepted result.

The programme's own failure is the best evidence that the method is real. A funded design closure for part of the extraction chain was simulated deterministically and failed at 0.263 s of model time. The contract that defined it was not rewritten to save it. The failure was recorded with its time, its inputs, and its reviewer, and the design was carried forward as an open defect into the next phase. A reader can disagree with the design. A reader cannot say the failure was hidden.

This is slower than a pitch deck. It is also the only way to know which numbers are real.

---

## 6. The edge

**AI is why this programme's calendar closes. Here is the mechanism, not the motto.**

The incumbent way to buy certainty in aerospace is headcount: specialists to read the literature, CAD operators to keep assemblies in sync with a parameter model, simulation teams to falsify designs, reviewers to catch what the simulation missed, writers to describe it. The failure modes of that method are well known: the coordination cost scales with the team, and the loop from idea to falsification takes months. The programme behind this paper runs the same workflows with AI in the loop. The loop is short, and its cost does not scale with headcount.

Every workflow in this programme runs with AI in it today:

| Workflow | What AI does | Evidence |
|---|---|---|
| Research | Reads the primary literature, keeps it cited and dated | The bibliography of this paper, every number labelled measured, sourced, modelled, or unknown |
| Design basis | Traces quantities through a parameterised model, labels each | 157 traced quantities, F1-BASIS-C02 |
| Architecture | Generates and compares candidate allocations; pinned CAD/STEP snapshots hash-verified | 716 of 716, file scope (F2) [13] |
| Verification | Deterministic simulation falsifies designs before hardware exists | A funded thermal closure failed at 0.263 s of model time |
| Review | Fresh-context AI reviewers read the work, edit nothing, file findings | This paper's technical review, 12 November 2026, including a 1,000× break-even error it caught before any human read the draft |
| This document | Researched, drafted, reviewed and arithmetically checked in days | Version 1.0, 12 November 2026 |

The benefit is multiplicative, not additive. Each gate is cheaper than the gate before it because the machinery — the traceability, the reconciliation, the simulation, the review — is built once and reused. A simulated falsification costs a fraction of a bench test. A bench test costs a fraction of a flight. The same programme, run the incumbent way, prices the loop in person-months per gate; run this way, the loop closes in days.

The human hours go to judgment: what to build, what to stop, what to ask next. None of this removes physics. Dust does not care about the token budget. A simulation that runs is not a machine that works, and an AI review is a label, not a proof: the 157 quantities are honest because each is tied to a source or an explicit assumption, not because a model produced them. Where this paper says unknown, it means nothing has been measured. The AI edge removes the bottleneck between those measurements, and calendar time lives in that bottleneck.

That is the edge. It compounds, it is checkable, and it is how this machine gets measured on a startup's budget.

---

## 7. The buyer

**The price of helium-3 is high because the supply is small, not because the demand is large.**

This is the most important economic fact in the paper, and it cuts against the usual lunar mining story.

Global production of helium-3 is under four kilograms a year [4]. The United States produces about one kilogram a year [14], almost all of it as a by-product of tritium decay at the Savannah River Site. United States federal demand, after a decade of substitution and recycling, is below 6,000 litres a year, about 0.8 kilograms [14][15]. The price is quoted around $20 million per kilogram, with small-lot quotes ranging from $15,000 to $19,000 per gram [4][16].

A plant producing forty kilograms a year would not find forty times the customers. It would find a lower price. The demand curve, not the geology, sets the ceiling on the first mine. That is why the sequence in section 8 starts with a prospecting payload and a bench unit, not a hundred-tonne excavator.

The demand has three parts, and they are not equally durable.

**Quantum cooling.** Dilution refrigerators use a helium-3/helium-4 mixture to reach millikelvin temperatures. Superconducting qubits need that cooling. Quantum computing is the fastest-growing source of demand, and it is where the first large commercial contracts for lunar helium-3 have appeared [4]. It is also the segment most exposed to substitution: researchers are actively engineering around helium-3 because the supply is scarce and the price is high.

**Neutron detection.** Helium-3 was the standard fill gas for neutron detectors used in port and border security. Demand spiked after 2001, drained the United States stockpile, and forced rationing [15]. The shortage accelerated alternatives: lithium-6 and boron-10 detectors now meet the same requirement without helium-3 [17]. This segment is unlikely to grow.

**Fusion.** The deuterium-helium-3 reaction is aneutronic in its main branch, which means less wall damage and the possibility of direct energy conversion. It also ignites at roughly 700 million degrees Celsius, about four times the deuterium-tritium temperature, and no machine is close to it [18]. Only a few fusion developers plan to buy helium-3 on the open market; most plan to breed their own or use deuterium-tritium. Fusion is an option on the future, not a customer today.

The honest summary is that helium-3 is a niche isotope market with a strategic option on fusion. The niche is real: the price is real, the contracts are real, and the supply is genuinely constrained. The option is real too, but it is an option, and a company that needs fusion demand to survive will not survive long enough to see it.

What follows is the case for sizing the first plant to the niche, and building the industrial base that makes the next product possible. The same feed handling, power, and thermal infrastructure that heats regolith for helium-3 can support oxygen, metals, and sintered structural material. Those products have larger markets and lower prices. They are the base. Helium-3 is the margin that pays for the first unit.

The comparison is worth stating plainly. At 10 ppb and 50% recovery, a tonne of regolith yields 5 milligrams of helium-3, worth about $100 at $20 million per kilogram. A tonne of regolith at 10% aluminium and 50% recovery, an optimistic assumption used for illustration, yields 50 kilograms of aluminium, worth about $198 at $3.97 per kilogram [19]. By gross revenue per tonne of feed, aluminium wins. By revenue per kilogram of product, helium-3 wins by a factor of five million. The first metric governs the size of the machine. The second governs the size of the market. The arithmetic is in Appendix B. A mine has to satisfy both, and the programme's model is built to find out whether any configuration does.

That is the question the first plant is designed to answer. A white paper cannot answer it.

---

## 8. The sequence

**The first machine should be small enough to fail.**

The programme is organised as a sequence of gates. Each gate has a question, a measurement, and a kill criterion. A gate that cannot be failed is not a gate.

**Gate 0: Prospect.** A small payload measures helium-3 and helium-4 at a candidate site, with a calibrated gas assay and a known sampling depth. The question is whether the grade is above 5 ppb, and whether it is spatially uniform enough to mine. The kill criterion is a measured grade below 5 ppb at the best accessible site, which would make the current architecture uneconomic and force a re-selection of product or site. A prospecting payload is of the order of tens of kilograms, not tonnes (an estimate; no payload design exists yet). It is the cheapest way to retire the largest unknown.

**Gate 1: Bench.** A laboratory unit processes simulant and, where available, lunar-derived feed. It measures release fraction versus temperature and time, capture efficiency, heat recovery, and the mass balance of the gas train. The question is whether 50% of the implanted helium can be recovered at 500 °C with at least 80% recuperation (the published Mark-III concept claims 85%). The kill criterion is a measured release below 30% at 800 °C, which would break the thermal route and move the programme to mechanical or hybrid extraction.

**Gate 2: Pilot.** A sub-scale unit, on the Moon, operates for one lunar day. It measures gas, power, dust, and thermal performance in the real environment. The question is whether the machine survives the night and whether the measured output matches the model within a factor of two. The kill criterion is a measured output below one-fifth of the model, which would mean the loss chain is not understood.

**Gate 3: Production.** A small fleet produces a few kilograms a year and sells them into the niche market. The question is whether the unit economics close at the contract price. The kill criterion is a cost per kilogram above the contract price after two years of operation.

**Gate 4: Base.** The same fleet produces bulk products for lunar use: oxygen, metals, and structural material. The question is whether the marginal cost of those products is below the cost of delivering them from Earth. This is where the industrial arc starts paying for itself: the industrial base becomes the business, and helium-3 becomes the margin rather than the product.

The sequence is deliberately front-loaded with measurement, and it is achievable on a startup calendar precisely because the loop in section 6 makes each gate cheap to close. A simple cost model says the first plant is dominated by launch mass: at $1 million per kilogram delivered to the lunar surface and $20 million per kilogram of product, every tonne of hardware must produce fifty kilograms over its life to break even. At $100,000 per kilogram, the requirement falls to five kilograms per tonne. That single ratio is a concrete design driver, because it tells the engineer what to minimise.

| Launch price | Product needed per tonne of hardware, over life |
|---:|---:|
| $1,000,000/kg | 50 kg |
| $500,000/kg | 25 kg |
| $100,000/kg | 5 kg |

No public data establishes a lunar plant's mass per unit of throughput. Hence the sequence starts with a pilot. The pilot measures the mass. The mass sets the launch requirement. The launch requirement sets the capital. The capital sets the price. The price meets the demand ceiling. The chain is closed, and every link is a number.

---

## 9. The landscape

**Interlune mines. We are building the industrial base beneath the space economy.**

Nobody on Earth has flown an in-situ helium assay. Every announced prospect is a forward forecast standing on sample interpolation until someone returns one. That gap is deliberately ours.

Interlune, founded by ex-Blue Origin leadership, is the only serious announced competitor in the field. It has an excavator running in Iowa (Vermeer, 2025), pure helium-3 from domestic helium (July 2026), and nearly $500 million in binding helium-3 purchase agreements with Maybell Quantum, Bluefors and the U.S. Department of Energy — its own accounting, not audited [25]. That is real, and it is a mining company: one isotope, one harvest, one cash flow.

**Where the difference actually lies.** Helium-3 is not the company; it is the wedge. The company is the first industrial base in space — energy and resources made off-world at scale, the thing that turns the space economy from a venture experiment into infrastructure the world depends on. Interlune sells one substance with a price tag. We are building the machine that makes the space economy possible: power, heat, gas handling, metals, oxygen, structure. The base from which habitats, manufacturing, propulsion and a permanent presence become consequences, not miracles. Whoever builds the first working base owns the century. That is the position this programme exists to hold.

**The edge, stated plainly.**

- Nobody has flown an in-situ prospecting assay. Ours is Gate 0. The first flown measurement is the number every buyer prices from afterwards.
- Our engineering loop runs at AI speed. The reading, the reconciliation, the simulation, the review close in days, and every piece is published and checkable.
- Nothing in this programme survives on hope. Our designs are closed against their own failure conditions before they are closed against any commitment.
- Capital burns in gate-sized increments with stated kill criteria. Each dollar buys one question answered or one reason to stop.

**The direct read.** The assay decides everything downstream, and ours comes first. From the assay: the gate, the bench, and then the base. We do not need to be the larger company to be the one whose measurement reprices the field.

---

## 10. The questions

**Ten questions a technical reader should ask, with the answers this paper can defend.**

**Why helium-3 rather than water or metals?**
Because it is the only lunar material whose price per delivered kilogram is high enough for a small plant to be revenue-relevant. Water and metals have larger markets and lower prices; they become attractive when the industrial base exists to make them cheaply. Helium-3 is the bootstrap, not the destination.

**Isn't the market too small?**
Yes, for a large plant. The market is about one to four kilograms a year [4][14][15] at current demand and supply. Hence the first plant is small, and the business case rests on the niche plus the industrial base, not on fusion demand.

**Why would anyone buy lunar helium-3 when terrestrial supply exists?**
Because the terrestrial supply is constrained by tritium decay and by the cost of separation from natural gas. A second source with a different cost structure is strategically valuable, and the first commercial contracts show buyers will pay for it. Whether they will pay enough at scale is unproven.

**Can the Moon supply it at a competitive cost?**
The physics allows it. The published estimates of $20–100 million per kilogram bracket the current price, which means the answer depends on launch mass, life, and recovery. The programme does not claim a cost. It claims a method for measuring one.

**What about the 14-day night?**
It is a design variable. A plant can stop, store, or site for illumination. Each choice has a mass and output penalty. The design basis models all three, and the pilot measures the one selected.

**Why not use nuclear power?**
It is a candidate for later phases. Solar is the primary source because it is abundant, scalable, and does not require a reactor qualification. A reactor would remove the night constraint at the cost of mass, licensing, and thermal rejection. The trade-off remains open; the design basis models both paths.

**Is the separation the hard part?**
It is one of the hard parts. The lunar helium is enriched about 200 times relative to terrestrial helium, which helps. Reaching 99% purity at 2 K still requires a cryogenic plant with a measured power budget. No public measurement supports a lunar-scale number, so the programme carries it as an unknown.

**What is the legal status?**
The Outer Space Treaty prohibits national appropriation of the Moon but does not settle whether a private party may extract and sell a resource [20]. The Moon Agreement, which treats resources as common heritage, has 17 parties (Saudi Arabia withdrew, effective 2024) and binds none of the major spacefaring states [21]. The United States, Luxembourg, the UAE, and Japan have enacted domestic frameworks recognising extracted resources as property [22]. The Artemis Accords, signed by 78 states as of October 2026, state that resource extraction does not inherently constitute national appropriation [23]. The practical position is that extraction is probably lawful for an operator whose state recognises it, and that the first serious dispute will be political, not technical.

**What happens if fusion never arrives?**
The niche market still exists, the industrial base still has value for lunar operations, and the option expires worthless. That is an acceptable outcome if the first plant is sized to the niche. It is not acceptable if the plan requires fusion demand to repay the capital.

**What is the biggest risk?**
The biggest risk is not geology, and not thermodynamics. It is that the loss chain, the sequence of small efficiencies from excavation to storage, multiplies to a recovery so low that the machine cannot pay for its own mass. The bench and pilot gates exist for that reason.

---

## 11. What this paper does not claim

It does not claim that a lunar helium-3 mine exists.
It does not claim a cost per kilogram.
It does not claim a measured grade at any site.
It does not claim that fusion will create demand.
It does not claim that the current architecture is the best one.
It does not claim that the programme's design basis is hardware.

It claims that the problem is real, that the arithmetic is checkable, that the first machine can be small, and that the sequence from prospecting to production is a sequence of measurements rather than promises.

---

## The co-founder

Kardashev is pre-funding. There is no salary on offer and no fund behind the cheque book. What exists is the problem, the method, and a public, reviewable body of work: a traceable design basis, a failure record, and a white paper at kardashev.aft.page. That is the whole asset sheet.

Two shapes of partner can make this real.

**A technical co-founder.** Someone who can own one of the hard parts — ISRU process engineering (high-temperature gas-solid reactions, volatiles, cryogenics); spacecraft thermal and mechanical systems (heat rejection, mechanisms, structures, dust); robotics and autonomy (perception, manipulation, fault recovery); or bulk materials handling (excavation, comminution, wear) — and who would rather build the machine than explain it. They take equity, not a salary. Compensation is ownership of what the machine becomes.

**A financial co-founder or angel.** Someone who reads the white paper and sees not a dream, but a sequence of cheap, falsifiable steps. They do not write a check against the Moon. They write one against the next gate — the prospecting payload, or the bench unit that settles release fraction on simulant — where the exposure is bounded, the kill criteria are explicit, and the downside is a measured no.

What a partner gets, either way: a founder with demonstrable and checkable velocity (a public design basis, a live site, and the paper, executed while the usual paperwork is still being drafted), a method that keeps its own failures in the record, and a milestone sequence with stated stop conditions. What a partner does not get: fabricated traction, a salary, or optimism in place of arithmetic.

The signal is not a follower count. The best people in this field have small audiences because they are in laboratories. What matters is a first-author measurement, a flown or tested article, an SBIR or CLPS payload, or an open-source tool with real users. A person who has measured helium release from a simulant is worth more than a person who has explained it to a hundred thousand people.

The company is named after a scale, not a product. The first product is helium-3. The company is the machine that makes lunar industry possible, one measured step at a time. Your move.

---

## References

[1] Kardashev, N. S. (1964). Transmission of information by extraterrestrial civilizations. *Soviet Astronomy*, 8, 217.

[2] Sagan, C. (1973). *The Cosmic Connection*. Anchor Press. Logarithmic scale: K = (log10 P − 6)/10.

[3] Energy Institute (2024). *Statistical Review of World Energy 2024*. Primary energy consumption, 620 EJ in 2023, ~1.96×10^13 W.

[4] Nasr, M. (2026). Who Owns the Moon? A Case Study on Helium-3. Belfer Center for Science and International Affairs, 26 October 2026. https://www.belfercenter.org/research-analysis/who-owns-moon-case-study-helium-3

[5] Fa, W., & Jin, Y.-Q. (2007). Quantitative estimation of helium-3 spatial distribution in the lunar regolith layer. *Icarus*, 190, 15–23. https://doi.org/10.1016/j.icarus.2007.03.014

[6] Hintenberger, H., Weber, H., Voshage, H., Wänke, H., Begemann, F., & Wlotzka, F. (1970). Concentrations and isotopic abundances of the rare gases, hydrogen and nitrogen in Apollo 11 lunar fines. *Proceedings of the Apollo 11 Lunar Science Conference*, 1.

[7] Olson, A. D. S. (2021). Lunar Helium-3: Mining Concepts, Extraction Research, and Potential ISRU Synergies. AIAA ASCEND 2021. NASA NTRS 20210022801. https://ntrs.nasa.gov/citations/20210022801

[8] Internal design basis, F1-BASIS-C02. Apollo 17 sample assays 72501,27 and 70011,18: 4.656 and 11.209 ppb. Internal, versioned.

[9] Johnson, J. R., Swindle, T. D., & Lucey, P. G. (1999). Estimated solar wind-implanted helium-3 distribution on the Moon. *Geophysical Research Letters*, 26, 385–388. https://doi.org/10.1029/1998GL900305

[10] Crawford, I. A. (2015). Lunar resources: A review. *Progress in Physical Geography*, 39, 137–167. https://doi.org/10.1177/0309133314567585

[11] Nakayama, Y., Kudo, N., Kuroiwa, N., Endo, R., Ota, H., & Nishi, T. (2025). 温度変調型示差走査熱量計を用いた模擬月砂の比熱測定 [Specific heat of simulated lunar sand by temperature-modulated differential scanning calorimetry]. *Experimental Mechanics*, 25(1), 14–17. https://doi.org/10.11395/jjsem.25.14. The FJS-1 designation comes from the internal design basis, not the article metadata.

[12] Internal design basis, F1-BASIS-C01/A01 scalar check. 226,744.1 J/kg over 313–570 K, two numerical routes, relative difference 3.19×10^-9. Internal, versioned.

[13] Internal design basis (F1-BASIS-C02) and the F2 architecture study. Two candidate allocations; CAD/STEP pinned snapshots hash-verified 716/716 at file scope; geometry-to-parameter binding unproven, deferred to F3. Internal, versioned; closed at declared conditional scope, not accepted as hardware.

[14] US Department of Energy, Isotope Program. Supply and Demand of Helium-3. https://www.isotopes.gov/Supply-and-Demand-of-Helium-3

[15] US Government Accountability Office (2011). Managing Critical Isotopes: Weaknesses in DOE's Management of Helium-3 Delayed the Federal Response to a Critical Supply Shortage. GAO-11-472. https://www.gao.gov/products/gao-11-472

[16] Pulsar Helium. Helium-3 price range, $15,000–$19,000 per gram. https://pulsarhelium.com/he-hub/about-he/

[17] NIST (2018). Neutron detection method: long-sought workaround to helium shortage. https://www.nist.gov/news-events/news/2018/06/nist-neutron-detection-method-long-sought-workaround-helium-shortage

[18] Temmerman, G. D. (2021). The helium bubble: prospects for ³He-fuelled nuclear fusion. *Joule*, 5, 1312–1315. https://doi.org/10.1016/j.joule.2021.05.003

[19] USGS (2026). *Mineral Commodity Summaries 2026*: Aluminium and Titanium. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-aluminum.pdf

[20] United Nations (1967). Treaty on Principles Governing the Activities of States in the Exploration and Use of Outer Space, including the Moon and Other Celestial Bodies. https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html

[21] United Nations (1979). Agreement Governing the Activities of States on the Moon and Other Celestial Bodies. https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/moon-agreement.html — 17 parties; Saudi Arabia withdrew, effective 5 January 2024 (18 was cited in earlier drafts; the withdrawal reduced the count).

[22] US Commercial Space Launch Competitiveness Act, H.R. 2262 (2015); Luxembourg Law of 20 July 2017; UAE Federal Law No. 12 of 2019; Japan Act on the Promotion of Business Activities for Exploring and Developing Space Resources (2021).

[23] NASA. The Artemis Accords; 78 signatories as of 28 October 2026 (Vietnam, the 78th, signed that date). https://www.nasa.gov/artemis-accords/. Moon Agreement comparison: [21].

[24] Vasavada, A. R., et al. (2012). Lunar equatorial surface temperatures and regolith properties from the Diviner Lunar Radiometer Experiment. *Journal of Geophysical Research*, 117, E00H18. https://doi.org/10.1029/2011JE003987

[25] Interlune Corporation. Sources: https://interlune.space/ (claims nearly $500M in binding helium-3 purchase agreements, Maybell Quantum and Bluefors, May 2025 DOE Isotope Program 3-litre purchase), https://interlune.space/about (Meyerson, Lai, Hornsby, Schmitt adviser), https://interlune.space/press-releases (NASA $6.9M lunar resources contract May 2026, Vermeer excavator partnership 2025–2026, pure helium-3 from domestic helium July 2026, U.S. Air Force SBIR Direct-to-Phase II November 2025, helium-implanted simulant testing August 2026). Interlune's purchase figures are self-reported, not audited.


[26] Industrializing the Moon (2017, video essay). Vision framing for section 1. Popular exposition, not an engineering source. No technical claim in this paper depends on it.

---

## Appendix A. Units and conversions

- 1 ppb by mass = 1×10^-9 kg/kg = 1 mg per tonne.
- 1 tonne = 1,000 kg.
- 1 g of helium-3 at 10 ppb and 100% recovery requires 100 t of regolith; at 50% recovery, 200 t.
- 1 GJ = 277.8 kWh; 1 MWh = 3.6 GJ.
- 1 kg of helium-3 at $20 million/kg = $20,000 per gram.
- 1 litre of helium-3 gas at STP ≈ 0.135 g, so 7.4 litres ≈ 1 g.

## Appendix B. The arithmetic, step by step

1. Feed ratio: `m_feed = m_product / (grade × recovery)`.
2. Sensible heat: `Q = m_feed × ∫cp dT`. Over 313–570 K, the FJS-1 fit gives 226,744 J/kg [11][12].
3. Heat per gram: at 10 ppb and 50% recovery, 200 t × 0.5 MJ/kg = 100 GJ.
4. Net heat with recuperation: `Q_net = Q × (1 − r)`. At r = 0.85, 15 GJ = 4.2 MWh.
5. Night storage: `E = P × t_night`. At 1.4 MW and 1.275×10^6 s, 1.78×10^12 J = 495 MWh.
6. Break-even launch mass: `m_product / m_hardware = price_launch / price_product`. At $1M/kg and $20M/kg, the ratio is 0.05, i.e. 50 kg of product per tonne of hardware.
7. Aluminium comparison (illustrative, optimistic): 1 tonne of feed at 10% aluminium, 50% recovery → 50 kg Al ≈ $198 at $3.97/kg [19]; the same tonne yields 5 mg He-3 ≈ $100. Gross revenue per tonne favours aluminium; revenue per kilogram of product favours helium-3 by a factor of about 5 million.

## Appendix C. Status of the numbers

Measured: sample assays, heat-capacity fit within its range, surface temperatures, release fractions from Apollo sample 10084 [6][7].
Modelled: global inventory, plant mass, heat recovery.
Assumed: site grade, overall recovery, launch price, plant life.
Unknown: separation energy at 99% purity, capture efficiency, dust wear, robotic service life, cost per kilogram.

The paper's argument does not depend on any single unknown being favourable. It depends on the sequence that retires them in order of cost.
