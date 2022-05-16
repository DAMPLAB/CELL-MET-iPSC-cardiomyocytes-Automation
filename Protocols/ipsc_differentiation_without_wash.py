# iPSC Differentiation Protocol Without PBS Buffer Washing for Opentrons Python API Version 2

# Written by Rita Chen 2021-08-26
# Modify by Rita Chen 2021-08-27

import math
from opentrons import protocol_api
from opentrons import types

metadata = {
    "apiLevel": "2.10",
    "protocolName": "ipsc_differentiation_without_wash",
    "author": "Rita Chen",
    "description": "Perform iPSC differentiation protocol without PBS washing to 6-well culture plate",
}

def run(protocol: protocol_api.ProtocolContext):
    # Load temperature module for buffer and media
    reagent_temp_mod = protocol.load_module(
        "tempdeck",
        10,
        label="Temperature Module for Reagents",
    )

    reagent_reservior = reagent_temp_mod.load_labware(
        "usascientific_12_reservoir_22ml",
        label="Reagent Reservoir",
    )

    # Load labware, tiprack, and pipettes
    '''
    reagent_tubes = protocol.load_labware(
        load_name="opentrons_6_tuberack_falcon_50ml_conical",
        location=9,
        label="Reagent Tubes",
    )
    '''

    waste_reservoir = protocol.load_labware(
        load_name="agilent_1_reservoir_290ml",
        location=7,
        label="Waste Reservoir",
    )

    culture_plate = protocol.load_labware(
        load_name="corning_6_wellplate_16.8ml_flat",
        location=8,
        label="Culture Plate",
    )

    tiprack_1000 = protocol.load_labware(
        load_name="opentrons_96_filtertiprack_1000ul",
        location=11,
        label="Filter Tip 1000",
    )

    p1000_s = protocol.load_instrument(
        instrument_name="p1000_single",
        mount="right",
        tip_racks=[tiprack_1000],
    )

    # Reagents in well format
    media_1 = reagent_reservior[0]
    waste = waste_reservoir["A1"]

'''
    # Reagents in tube format
    # For tube, tube.bottom(22)
    media = reagent_tubes["B1"]
    waste = waste_reservoir["A1"]
'''

    # Default settings
    # Aspirate at the default flowrate of 150 ul/s
    # Dispense at the default flowrate of 300 ul/s
    # By default, the OT-2 will aspirate and dispense 1mm above the bottom of a well.

    # available_deck_slots = ['1', '2' '3', '4', '5', '6', '9']

    #######################Start differentiation protocol with PBS Wash####################
    protocol.comment("Begin differentiation protocol with wash!")
    # Turn on robot rail lights
    protocol.set_rail_lights(True)

    # Set temperature module to 37C
    reagent_temp_mod.set_temperature(37)

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
    diameter = culture_plate['A1'].diameter
    depth = culture_plate['A1'].depth
    z_pos_low = -9.2 # z-coordinate for the well bottom of culture plate
    z_pos_high = depth-7 # z-coordinate for the well top of culture plate
    x_pos = 0 # x-coordinate for the well of culture plate
    x_pos_left = -(diameter/2-2.5) # x-coordinate for the well left top of culture plate
    x_pos_right = diameter/2-2.5 # y-coordinate for the well right top of culture plate
    y_pos = 0 # y-coordinate for the well of culture plate
    y_pos_low = -(diameter/2-2.5) # y-coordinate for the well bottom of culture plate
    y_pos_high = diameter/2-2.5 # y-coordinate for the well top of culture plate

    # Remove Waste Media
    protocol.comment("Remove waste media!")
    p1000_s.flow_rate.dispense = 500 # Change dispense speed to 500ul/s
    p1000_s.pick_up_tip()
    for i in range(0, well_num):
        # Get the center of each well.
        center_location = culture_plate[well_list[i]].center()
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

    # Add Fresh Media
    protocol.comment("Add fresh media!")
    p1000_s.flow_rate.dispense = 250 # Change default dispense speed to 250ul/s
    p1000_s.pick_up_tip()
    for j in range(0,2):
        for i in range(0, well_num):
        # Aspirate fresh media 2000uL/well
            p1000_s.aspirate(925, media_1.bottom())
            # Get the center of each well.
            center_location = culture_plate[well_list[i]].center()
            # Get a location that's top y-coordinate and top z-coordinate from the center of each well.
            adjusted_location_top = center_location.move(types.Point(x_pos, y_pos_high, z_pos_high))
            # Move to top y-coordinate and top z-coordinate from the center of each well.
            p1000_s.move_to(adjusted_location_top)
            # Dispense fresh media 2000uL/well
            p1000_s.dispense(1000)
            p1000_s.blow_out()
    p1000_s.drop_tip()

    # Protocol Completed!
    protocol.comment("Protocol completed!")
    # Turn off robot rail lights
    protocol.set_rail_lights(False)
