import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from bank_account import BankAccount, InsufficientFundsError


class TestBankAccount:
    def setup_method(self):
        self.account = BankAccount(initial_balance=100)

    def test_initial_balance_is_set_correctly(self):
        account = BankAccount(initial_balance=50)
        assert account.balance == 50

    def test_default_initial_balance_is_zero(self):
        account = BankAccount()
        assert account.balance == 0

    def test_deposit_positive_amount_increases_balance(self):
        self.account.deposit(50)
        assert self.account.balance == 150

    def test_deposit_zero_does_not_change_balance(self):
        original_balance = self.account.balance
        self.account.deposit(0)
        assert self.account.balance == original_balance

    def test_deposit_negative_amount_raises_exception(self):
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            self.account.deposit(-10)

    def test_withdraw_valid_amount_decreases_balance(self):
        self.account.withdraw(30)
        assert self.account.balance == 70

    def test_withdraw_exact_balance_leaves_zero_balance(self):
        self.account.withdraw(100)
        assert self.account.balance == 0

    def test_withdraw_more_than_balance_raises_insufficient_funds_error(self):
        with pytest.raises(InsufficientFundsError, match="Insufficient funds"):
            self.account.withdraw(150)

    def test_withdraw_negative_amount_raises_exception(self):
        with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
            self.account.withdraw(-10)

    def test_withdraw_zero_does_not_change_balance(self):
        original_balance = self.account.balance
        self.account.withdraw(0)
        assert self.account.balance == original_balance

    def test_get_balance_returns_current_balance(self):
        assert self.account.get_balance() == 100
        self.account.deposit(25)
        assert self.account.get_balance() == 125

    def test_multiple_transactions(self):
        self.account.deposit(50)   # 150
        self.account.withdraw(30)  # 120
        self.account.deposit(10)   # 130
        self.account.withdraw(25)  # 105
        assert self.account.balance == 105
