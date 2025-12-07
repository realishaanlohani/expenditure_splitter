# expenditure_splitter
## Description

Expense Manager is a basic command line tool designed to simplify tracking shared expenses within a group. It allows users to easily record payments, maintain a list of participants, and automatically calculate an equal way to settle debts, ensuring everyone pays their part of the payment.

## Features

  * **Adding people:** Add and manage multiple accounts.
  * **Execute expenses:** Record shared expenses with details on the payer, amount, and description.
  * **Autocheck Balances:** Instantly calculates who owes whom to settle all debts.
  * **Persistent Storage:** Automatically saves and loads data so records are never lost.

## How It Works

The application runs locally in your terminal. When you add a person or an expense, the data is validated and immediately written to a local file. To determine settlements, the program sums the total expenses, calculates the average cost per person, and compares each individual's contribution against that average to generate a list of "who owes whom."

## Usage

1. Git clone the repo
   ```bash
   git clone https://github.com/realishaanlohani/expenditure_splitter/
   ```
2. Enter the folder
   ```bash
   cd expenditure_splitter
   ```
   
3.  **Run the application:**
    Open your terminal or command prompt and run the script:

    ```bash
    python main.py
    ```

4.  **Follow the menu prompts:**

      * Select **Add Person** to add a new group member.
      * Select **Add Expense** to log a paymentwith a description.
      * Select **Calculate Balances** to see the final settlements.

## Data Storage

This project uses **CSV (Comma-Separated Values)** file system to store and manage data. Data is saved to `expenses.csv` (or similar) in the project root. You can open this file in Excel or any text editor to view or back up your raw data!

## Requirements

**Python**

## Notes / Limitations

  * Currently, the logic assumes all expenses are split equally among all participants.
  * Data is stored locally on your machine, therefore is not being stored online.
  * The tool treats all numbers as generic values, and doesn't have currency conversions.
