## Running the Extension

To run the extension, execute the following command in your terminal:

```bash
python compounds_tracking.py
```

## Testing the Extension

To test the extension, execute the following command in your terminal: 

```bash
python test_compounds_tracking.py
```

### Testing for compound_registration
1. **Registering a Valid Compound**: This test ensures that the system can successfully register a compound with a valid format, denoted by the compound code "MRT-123456".

2. **Registering an Invalid Compound Format**: This test verifies that the system correctly identifies and rejects an attempt to register a compound with an invalid format, such as "InvalidFormat".

3. **Registering a Duplicate Compound**: This test evaluates the system's behavior when attempting to register a compound that has already been registered. It confirms that the system correctly identifies duplicates and prevents redundant registrations.

### Testing for compound_assignment
1. **Assigning a Valid Compound to a Valid Well ID**: 
   This test verifies that the system can successfully assign a compound with a valid format (e.g., "MRT-123456") to a well identified by a valid well ID (e.g., "A1").

2. **Assigning an Invalid Compound to a Valid Well ID**: 
   This test ensures that the system correctly handles the scenario where an attempt is made to assign an invalid compound format to a valid well ID.

3. **Assigning a Valid Compound to an Invalid Well ID**: 
   This test checks the system's behavior when attempting to assign a compound with a valid format (e.g., "MRT-123456") to an invalid well ID format (e.g., "InvalidFormat").

4. **Assigning a Non-Registered Compound**: 
   This test validates the system's response when trying to assign a compound that has not been registered to a well ID.

5. **Assigning a Duplicate Compound**: 
   This test verifies that the system correctly handles the situation where an attempt is made to assign a duplicate compound to a well ID that already contains the same compound.

### Testing for well_copy
1. **Copying Well from Another Well**: 
   This test ensures that the system can successfully copy compounds from one well to another. It registers several compounds, assigns them to different wells, and then copies the compounds from one well ("A1") to another ("B2"). The test validates that the operation completes successfully.

2. **Copying from an Invalid Source Well**: 
   This test verifies the system's behavior when attempting to copy compounds from an invalid source well. It attempts to copy compounds from a well identified by an invalid format to another valid well. The test ensures that the system handles this scenario correctly and returns a failure.

3. **Copying from an Empty Source Well**: 
   This test checks how the system behaves when attempting to copy compounds from an empty source well ("A1") to a valid destination well ("B1"). The test expects the operation to fail and verifies that the system handles empty wells appropriately.

### Testing for get_compounds_from_well
1. **Getting All Compounds from a Valid Well**: 
   This test verifies that the system can retrieve all compounds assigned to a valid well ("A1"). It registers two compounds ("MRT-123456" and "MRT-123457"), assigns them to the same well, and then retrieves the compounds from that well. The test expects the system to return the list of compounds ["MRT-123456", "MRT-123457"].

2. **Getting All Compounds from an Invalid Well**: 
   This test checks the system's behavior when attempting to retrieve compounds from an invalid well. It expects the system to handle this scenario gracefully and return an empty list.

3. **Getting All Compounds from an Empty Well**: 
   This test ensures that the system correctly handles the case where an attempt is made to retrieve compounds from an empty well ("A1"). It expects the system to return an empty list, indicating that there are no compounds assigned to the specified well.

### Testing for get_compounds_from_plate
1. **Getting Compounds from a Plate**: 
   This test ensures that the system can retrieve all compounds from a plate. It registers four compounds ("MRT-123456", "MRT-123457", "MRT-123458", and "MRT-123459") and assigns them to different wells on the plate. It then retrieves all compounds from the plate and expects the system to return the list ["MRT-123456", "MRT-123457", "MRT-123458", "MRT-123459"].

2. **Getting Compounds from an Empty Plate**: 
   This test verifies the system's behavior when attempting to retrieve compounds from an empty plate. It expects the system to return an empty list, indicating that there are no compounds assigned to any well on the plate.

## Assumption of the Extension
1. **Assumption 1**: All inputs(compound and well id) will be string.

2. **Assumption 2**: There is no capacity limitation for compound registration.

3. **Assumption 3**: The format of well_id follows the pattern of an uppercase letter followed by an integer greater than 0. Besides this format requirement, there are no other limitations imposed.

4. **Assumption 4**: A given compound cannot be simultaneously added to two different wells.

5. **Assumption 7**: The system assumes that there is a one-to-many relationship between wells and compounds, meaning that a single well can contain multiple compounds.

6. **Assumption 8**: The system assumes that compounds are uniquely identified by their compound codes. Duplicate compound codes are not allowed.

## Design of the Extension

### Data Structure Selection

1. **Compound Registration**: Utilizes the `Set` data structure to store registered compounds. Sets offer fast lookup operations, ensuring uniqueness of each compound, with a registration process time complexity of O(1).

2. **Well Assignment**: Implements the functionality of assigning compounds to wells using the `Map` data structure. Well IDs serve as keys, with the associated set of compounds for each well serving as values. This design allows for quick assignment of compounds to wells and retrieval of all compounds in a specific well when needed, while maintaining compound uniqueness.

### System Features
1. The system defaults to returning boolean values alongside output messages for compound registration and well assignment operations.

2. The system checks the validity of input.

