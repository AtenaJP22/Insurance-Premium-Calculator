import unittest
from hw1_2101183 import Customer, LifePolicy, AutoPolicy, HealthPolicy

class TestPolicies(unittest.TestCase):

    #Testing the premium calculation for each policy
    def test_life_policy_premium(self):
        policy = LifePolicy(base_premium=100, coverage_amount=500000)
        premium = policy.calculate_premium(age=70)
        self.assertAlmostEqual(premium, 6630.0, places=2)

    def test_auto_policy_premium(self):
        policy = AutoPolicy(base_premium=200, driving_record="major", vehicle_type="SUV")
        premium = policy.calculate_premium(age=30)
        self.assertAlmostEqual(premium, 560.0, places=2)

    def test_health_policy_premium(self):
        policy = HealthPolicy(base_premium=100, has_medical_conditions=True)
        premium = policy.calculate_premium(age=30)
        self.assertAlmostEqual(premium, 130.0, places=2)

    #Testing the addition of a policy to a customer
    def test_add_policy_to_customer(self):
        customer = Customer(name="Alice", age=45, address="123 Maple Street")
        policy = LifePolicy(base_premium=100, coverage_amount=500000)
        customer.add_policy(policy)
        self.assertEqual(len(customer.past_policies), 1)
        self.assertEqual(customer.past_policies[0], policy)

    #Now testing customer info update
    def test_update_address(self):
        customer = Customer(name="Alice", age=45, address="123 Maple Street")
        customer.update_customer_info(address="456 Oak Avenue")
        self.assertEqual(customer.address, "456 Oak Avenue")
    def test_update_age(self):
        customer = Customer(name="Alice", age=45, address="123 Maple Street")
        customer.update_customer_info(age=50)
        self.assertEqual(customer.age, 50)
    def test_update_name(self):
        customer = Customer(name="Alice", age=45, address="123 Maple Street")
        customer.update_customer_info(name="Bob")
        self.assertEqual(customer.name, "Bob")
        
    def test_update_all(self):
        customer = Customer(name="Alice", age=45, address="123 Maple Street")
        customer.update_customer_info(name="Bob", age=50, address="456 Oak Avenue")
        self.assertEqual(customer.name, "Bob")
        self.assertEqual(customer.age, 50)
        self.assertEqual(customer.address, "456 Oak Avenue")
        
    #Testing the removal of a policy
    def test_remove_policy(self):
        customer2 = Customer(name="Jane", age=35, address="321 Pine Street")
        policy = LifePolicy(base_premium=100, coverage_amount=500000)
        customer2.add_policy(policy)
        customer2.remove_policy(2)
        self.assertEqual(len(customer2.past_policies), 1)#1 because the customer named Bob (whose initial name was Alice) has an existing policy and-
        #-we added a new one in this test case, so after "Jane" is removed, only "Bob" remains.

    # Testing the generation of a quote with various policies
    def test_generate_quote(self):
        customer = Customer(name="Amy", age=45, address="220 Sunshine Street")
        
        # Test with a standard policy
        policy1 = LifePolicy(base_premium=100, coverage_amount=500000)
        quote1 = customer.generate_quote(policy1)
        self.assertEqual(quote1, 5100.0)
        
        # Test with a higher base premium
        policy2 = LifePolicy(base_premium=200, coverage_amount=500000)
        quote2 = customer.generate_quote(policy2)
        self.assertEqual(quote2, 5200.0)
        
        # Test with a higher coverage amount
        policy3 = LifePolicy(base_premium=100, coverage_amount=1000000)
        quote3 = customer.generate_quote(policy3)
        self.assertEqual(quote3, 10100.0)
        
        # Test with minimum values
        policy4 = LifePolicy(base_premium=0, coverage_amount=0)
        quote4 = customer.generate_quote(policy4)
        self.assertEqual(quote4, 0.0)
        
        # Test with maximum values (assuming some reasonable max values)
        policy5 = LifePolicy(base_premium=1000, coverage_amount=10000000)
        quote5 = customer.generate_quote(policy5)
        self.assertEqual(quote5, 101000.0)
    
        #Testing viewing past policies
        def test_view_past_policies(self):
            customer = Customer(name="Austin", age=55, address="322 West Street")
            policy = LifePolicy(base_premium=100, coverage_amount=500000)
            customer.add_policy(policy)
            self.assertEqual(customer.view_past_policies(), policy)
    
if __name__ == '__main__':
    unittest.main()