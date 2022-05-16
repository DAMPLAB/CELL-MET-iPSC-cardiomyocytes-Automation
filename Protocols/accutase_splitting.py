# Accutase Splitting & Seeding of iPSCS Protocol for Opentrons Python API Version 2

# Written by Rita Chen 2022-04-01
# Modify by Rita Chen 2021-05-15

import math
from opentrons import protocol_api
from opentrons import types

metadata = {
    "apiLevel": "2.10",
    "protocolName": "accutase_splitting",
    "author": "Rita Chen",
    "description": "Perform iPSCs accutase splitting protocol to 6-well culture plate",
}

def run(protocol: protocol_api.ProtocolContext):
    # Load temperature module for media and input plate
    input_temp_mod = protocol.load_module(
        "temperature module gen2",
        10,
        label="Temperature Module for Dissociation Plate",
    )

    splitting_plate = input_temp_mod.load_labware(
        "corning_6_wellplate_16.8ml_flat",
        label="Input Plate - Accutase Splitting",
    )

    reagent_temp_mod = protocol.load_module(
        "tempdeck",
        7,
        label="Temperature Module for Reagents",
    )

    reagent_reservior = reagent_temp_mod.load_labware(
        "usascientific_12_reservoir_22ml",
        label="Reagent Reservoir",
    )

    # Load labware, tiprack, and pipettes
    # Ecah accutase tubes need to be pre-filled with 5mL of PBS buffer
    input_plate = protocol.load_labware(
        load_name="corning_6_wellplate_16.8ml_flat",
        location=5,
        label="Input Culture Plate",
    )

    output_plate = protocol.load_labware(
        load_name="corning_6_wellplate_16.8ml_flat",
        location=6,
        label="Output Culture Plate",
    )

    accutase_tubes = protocol.load_labware(
        load_name="opentrons_15_tuberack_falcon_15ml_conical",
        location=8,
        label="Accutase Tubes",
    )

    waste_reservoir = protocol.load_labware(
        load_name="agilent_1_reservoir_290ml",
        location=11,
        label="Waste Reservoir",
    )

    tiprack_1000 = protocol.load_labware(
        load_name="opentrons_96_filtertiprack_1000ul",
        location=4,
        label="Filter Tip 1000",
    )

    p1000_s = protocol.load_instrument(
        instrument_name="p1000_single",
        mount="right",
        tip_racks=[tiprack_1000],
    )

    # Reagents
    input_pbs = reagent_reservior["A1"]
    output_pbs = reagent_reservior["A2"]
    media_1 = reagent_reservior["A4"]
    media_2 = reagent_reservior["A5"]
    media_3 = reagent_reservior["A6"]
    media_4 = reagent_reservior["A7"]
    media_5 = reagent_reservior["A8"]
    accutase = reagent_reservior["A12"]
    waste = waste_reservoir["A1"]
    cell_accutase = accutase_tubes["A1"]

    # Default settings
    # Aspirate at the default flowrate of 150 ul/s
    # Dispense at the default flowrate of 300 ul/s
    # By default, the OT-2 will aspirate and dispense 1mm above the bottom of a well.

    # available_deck_slots = ['1', '2' '3', '9']

    #######################Start seeding protocol with accutase splitting####################
    protocol.comment("Begin seeding protocol with accutase splitting!")
    # Turn on robot rail lights
    protocol.set_rail_lights(True)

    # Set temperature module to 37C
    reagent_temp_mod.set_temperature(37)
    input_temp_mod.set_temperature(37)

    # Create a well list for 6-well culture plate well locations to output the correct well location for liquid transfer
    culture_12 = 4 # number of columns for 12-well culture plate, 3x4

    culture_6 = 3 # number of columns for 6-well culture plate, 2x3
    count = 2
    well_list = []
    for j in range(count):
        for i in range(1,(culture_6+1)):
            well_list.append(f"{chr(j + 65)}{i}")

    # Constants for Protocol
    well_num = 6
    diameter = input_plate['A1'].diameter
    depth = input_plate['A1'].depth
    z_pos_low = -9.2 # z-coordinate for the well bottom of culture plate
    z_pos_high = depth-7 # z-coordinate for the well top of culture plate
    x_pos = 0 # x-coordinate for the well of culture plate
    x_pos_left = -(diameter/2-2.5) # x-coordinate for the well left top of culture plate
    x_pos_right = diameter/2-2.5 # y-coordinate for the well right top of culture plate
    y_pos = 0 # y-coordinate for the well of culture plate
    y_pos_low = -(diameter/2-2.5) # y-coordinate for the well bottom of culture plate
    y_pos_high = diameter/2-2.5 # y-coordinate for the well top of culture plate

    # Remove Waste Media for Input Plate
    protocol.comment("Remove waste media for input culture plate!")
    p1000_s.flow_rate.dispense = 500 # Change dispense speed to 500ul/s
    p1000_s.pick_up_tip()
    for i in range(0, well_num):
        # Get the center of each well.
        center_location = input_plate[well_list[i]].center()
        # Get a location that's bottom y-coordinate and bottom z-coordinate from the center of each well.
        adjusted_location_bottom = center_location.move(types.Point(x_pos, y_pos_low, z_pos_low))
        # Remove Waste Media 2000uL/well
        for j in range(0, 2):
            # Move to bottom y-coordinate and bottom z-coordinate from the center of each well.
            p1000_s.move_to(adjusted_location_bottom)
            p1000_s.aspirate(1000)
            p1000_s.dispense(1000, waste.top())
            p1000_s.blow_out()
    p1000_s.drop_tip()

    # Perform PBS Wash for Input Plate
    protocol.comment("Perform PBS wash for input culture plate!")
    p1000_s.flow_rate.dispense = 250 # Change default dispense speed to 250ul/s
    p1000_s.pick_up_tip()
    for i in range(0, well_num):
        # Aspirate PBS Buffer 500uL/well
        p1000_s.aspirate(500, input_pbs.bottom())
        # Get the center of each well.
        center_location = input_plate[well_list[i]].center()
        # Get a location that's top y-coordinate and top z-coordinate from the center of each well.
        adjusted_location_top = center_location.move(types.Point(x_pos, y_pos_high, z_pos_high))
        '''
        # Get a location that's left x-coordinate and top z-coordinate from the center of each well.
        adjusted_location_left = center_location.move(types.Point(x_pos_left, y_pos, z_pos_high))
        # Get a location that's right x-coordinate and top z-coordinate from the center of each well.
        adjusted_location_right = center_location.move(types.Point(x_pos_right, y_pos, z_pos_high))
        '''
        # Need to divide the dispense into 4 regions, 125uL/region/well ???
        # Move to top y-coordinate and top z-coordinate from the center of each well.
        # Dispense PBS Buffer 500uL/well
        p1000_s.move_to(adjusted_location_top)
        p1000_s.dispense(500)
        '''
        p1000_s.move_to(adjusted_location_top)
        p1000_s.dispense(125)
        # Move to center of each well.
        p1000_s.move_to(center_location)
        p1000_s.dispense(125)
        # Move to left x-coordinate and top z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_left)
        p1000_s.dispense(125)
        # Move to right x-coordinate and top z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_right)
        p1000_s.dispense(125)
        '''
        p1000_s.blow_out()
    p1000_s.drop_tip()

    # Remove PBS Wash for Input Plate
    protocol.comment("Remove PBS wash for input culture plate!")
    p1000_s.flow_rate.dispense = 500 # Change dispense speed to 500ul/s
    p1000_s.pick_up_tip()
    for i in range(0, well_num):
        # Get the center of each well.
        center_location = input_plate[well_list[i]].center()
        # Get a location that's bottom y-coordinate and bottom z-coordinate from the center of each well.
        adjusted_location_bottom = center_location.move(types.Point(x_pos, y_pos_low, z_pos_low))
        # Move to bottom y-coordinate and bottom z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_bottom)
        # Remove PBS Buffer 500uL/well
        p1000_s.aspirate(550)
        p1000_s.dispense(550, waste.top())
        p1000_s.blow_out()
    p1000_s.drop_tip()

    # Perform Accutase Splitting for Input Plate
    protocol.comment("Perform accutase splitting for input culture plate!")
    p1000_s.flow_rate.dispense = 250 # Change default dispense speed to 250ul/s
    p1000_s.pick_up_tip()
    for i in range(0, well_num):
        # Aspirate Accutase 500uL/well
        p1000_s.aspirate(500, accutase.bottom())
        # Get the center of each well.
        center_location = input_plate[well_list[i]].center()
        # Get a location that's top y-coordinate and top z-coordinate from the center of each well.
        adjusted_location_top = center_location.move(types.Point(x_pos, y_pos_high, z_pos_high))
        '''
        # Get a location that's left x-coordinate and top z-coordinate from the center of each well.
        adjusted_location_left = center_location.move(types.Point(x_pos_left, y_pos, z_pos_high))
        # Get a location that's right x-coordinate and top z-coordinate from the center of each well.
        adjusted_location_right = center_location.move(types.Point(x_pos_right, y_pos, z_pos_high))
        '''
        # Need to divide the dispense into 4 regions, 125uL/region/well ???
        # Move to top y-coordinate and top z-coordinate from the center of each well.
        # Dispense Accutase 500uL/well
        p1000_s.move_to(adjusted_location_top)
        p1000_s.dispense(500)
        '''
        p1000_s.move_to(adjusted_location_top)
        p1000_s.dispense(125)
        # Move to center of each well.
        p1000_s.move_to(center_location)
        p1000_s.dispense(125)
        # Move to left x-coordinate and top z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_left)
        p1000_s.dispense(125)
        # Move to right x-coordinate and top z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_right)
        p1000_s.dispense(125)
        '''
        p1000_s.blow_out()
    p1000_s.drop_tip()

    # Incubate Input Plate @37C for 7 Minutes
    protocol.pause('Place input culture plate on the Temperature Module for 7 minutes incubation @37C for accutase splitting!')
    protocol.delay(minutes=7)
    protocol.pause('Complet incubate, place input culture plate to its original location!')

    # Collect Cell/Accutase Mixture for Centrifuge
    protocol.comment("Collect cell/accutase mixture for centrifuge!")
    p1000_s.flow_rate.dispense = 300 # Change dispense speed to 300ul/s
    p1000_s.pick_up_tip()
    for i in range(0, well_num):
        # Get the center of each well.
        center_location = input_plate[well_list[i]].center()
        # Get a location that's bottom y-coordinate and bottom z-coordinate from the center of each well.
        adjusted_location_bottom = center_location.move(types.Point(x_pos, y_pos_low, z_pos_low))
        # Get a location that's top y-coordinate and top z-coordinate from the center of each well.
        adjusted_location_top = center_location.move(types.Point(x_pos, y_pos_high, z_pos_high))
        # Move to bottom y-coordinate and bottom z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_bottom)
        # Collect Cell/Accutase Mixture 500uL/well
        # Mix 3 times, p1000_s.mix(3, 450)
        for i in range(0, 5):
            p1000_s.move_to(adjusted_location_bottom)
            p1000_s.aspirate(450)
            p1000_s.move_to(adjusted_location_top)
            p1000_s.dispense(450)
        p1000_s.aspirate(520)
        p1000_s.dispense(520, cell_accutase.bottom(15))
        p1000_s.blow_out()
    p1000_s.drop_tip()
    protocol.pause('Spin cell/accutase mixture @1000rpm for 4 minutes @4C/RT!')

    # Remove Supernatant can be performed manually
    '''
    # Remove Supernatant From Cell/Accutase Mixture After Centrifuge
    protocol.comment("Remove supernatant from cell/accutase mixture after centrifuge!")
    p1000_s.flow_rate.dispense = 500 # Change dispense speed to 500ul/s
    p1000_s.pick_up_tip()
    for i in range(0, 4):
        p1000_s.aspirate(1000, cell_accutase.bottom(10))
        p1000_s.dispense(1000, waste.top())
        p1000_s.blow_out()
    for i in range(0, 4):
        p1000_s.aspirate(1000, cell_accutase.bottom(2))
        p1000_s.dispense(1000, waste.top())
        p1000_s.blow_out()
    p1000_s.drop_tip()
    '''

    # Add 1mL mTeSR medium with Y27632
    protocol.comment("Add 1mL mTeSR medium with Y27632 to cell pellet!")
    p1000_s.flow_rate.dispense = 250 # Change dispense speed to 250ul/s
    p1000_s.pick_up_tip()
    p1000_s.aspirate(1000, media_1.bottom())
    p1000_s.dispense(1000, cell_accutase.bottom(15))
    # Mix 5 times, p1000_s.mix(5, 900)
    for i in range (0, 5):
        p1000_s.aspirate(900, cell_accutase.bottom(5))
        p1000_s.dispense(1000, cell_accutase.bottom(15))
    p1000_s.blow_out()
    p1000_s.drop_tip()

    # Remove Waste Media for Output Plate
    protocol.comment("Remove waste media for output culture plate!")
    p1000_s.flow_rate.dispense = 500 # Change dispense speed to 500ul/s
    p1000_s.pick_up_tip()
    for i in range(0, well_num):
        # Get the center of each well.
        center_location = output_plate[well_list[i]].center()
        # Get a location that's bottom y-coordinate and bottom z-coordinate from the center of each well.
        adjusted_location_bottom = center_location.move(types.Point(x_pos, y_pos_low, z_pos_low))
        # Remove Waste Media 2000uL/well
        for j in range(0, 2):
            # Move to bottom y-coordinate and bottom z-coordinate from the center of each well.
            p1000_s.move_to(adjusted_location_bottom)
            p1000_s.aspirate(1000)
            p1000_s.dispense(1000, waste.top())
            p1000_s.blow_out()
    p1000_s.drop_tip()

    # Perform PBS Wash for Output Plate
    protocol.comment("Perform PBS wash for output culture plate!")
    p1000_s.flow_rate.dispense = 250 # Change default dispense speed to 250ul/s
    p1000_s.pick_up_tip()
    for i in range(0, well_num):
        # Aspirate PBS Buffer 500uL/well
        p1000_s.aspirate(500, output_pbs.bottom())
        # Get the center of each well.
        center_location = output_plate[well_list[i]].center()
        # Get a location that's top y-coordinate and top z-coordinate from the center of each well.
        adjusted_location_top = center_location.move(types.Point(x_pos, y_pos_high, z_pos_high))
        '''
        # Get a location that's left x-coordinate and top z-coordinate from the center of each well.
        adjusted_location_left = center_location.move(types.Point(x_pos_left, y_pos, z_pos_high))
        # Get a location that's right x-coordinate and top z-coordinate from the center of each well.
        adjusted_location_right = center_location.move(types.Point(x_pos_right, y_pos, z_pos_high))
        '''
        # Need to divide the dispense into 4 regions, 125uL/region/well ???
        # Move to top y-coordinate and top z-coordinate from the center of each well.
        # Dispense PBS Buffer 500uL/well
        p1000_s.move_to(adjusted_location_top)
        p1000_s.dispense(500)
        '''
        p1000_s.move_to(adjusted_location_top)
        p1000_s.dispense(125)
        # Move to center of each well.
        p1000_s.move_to(center_location)
        p1000_s.dispense(125)
        # Move to left x-coordinate and top z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_left)
        p1000_s.dispense(125)
        # Move to right x-coordinate and top z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_right)
        p1000_s.dispense(125)
        '''
        p1000_s.blow_out()
    p1000_s.drop_tip()

    # Remove PBS Wash for Output Plate
    protocol.comment("Remove PBS wash for output culture plate!")
    p1000_s.flow_rate.dispense = 500 # Change dispense speed to 500ul/s
    p1000_s.pick_up_tip()
    for i in range(0, well_num):
        # Get the center of each well.
        center_location = output_plate[well_list[i]].center()
        # Get a location that's bottom y-coordinate and bottom z-coordinate from the center of each well.
        adjusted_location_bottom = center_location.move(types.Point(x_pos, y_pos_low, z_pos_low))
        # Move to bottom y-coordinate and bottom z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_bottom)
        # Remove PBS Buffer 500uL/well
        p1000_s.aspirate(550)
        p1000_s.dispense(550, waste.top())
        p1000_s.blow_out()
    p1000_s.drop_tip()

    # Add Fresh Media for Output Plate
    protocol.comment("Add fresh media for output culture plate!")
    p1000_s.flow_rate.dispense = 250 # Change default dispense speed to 250ul/s
    p1000_s.pick_up_tip()
    for j in range(0,2):
        for i in range(0, well_num):
        # Aspirate fresh media 2000uL/well
            p1000_s.aspirate(750, media_1.bottom())
            # Get the center of each well.
            center_location = output_plate[well_list[i]].center()
            # Get a location that's top y-coordinate and top z-coordinate from the center of each well.
            adjusted_location_top = center_location.move(types.Point(x_pos, y_pos_high, z_pos_high))
            # Move to top y-coordinate and top z-coordinate from the center of each well.
            p1000_s.move_to(adjusted_location_top)
            # Dispense fresh media 2000uL/well
            p1000_s.dispense(750)
            p1000_s.blow_out()
    p1000_s.drop_tip()

    # Add 100uL Cell Suspension Into Fresh Well of Output Plate
    protocol.comment("Add 100uL cell suspension into gresh well of output culture plate!")
    p1000_s.flow_rate.dispense = 125 # Change default dispense speed to 125ul/s
    p1000_s.pick_up_tip()
    p1000_s.aspirate(600, cell_accutase.bottom(2))
    for i in range(0, well_num):
        # Aspirate PBS Buffer 500uL/well
        # Get the center of each well.
        center_location = output_plate[well_list[i]].center()
        # Get a location that's top y-coordinate and top z-coordinate from the center of each well.
        adjusted_location_top = center_location.move(types.Point(x_pos, y_pos_high, z_pos_high))
        '''
        # Get a location that's left x-coordinate and top z-coordinate from the center of each well.
        adjusted_location_left = center_location.move(types.Point(x_pos_left, y_pos, z_pos_high))
        # Get a location that's right x-coordinate and top z-coordinate from the center of each well.
        adjusted_location_right = center_location.move(types.Point(x_pos_right, y_pos, z_pos_high))
        '''
        # Need to divide the dispense into 4 regions, 125uL/region/well ???
        # Move to top y-coordinate and top z-coordinate from the center of each well.
        # Add 100uL cell suspension per well
        p1000_s.move_to(adjusted_location_top)
        p1000_s.dispense(100)
        '''
        p1000_s.move_to(adjusted_location_top)
        p1000_s.dispense(125)
        # Move to center of each well.
        p1000_s.move_to(center_location)
        p1000_s.dispense(125)
        # Move to left x-coordinate and top z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_left)
        p1000_s.dispense(125)
        # Move to right x-coordinate and top z-coordinate from the center of each well.
        p1000_s.move_to(adjusted_location_right)
        p1000_s.dispense(125)
        '''
        p1000_s.blow_out()
    p1000_s.drop_tip()

    # Protocol Completed!
    protocol.comment("Protocol completed! Put plate back into 37C incubator and perform medium change daily until cells are ready for passage ")
    # Turn off robot rail lights
    protocol.set_rail_lights(False)
