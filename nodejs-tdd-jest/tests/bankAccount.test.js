const { BankAccount, InsufficientFundsError } = require('../src/bankAccount');

describe('BankAccount', () => {
  let account;

  beforeEach(() => {
    account = new BankAccount(100);
  });

  describe('constructor', () => {
    test('should set initial balance correctly', () => {
      const newAccount = new BankAccount(50);
      expect(newAccount.balance).toBe(50);
    });

    test('should default to zero balance', () => {
      const newAccount = new BankAccount();
      expect(newAccount.balance).toBe(0);
    });

    test('should be instance of BankAccount', () => {
      expect(account).toBeInstanceOf(BankAccount);
    });
  });

  describe('deposit', () => {
    test('should increase balance with positive amount', () => {
      account.deposit(50);
      expect(account.balance).toBe(150);
    });

    test('should not change balance when depositing zero', () => {
      const originalBalance = account.balance;
      account.deposit(0);
      expect(account.balance).toBe(originalBalance);
    });

    test('should throw error for negative deposit', () => {
      expect(() => {
        account.deposit(-10);
      }).toThrow('Deposit amount must be positive');
    });

    test('should handle decimal deposits', () => {
      account.deposit(25.50);
      expect(account.balance).toBeCloseTo(125.50);
    });

    test('should handle very large deposits', () => {
      account.deposit(1000000);
      expect(account.balance).toBe(1000100);
    });
  });

  describe('withdraw', () => {
    test('should decrease balance with valid amount', () => {
      account.withdraw(30);
      expect(account.balance).toBe(70);
    });

    test('should allow withdrawing exact balance', () => {
      account.withdraw(100);
      expect(account.balance).toBe(0);
    });

    test('should throw InsufficientFundsError when withdrawing more than balance', () => {
      expect(() => {
        account.withdraw(150);
      }).toThrow(InsufficientFundsError);
      
      expect(() => {
        account.withdraw(150);
      }).toThrow('Insufficient funds');
    });

    test('should throw error for negative withdrawal', () => {
      expect(() => {
        account.withdraw(-10);
      }).toThrow('Withdrawal amount must be positive');
    });

    test('should not change balance when withdrawing zero', () => {
      const originalBalance = account.balance;
      account.withdraw(0);
      expect(account.balance).toBe(originalBalance);
    });

    test('should handle decimal withdrawals', () => {
      account.withdraw(25.50);
      expect(account.balance).toBeCloseTo(74.50);
    });
  });

  describe('getBalance', () => {
    test('should return current balance', () => {
      expect(account.getBalance()).toBe(100);
      account.deposit(25);
      expect(account.getBalance()).toBe(125);
    });

    test('should return balance as number', () => {
      const balance = account.getBalance();
      expect(typeof balance).toBe('number');
    });
  });

  describe('multiple transactions', () => {
    test('should handle series of deposits and withdrawals', () => {
      account.deposit(50);   // 150
      account.withdraw(30);  // 120
      account.deposit(10);   // 130
      account.withdraw(25);  // 105
      expect(account.balance).toBe(105);
    });

    test('should maintain accurate balance through complex operations', () => {
      account.deposit(123.45);
      account.withdraw(23.45);
      account.deposit(0.55);
      expect(account.balance).toBeCloseTo(200.55);
    });
  });

  describe('edge cases', () => {
    test('should handle very small amounts', () => {
      const smallAccount = new BankAccount(0.01);
      smallAccount.deposit(0.01);
      expect(smallAccount.balance).toBeCloseTo(0.02);
    });

    test('should handle floating point precision', () => {
      const precisionAccount = new BankAccount(0.1);
      precisionAccount.deposit(0.2);
      expect(precisionAccount.balance).toBeCloseTo(0.3);
    });
  });
});

describe('InsufficientFundsError', () => {
  test('should be instance of Error', () => {
    const error = new InsufficientFundsError('Test message');
    expect(error).toBeInstanceOf(Error);
    expect(error).toBeInstanceOf(InsufficientFundsError);
  });

  test('should preserve error message', () => {
    const message = 'Custom insufficient funds message';
    const error = new InsufficientFundsError(message);
    expect(error.message).toBe(message);
  });
});