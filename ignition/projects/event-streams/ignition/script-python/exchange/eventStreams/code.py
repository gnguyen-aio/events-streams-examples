def eventStreamsSim():
    """
    Simulates a material mixing process by manipulating inventory and mixer tags.
    
    This function acts as a state machine based on the 'Process Step' tag:
        0: Reset - Refills inventories and clears the mixer.
        1: Fill - Decrements bean/rice inventory and increments mixer weight.
        2: Mix - Holds values and caps the mixer weight at 200.
        3: Empty - Decrements mixer weight (discharge phase).
    """
    # Define the base path for the process step control tag
    processStepPath = '[default]Exchange/event-streams/simulator/Process Step'
    processStep = system.tag.readBlocking([processStepPath])[0].value
    
    # Define paths for the process value tags (Inventory and Mixer)
    beanPath = '[default]Exchange/event-streams/simulator/Process Values/Beans Inventory'
    ricePath = '[default]Exchange/event-streams/simulator/Process Values/Rice Inventory'
    mixerWeightPath = '[default]Exchange/event-streams/simulator/Process Values/Mixer Weight'
    
    # Define paths for the setpoint tags
    beansConveyor = '[default]Exchange/event-streams/simulator/Process Setpoints/Beans Conveyor'
    riceConveyor = '[default]Exchange/event-streams/simulator/Process Setpoints/Rice Conveyor'
    exitValve = '[default]Exchange/event-streams/simulator/Process Setpoints/Exit Valve'
    mixerMotor = '[default]Exchange/event-streams/simulator/Process Setpoints/Mixer Motor'
    
    tagPaths = [beanPath, ricePath, mixerWeightPath, beansConveyor, riceConveyor, exitValve, mixerMotor]
    
    # --- State 0: System Reset/Refill ---
    if processStep == 0:
        # Reset inventory to full (200) and mixer to empty (0)
        tagValues = [200, 200, 0, 0, 0, 0, 0]
        system.tag.writeBlocking(tagPaths, tagValues)
        
    # --- State 1: Filling Phase ---
    elif processStep == 1:
        # Read current values to calculate the next delta
        currentValues = system.tag.readBlocking(tagPaths)
        
        # Logic: Pull 6 beans and 4 rice, add 7 to mixer weight
        beanValue = currentValues[0].value - 6
        riceValue = currentValues[1].value - 4
        mixerValue = currentValues[2].value + 7
        beansConveyorValue = 60
        riceConveyorValue = 60
        exitValveValue = 0
        mixerMotorValue = 0
        
        # Check for empty inventory and refill if necessary to keep sim running
        if beanValue < 0:
            beanValue = 200
        if riceValue < 0:
            riceValue = 200
            
        tagValues = [beanValue, riceValue, mixerValue, beansConveyorValue, riceConveyorValue, exitValveValue, mixerMotorValue]
        system.tag.writeBlocking(tagPaths, tagValues)
        
    # --- State 2: Mixing Phase ---
    elif processStep == 2:
        # Read current state
        currentValues = system.tag.readBlocking(tagPaths)
        beanValue = currentValues[0].value
        riceValue = currentValues[1].value
        mixerValue = currentValues[2].value
        beansConveyorValue = 0
        riceConveyorValue = 0
        exitValveValue = 0
        mixerMotorValue = 45
        
        # Cap the mixer weight at 200 during the mixing cycle
        if mixerValue > 200:
            mixerValue = 200
            
        tagValues = [beanValue, riceValue, mixerValue, beansConveyorValue, riceConveyorValue, exitValveValue, mixerMotorValue]
        system.tag.writeBlocking(tagPaths, tagValues)
        
    # --- State 3: Emptying/Discharge Phase ---
    elif processStep == 3:
        # Read current state
        currentValues = system.tag.readBlocking(tagPaths)
        
        # Logic: Discharge 33 units from the mixer
        mixerValue = currentValues[2].value - 33
        beansConveyorValue = 0
        riceConveyorValue = 0
        exitValveValue = 1
        mixerMotorValue = 0
        
        # Ensure mixer weight doesn't drop below zero
        if mixerValue < 0:
            mixerValue = 0
        
        # Maintain bean/rice levels while updating mixer weight
        tagValues = [currentValues[0].value, currentValues[1].value, mixerValue, beansConveyorValue, riceConveyorValue, exitValveValue, mixerMotorValue]
        system.tag.writeBlocking(tagPaths, tagValues)
        
    else:
        # Handle undefined process steps
        pass
    
    return