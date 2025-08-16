import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from bank_account import BankAccount, InsufficientFundsError


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(initial_balance=100)

    def test_initial_balance_is_set_correctly(self):
        account = BankAccount(initial_balance=50)
        self.assertEqual(account.balance, 50)

    def test_default_initial_balance_is_zero(self):
        account = BankAccount()
        self.assertEqual(account.balance, 0)

    def test_deposit_positive_amount_increases_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_zero_does_not_change_balance(self):
        original_balance = self.account.balance
        self.account.deposit(0)
        self.assertEqual(self.account.balance, original_balance)

    def test_deposit_negative_amount_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-10)
        self.assertIn("Deposit amount must be positive", str(context.exception))

    def test_withdraw_valid_amount_decreases_balance(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_withdraw_exact_balance_leaves_zero_balance(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 0)

    def test_withdraw_more_than_balance_raises_insufficient_funds_error(self):
        with self.assertRaises(InsufficientFundsError) as context:
            self.account.withdraw(150)
        self.assertIn("Insufficient funds", str(context.exception))

    def test_withdraw_negative_amount_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-10)
        self.assertIn("Withdrawal amount must be positive", str(context.exception))

    def test_withdraw_zero_does_not_change_balance(self):
        original_balance = self.account.balance
        self.account.withdraw(0)
        self.assertEqual(self.account.balance, original_balance)

    def test_get_balance_returns_current_balance(self):
        self.assertEqual(self.account.get_balance(), 100)
        self.account.deposit(25)
        self.assertEqual(self.account.get_balance(), 125)

    def test_multiple_transactions(self):
        self.account.deposit(50)   # 150
        self.account.withdraw(30)  # 120
        self.account.deposit(10)   # 130
        self.account.withdraw(25)  # 105
        self.assertEqual(self.account.balance, 105)

    def test_bank_account_instance_creation(self):
        account = BankAccount()
        self.assertIsInstance(account, BankAccount)

    def test_balance_is_numeric(self):
        self.assertIsInstance(self.account.balance, (int, float))

    def test_large_deposit(self):
        self.account.deposit(1000000)
        self.assertEqual(self.account.balance, 1000100)

    def test_insufficient_funds_error_inheritance(self):
        self.assertTrue(issubclass(InsufficientFundsError, Exception))

    def tearDown(self):
        # Clean up after each test if needed
        pass


class TestBankAccountEdgeCases(unittest.TestCase):
    def test_very_small_amounts(self):
        account = BankAccount(0.01)
        account.deposit(0.01)
        self.assertAlmostEqual(account.balance, 0.02, places=2)

    def test_floating_point_precision(self):
        account = BankAccount(0.1)
        account.deposit(0.2)
        # Using assertAlmostEqual for floating point comparisons
        self.assertAlmostEqual(account.balance, 0.3, places=7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
