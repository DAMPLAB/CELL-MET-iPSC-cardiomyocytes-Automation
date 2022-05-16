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
    - 70% Ethanol
    -

## Protocol
### OT-2 Preparation
Follow the Opentrons guidelines for setting up the OT-2 before executing any protocols.

### General Installation
Using any web browser, navigate to the [GitHub directory](https://github.com/DAMPLAB/CELL-MET-iPSC-cardiomyocytes-Automation) and follow the instructions provided in the **README.md** for the General Installation to install the necessary software setup.

### Prepare 70% Ethanol
Prepare 70% Ethanol spray bottles using Ethanol and Deionized Water for surface disinfectant.

### Prepare Reagents in the Proper Labware for Accutase Splitting & Seeding of iPSCs Protocol
Follow the instruction provided in the section on **Accutase splitting of iPSCs** for [iPSC culture and differentiation.pdf](https://github.com/DAMPLAB/CELL-MET-iPSC-cardiomyocytes-Automation) for preparing the necessary reagents. Refer to Figure 1B for the appropriate labware needed for protocol execution.    
**NOTE:** When prepare for reagents in the proper labware, be sure to account for 10% overage.

### Execute Accutase Splitting & Seeding of iPSCs Protocol on OT-2
1. Open up OT2 APP, and upload the *accutase_splitting.py* for performing accutase splitting of iPSCs. [15 Minutes / Variable]
2. Once the protocol is uploaded, following the calibration instructions provided by the OT2 APP by placing the Temperature Module and an empty Bio-Rad 96 well plate (Output Plate), the Magnetic Module and a USA Scientific 96 deep well plate containing the samples (Reaction Plate), the Reagents Plate, the Reagent Trough, the Waste Reservoir, two Opentrons 20 µL Filter Tips, and four Opentrons 200 µL Filter Tips Racks onto the deck of the liquid handler. (Figure 1A and 1B). [5 Minutes / Variable]     
  **NOTE:** 200 µL tip reload will be necessary, protocol will pause in the proper places and must be resumed manually.       
3. Once the calibration process is completed, proceed to running the protocol. [2 Hours / Variable]     
  **NOTE:** Always allow the robotic liquid handler to complete the execution of a script before trying to access the deck space.    
  **NOTE:** All shaking and incubation steps are performed with benchtop Eppendorf ThermoMixer® C.  Protocol will pause in the proper places and must be resumed manually.    
4. The robotic liquid handler would automatically pause when the RNA extraction protocol is completed. Leave the output plate on the OT2 robot (Deck #8), and immediately proceed to the qPCR assay preparation protocol.    
  **NOTE:** Significant bead carry over may adversely impact RT-PCR performance.

<p align="center">
  <img src="https://user-images.githubusercontent.com/32885235/97507189-0910ad80-1953-11eb-8523-cfd40ce13af3.png" />

  **Figure 1:** Workflow for executing RNA extraction protocols on OT-2.     
  **(A)** Representative OT-2 deck layout with labwares and pipette tip boxes placement locations.     
  **(B)** Representative OT-2 deck layout for plate setup instructions
</p>

### Prepare Reagents in the Proper Labware for iPSCs Differentiation With/out PBS Wash Protocol
Follow the instruction provided in the section on **iPSCs differentiation into CMs (Wnt pathway)** for [iPSC culture and differentiation.pdf](https://github.com/DAMPLAB/CELL-MET-iPSC-cardiomyocytes-Automation) for preparing the necessary reagents. Refer to Figure 2B for the appropriate labware needed for protocol execution.    
**NOTE:** When prepare for reagents in the proper labware, be sure to account for 10% overage.

### Execute iPSCs Differentiation With/out PBS Wash Protocol on OT-2
1. Open up OT2 APP, and upload the *ipsc_differentiation_with_wash.py* for performing iPSCs differentiation with PBS wash, or upload the *ipsc_differentiation_without_wash.py* for performing iPSCs differentiation without PBS wash. [5 Minutes / Variable]
2. Once the protocol is uploaded, following the calibration instructions provided by the OT2 APP by placing the Temperature Modules 1 and a Bio-Rad 96 well plate containing purified RNA extraction form the previous workflow (Reaction Plate), place the Temperature Modules 2 and a Bio-Rad 96 well plate containing TaqPath™ master mixes (Reagents Plate), and one Opentrons 200 µL Filter Tips Racks onto the deck of the liquid handler (Figure 2A and 2B). [2 Minutes / Variable]    
  **NOTE:** Pipette replacement might be necessary, please follow the instructions provided by OT2 App.
3. Once the calibration process is completed, proceed to running the protocol. [12 Minutes / Variable]    
  **NOTE:** Always allow the robotic liquid handler to complete the execution of a script before trying to access the deck space.
4. The robotic liquid handler would automatically pause when the qPCR assay preparation protocol is completed. Seal and store the RNA Plate from the previous protocol.

<p align="center">
  <img src="https://user-images.githubusercontent.com/32885235/97507580-d915da00-1953-11eb-88fe-4cc303e58564.png" />

  **Figure 2:** Workflow for executing qPCR assay preparation protocols on OT-2.     
  **(A)** Representative OT-2 deck layout with labwares and pipette tip boxes placement locations.     
  **(B)** Representative OT-2 deck layout for plate setup instructions
</p>

### Prepare Reagents in the Proper Labware for Re-plating Cardiomyocytes Protocol
Follow the instruction provided in the section on **Re-plating Cardiomyocytes** for [iPSC culture and differentiation.pdf](https://github.com/DAMPLAB/CELL-MET-iPSC-cardiomyocytes-Automation) for preparing the necessary reagents. Refer to Figure 2B for the appropriate labware needed for protocol execution.    
**NOTE:** When prepare for reagents in the proper labware, be sure to account for 10% overage.

### Execute Re-plating Cardiomyocytes Protocol on OT-2
1. Open up OT2 APP, and upload the *replating_cardiomyocytes.py* for performing replating of cardiomyocytes. [30 Minutes / Variable]
2. Once the protocol is uploaded, following the calibration instructions provided by the OT2 APP by placing the Temperature Modules 1 and a Bio-Rad 96 well plate containing purified RNA extraction form the previous workflow (Reaction Plate), place the Temperature Modules 2 and a Bio-Rad 96 well plate containing TaqPath™ master mixes (Reagents Plate), and one Opentrons 200 µL Filter Tips Racks onto the deck of the liquid handler (Figure 2A and 2B). [2 Minutes / Variable]    
  **NOTE:** Pipette replacement might be necessary, please follow the instructions provided by OT2 App.
3. Once the calibration process is completed, proceed to running the protocol. [12 Minutes / Variable]    
  **NOTE:** Always allow the robotic liquid handler to complete the execution of a script before trying to access the deck space.
4. The robotic liquid handler would automatically pause when the qPCR assay preparation protocol is completed. Seal and store the RNA Plate from the previous protocol.

<p align="center">
  <img src="https://user-images.githubusercontent.com/32885235/97507580-d915da00-1953-11eb-88fe-4cc303e58564.png" />

  **Figure 2:** Workflow for executing qPCR assay preparation protocols on OT-2.     
  **(A)** Representative OT-2 deck layout with labwares and pipette tip boxes placement locations.     
  **(B)** Representative OT-2 deck layout for plate setup instructions
</p>
