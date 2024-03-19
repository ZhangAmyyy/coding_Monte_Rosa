import unittest
from compounds_tracking import reset_global_variables, compound_registration, assign_compound_to_well, copy_well, get_compounds_from_well, get_compounds_from_plate

class TestCompoundsTracking(unittest.TestCase):

    def setUp(self):
        reset_global_variables()

    def test_compound_registration_valid(self):
        #Test1 test for register a valid compound
        print("===================Test: register a valid compound===================")
        self.assertTrue(compound_registration("MRT-123456"))

    def test_compound_register_invalid_format(self):
        print("===================Test: register an invalid compound===================")
        self.assertFalse(compound_registration("InvalidFormat"))

    def test_compound_register_duplicate(self):
        print("===================Test: register a duplicate compound===================")
        compound_registration("MRT-123456")
        self.assertFalse(compound_registration("MRT-123456"))

    def test_assign_compound_to_well_valid(self):
        print("===================Test: assign a valid compound to a valid well id===================")
        compound_registration("MRT-123456")
        self.assertTrue(assign_compound_to_well("MRT-123456", "A1"))

    def test_assign_compound_to_well_invalid_compound_format(self):
        print("===================Test: assign an invalid compound to a valid well id===================")
        self.assertFalse(assign_compound_to_well("InvalidFormat", "A1"))
    
    def test_assign_compound_to_well_invalid_well_format(self):
        print("===================Test: assign a valid compound to an invalid well id===================")
        compound_registration("MRT-123456")
        self.assertFalse(assign_compound_to_well("MRT-123456","InvalidFormat"))

    def test_assign_compound_to_well_compound_not_registered(self):
        print("===================Test: assign a non-registered compound===================")
        self.assertFalse(assign_compound_to_well("MRT-123456", "A1"))
    
    def test_assign_compound_to_well_duplicate_registered(self):
        print("===================Test: assign a duplicate compound===================")
        compound_registration("MRT-123456")
        assign_compound_to_well("MRT-123456", "A1")
        self.assertFalse(assign_compound_to_well("MRT-123456", "A1"))

    def test_copy_well_valid(self):
        print("===================Test: copy well from another well===================")
        compound_registration("MRT-123456")
        assign_compound_to_well("MRT-123456", "A1")
        compound_registration("MRT-123457")
        compound_registration("MRT-123458")
        compound_registration("MRT-123459")
        assign_compound_to_well("MRT-123457", "B2")
        assign_compound_to_well("MRT-123458", "B2")
        assign_compound_to_well("MRT-123459", "B2")
        self.assertTrue(copy_well("A1", "B2"))
    
    def test_copy_well_valid(self):
        print("===================Test: copy invalid well===================")
        self.assertFalse(copy_well("InvalidFormat", "B2"))

    def test_copy_well_empty_source_well(self):
        print("===================Test: copy empty well===================")
        self.assertFalse(copy_well("A1", "B1"))

    def test_get_compounds_from_well_valid(self):
        print("===================Test: get all compounds from a valid well===================")
        compound_registration("MRT-123456")
        assign_compound_to_well("MRT-123456", "A1")
        compound_registration("MRT-123457")
        assign_compound_to_well("MRT-123457", "A1")
        self.assertEqual(get_compounds_from_well("A1"), ["MRT-123456","MRT-123457"])
    
    def test_get_compounds_from_well_invalid_format(self):
        print("===================Test: get all compounds from an invalid well===================")
        self.assertEqual(get_compounds_from_well("InvalidFormat"), [])
    
    def test_get_compounds_from_well_empty_well(self):
        print("===================Test: get all compounds from an invalid well===================")
        self.assertEqual(get_compounds_from_well("A1"), [])

    def test_get_compounds_from_plate_valid(self):
        print("===================Test: get compounds from a plate===================")
        compound_registration("MRT-123456")
        compound_registration("MRT-123457")
        assign_compound_to_well("MRT-123456", "A1")
        assign_compound_to_well("MRT-123457", "A1")
        compound_registration("MRT-123458")
        compound_registration("MRT-123459")
        assign_compound_to_well("MRT-123457", "B2")
        assign_compound_to_well("MRT-123458", "B2")
        assign_compound_to_well("MRT-123459", "B2")
        self.assertEqual(get_compounds_from_plate(), ["MRT-123456","MRT-123457","MRT-123458","MRT-123459"])

    def test_get_compounds_from_plate_empty(self):
        print("===================Test: get compounds from an empty plate===================")
        self.assertEqual(get_compounds_from_plate(), [])

if __name__ == '__main__':
    unittest.main()
