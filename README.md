# expenditure_splitter

Expense Manager is designed to simplify expenses tracking. It allows users to easily record payments, maintain a list of participants, and automatically calculate an equal way to settle debts, so that everyone pays their part of the payment.

## Features

  * **Adding people:** Add and manage multiple accounts.
  * **Execute expenses:** Record shared expenses with details on the payer, amount, and description.
  * **Checking accounts history:** Instantly calculates who owes whom to settle all debts.
    
## How It Works

The application runs locally in your terminal. When you add a person or an expense, the data is validated and immediately written to a local file. To determine settlements, the program sums the total expenses, calculates the average cost per person, and compares each individual's contribution against that average to generate a list of "who owes whom."

## Use

1. Git clone the repo
   ```bash
   git clone https://github.com/realishaanlohani/expenditure_splitter/
   ```
2. Enter the folder
   ```bash
   cd expenditure_splitter
   ```
   
3.  **Running the application:**
    Open your terminal or command prompt and run the script:

    ```bash
    python main.py
    ```

4.  **Options:**

      * Select **Add Person** to add a new group member.
      * Select **Make Expense** to enter a payment with a description.
      * Select **Calculate Balances** to see the final settlements.

## Transaction History

This project is using CSV file system to store and manage transactions. Data is saved to `bigo.csv` in the project root. You can open this file in Excel or any text editor to view or back up your raw data!

## Requirements

**Python** (any latest version)

## Notes

  * Currently, the logic assumes all expenses are split equally among all participants.
  * Data is stored locally on your machine, therefore is not being stored online.
