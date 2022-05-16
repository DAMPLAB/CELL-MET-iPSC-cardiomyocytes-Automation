# Instructions for CELL-MET-iPSC-cardiomyocytes-Automation
<p align="center">
  <img src="https://user-images.githubusercontent.com/32885235/95505810-fb33c200-097c-11eb-9cb9-3f299bb68920.png" />
</p>

## About
This document is intended to guide users through iPSC-derived cardiomyocytes culturing and differentiation. This workflow enables iPSC differentiation into cardiomyocytes via Wnt signaling pathway using the OT2 liquid handling robot by Opentrons. This includes:
- Accutase splitting and seeding of induced pluripotent stem cells (iPSCs)
- Induced pluripotent stem cells (iPSCs) differentiation into cardiomyocytes (CMs) via Wnt signaling pathway
- Re-plating cardiomyocytes (CMs) onto fibronectin coating plate

## Materials
Below we list the materials previously used to implement CELL-MET iPSC-cardiomyocytes automation workflow. We recommend starting with these consumables, however certain standard labwares may be altered. Labware needs to be defined carefully when working with OpenTrons OT-2 liquid handling robot and changes to labware requires the user to update the protocol scripts and the labwares used during the execution of the iPSC-cardiomyocytes culturing and differentiation runs. Here is a general [OpenTrons’ Guideline](https://support.opentrons.com/en/articles/3137426-what-labware-can-i-use-with-the-ot-2) for utilizing labware for users new to OT2 and additional details regarding labware can be found on [OpenTrons Labware Library](https://labware.opentrons.com/).

### Software:
- OpenTrons OT-2 App (Version 3.10.3 or later)
- Python 3
- [CELL-MET iPSC-cardiomyocytes Automation](https://github.com/DAMPLAB/CELL-MET-iPSC-cardiomyocytes-Automation)

### Hardware:
- [OpenTrons OT-2](https://opentrons.com/ot-2)
- [OpenTrons P1000 Single-Channel Generation 2 Electronic Pipette](https://opentrons.com/pipettes)
- [OpenTrons Temperature Module Generation 2](https://opentrons.com/modules#temperature)

### Consumables & Reagents:
- [OpenTrons 1000 µL Filter Tips](https://shop.opentrons.com/opentrons-1000ul-filter-tips-1000-racks/)
- [Corning 6 Well Plate 16.8 mL Flat](https://ecatalog.corning.com/life-sciences/b2c/US/en/Microplates/Assay-Microplates/96-Well-Microplates/Costar%C2%AE-Multiple-Well-Cell-Culture-Plates/p/3335)
- [Agilent 1 Well Reservoir 290 mL](https://www.agilent.com/store/en_US/Prod-201252-100/201252-100)
- [USA Scientific 12- well Reservoir](https://www.usascientific.com/12-channel-automation-reservoir/p/1061-8150)
- [Opentrons 15 Tube Rack with Falcon 15 mL Conical](https://shop.opentrons.com/4-in-1-tube-rack-set/)
- [Opentrons 6 Tube Rack with Falcon 50 mL Conical](https://shop.opentrons.com/4-in-1-tube-rack-set/)
- [Thermo Scientific Adhesive PCR Plate Foils](https://www.thermofisher.com/order/catalog/product/A47814#/A47814)
- Additional Reagents:
    - 70% Ethanol, Histological
    - PBS Buffer
    - Cell Culture Grade Water
    - Matrigel, Growth Factor Reduced Membrane Matrix 354230 (Fisher Scientific catalog CB-40230)
    - Y-27632 Dihydrochloride (Tocris Bioscience catalog 1254, 10mg)
    - mTeSR1 Medium (Stemcell Technologies Inc, basal medium catalog 05850, 5x supplement catalog 05852)
    - IWP4 (Tocris Bioscience catalog 5214)
    - CHIR99021 (Tocris Bioscience catalog 4423)
    - FreSR™-S (Stemcell Technologies Inc catalog 05859)
    - Fibronectin (Fisher Scientific catalog 356009)
    - DMEM/F-12, HEPES (Fisher Scientific catalog 11-330-057)
    - DMSO, Dimethyl Sulfoxide (Fisher Scientific catalog BP231-1)
    - Accutase™ Cell Detachment Solution (Fisher Scientific catalog MT25058CI)
    - RPMI 1640 Medium, GlutaMAX™ Supplement (Fisher Scientific catalog 61-870-127)
    - B-27™ Supplement, minus insulin (Fisher Scientific catalog A1895601)
    - B-27™ Supplement (50X), custom with insulin (Fisher Scientific catalog 00-800-85SA)
    - RPMI 1640 Medium, no glucose (Fisher Scientific catalog 11-879-020)
    - Sodium L-lactate (Fisher Scientific catalog AAL1450014)
    - Trypsin-EDTA (0.25%), phenol red (Fisher Scientific catalog 25-200-072)
    - 10 ug/mL DNAse (Stemcell Technologies Inc catalog NC9007308)
    - Fetal Bovine Serum (Fisher Scientific catalog MT35015CF)

## Protocol
### OT-2 Preparation
Follow the Opentrons guidelines for setting up the OT-2 before executing any protocols.

### General Installation
Using any web browser, navigate to the [GitHub directory](https://github.com/DAMPLAB/CELL-MET-iPSC-cardiomyocytes-Automation) and follow the instructions provided in the **README.md** for the General Installation to install the necessary software setup.

### Prepare 70% Ethanol
Prepare 70% Ethanol spray bottles using Ethanol and Deionized Water for surface disinfectant.

### Prepare Reagents in the Proper Labware for Accutase Splitting & Seeding of iPSCs Protocol
Follow the instruction provided in the section on **Accutase splitting of iPSCs** for [iPSC culture and differentiation.pdf](https://github.com/DAMPLAB/CELL-MET-iPSC-cardiomyocytes-Automation/blob/main/iPSC%20culture%20and%20differentiation.pdf) for preparing the necessary reagents. Refer to Figure 1B for the appropriate labware needed for protocol execution.    
**NOTE:** When prepare for reagents in the proper labware, be sure to account for 10% overage.

### Execute Accutase Splitting & Seeding of iPSCs Protocol on OT-2
1. Open up OT2 APP, and upload the *accutase_splitting.py* for performing accutase splitting and seeding of iPSCs. [15 Minutes / Variable]
2. Once the protocol is uploaded, following the calibration instructions provided by the OT2 APP by placing the two Temperature Modules (Temperature Module 1 with the reagent reservoir, Temperature Module 2 for incubation of accutase splitting), the Waste Reservoir, the Opentrons 15 Tube Rack with Falcon 15 mL Conical, the Opentrons 1000 µL Filter Tips, a input culture plate, and five output culture plates onto the deck of the liquid handler (Figure 1A and 1B). [3 Minutes / Variable]         
3. Once the calibration process is completed, proceed to running the protocol. [15 Minutes / Variable]     
  **NOTE:** Always allow the robotic liquid handler to complete the execution of a script before trying to access the deck space.    
  **NOTE:** Protocol will pause to ensure proper incubation by placing of input plate onto the temperature module and must be resumed manually.      
  **NOTE:** Protocol will pause to allow external centrifugation step and must be resumed manually.   
4. The robotic liquid handler would automatically pause when the accutase splitting and seeding of iPSCs protocol is completed.
5. Transfer output culture plates back into 37C incubator.     
  **NOTE:** Move the plate in three quick, short, back-and-forth and side-to-side motions to disperse the cells across the surface of the well.     
  **NOTE:** Medium change daily with fresh RT mTeSR1 medium without Y-27632 (@ 2mL/well) until cells are ready (70%-90% confluent, every 3-5 days) for passage.

<p align="center">
  <img src="https://user-images.githubusercontent.com/32885235/168688485-4085666f-6652-44fb-9cbd-dcecf87e8c46.png" />

  **Figure 1:** Workflow for executing accutase splitting and seeding of iPSCs protocol on OT-2.     
  **(A)** Representative OT-2 deck layout with labwares and pipette tip boxes placement locations.     
  **(B)** Representative OT-2 deck layout for plate setup instructions
</p>

### Prepare Reagents in the Proper Labware for iPSCs Differentiation With/out PBS Wash Protocol
Follow the instruction provided in the section on **iPSCs differentiation into CMs (Wnt pathway)** for [iPSC culture and differentiation.pdf](https://github.com/DAMPLAB/CELL-MET-iPSC-cardiomyocytes-Automation/blob/main/iPSC%20culture%20and%20differentiation.pdf) for preparing the necessary reagents. Refer to Figure 2B for the appropriate labware needed for protocol execution.    
**NOTE:** When prepare for reagents in the proper labware, be sure to account for 10% overage.

### Execute iPSCs Differentiation With/out PBS Wash Protocol on OT-2
1. Open up OT2 APP, and upload the *ipsc_differentiation_with_wash.py* for performing iPSCs differentiation with PBS wash, or upload the *ipsc_differentiation_without_wash.py* for performing iPSCs differentiation without PBS wash. [5 Minutes / Variable]
2. Once the protocol is uploaded, following the calibration instructions provided by the OT2 APP by placing the Temperature Modules and the Reagent Reservoir, the Waste Reservoir, the Opentrons 1000 µL Filter Tips, and eight culture plates onto the deck of the liquid handler (Figure 2A and 2B). [3 Minutes / Variable]    
3. Once the calibration process is completed, proceed to running the protocol. [5 Minutes / Variable]     
  **NOTE:** Always allow the robotic liquid handler to complete the execution of a script before trying to access the deck space.       
4. The robotic liquid handler would automatically pause when the iPSCs differentiation protocol is completed.
5. Transfer culture plates back into 37C incubator.     
  **NOTE:** Move the plate in three quick, short, back-and-forth and side-to-side motions to disperse the cells across the surface of the well.     
  **NOTE:** Medium change when neccessary with based on days of experiment until cells are ready for replating.

<p align="center">
  <img src="https://user-images.githubusercontent.com/32885235/168690248-adbecd9f-80f3-44d0-8515-db9184b0cf11.png" />

  **Figure 2:** Workflow for executing iPSCs differentiation with PBS wash protocols on OT-2.     
  **(A)** Representative OT-2 deck layout with labwares and pipette tip boxes placement locations.     
  **(B)** Representative OT-2 deck layout for plate setup instructions
</p>

### Prepare Reagents in the Proper Labware for Re-plating Cardiomyocytes Protocol
Follow the instruction provided in the section on **Re-plating Cardiomyocytes** for [iPSC culture and differentiation.pdf](https://github.com/DAMPLAB/CELL-MET-iPSC-cardiomyocytes-Automation/blob/main/iPSC%20culture%20and%20differentiation.pdf) for preparing the necessary reagents. Refer to Figure 3B for the appropriate labware needed for protocol execution.    
**NOTE:** When prepare for reagents in the proper labware, be sure to account for 10% overage.

### Execute Re-plating Cardiomyocytes Protocol on OT-2
1.The replating of cardiomyocytes step is divided into two protocols. **Part 1** of the protocol, the *replating_cardiomyocytes_part1.py*, perfroms trypsin dissocation and FBS neutralization. Whereas, **Part 2** of the protocol, the *replating_cardiomyocytes_part2.py*, perfroms replating of the neutralized cells onto fibronectin coated plate.
2. Open up OT2 APP, and upload the *replating_cardiomyocytes_part1.py* or *replating_cardiomyocytes_part2.py* for performing replating of cardiomyocytes. [30 Minutes / Variable]
3. Once the protocol is uploaded, following the calibration instructions provided by the OT2 APP by placing the two Temperature Modules (Temperature Module 1 with the reagent reservoir, Temperature Module 2 for incubation of trypsin dissociation), the Waste Reservoir, the Opentrons 15 Tube Rack with Falcon 15 mL Conical, the Opentrons 1000 µL Filter Tips, a input culture plate, and five output culture plates onto the deck of the liquid handler (Figure 1A and 1B). [3 Minutes / Variable]         
4. Once the calibration process is completed, proceed to running the protocol. [30 Minutes / Variable]     
  **NOTE:** Always allow the robotic liquid handler to complete the execution of a script before trying to access the deck space.    
  **NOTE:** Protocol will pause to ensure proper incubation by placing of input plate onto the temperature module and must be resumed manually.   
  **NOTE:** Protocol will pause to allow external centrifugation step and must be resumed manually.  
5. The robotic liquid handler would automatically pause when the replating of cardiomyocytes protocol is completed.
6. Transfer output culture plates back into 37C incubator.     
  **NOTE:** Move the plate in three quick, short, back-and-forth and side-to-side motions to disperse the cells across the surface of the well.     
  **NOTE:** Medium change daily with freshRPMI B-27 with insulin (@ 2mL/well).

<p align="center">
  <img src="https://user-images.githubusercontent.com/32885235/168691814-b9a61a81-241e-4dae-a216-5cd4f83f6526.png" />

  **Figure 3:** Workflow for executing part 1 of replating of cardiomyocytes protocols on OT-2.     
  **(A)** Representative OT-2 deck layout with labwares and pipette tip boxes placement locations.     
  **(B)** Representative OT-2 deck layout for plate setup instructions
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/32885235/168691682-5b7dbb7c-e57f-40ef-bf4a-7a6817465842.png" />

  **Figure 4:** Workflow for executing part 2 of replating of cardiomyocytes protocols on OT-2.       
  **(A)** Representative OT-2 deck layout with labwares and pipette tip boxes placement locations.     
  **(B)** Representative OT-2 deck layout for plate setup instructions
</p>
