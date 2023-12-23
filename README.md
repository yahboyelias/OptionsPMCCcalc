# OptionsPMCCcalc
A "poor man's covered call" is an options strategy where you buy a longer-term call option and sell a shorter-term call option with the same strike price. It aims to replicate the potential gains of a covered call strategy but with reduced upfront costs, enabling participation in stock price increases with less capital.

This calculator helps evaluate your position's value, break-even point, and potential profitability within a four-week timeframe based on specific mathematical inputs.

# Poor Mans Covered Call Calculator

This Python script serves as a simple options calculator, allowing users to calculate various metrics related to options trading via the terminal/command line interface.

## Prerequisites

- Python 3.x installed

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/yahboyelias/OptionsPMCCcalc.git
    ```

2. Navigate to the project directory:
    ```bash
    cd options-calculator
    ```

3. Run the script:
    ```bash
    python OptionsPMCCCalc.py
    ```

4. Follow the prompts and enter the required information to calculate options-related metrics.

## Usage

- Upon running the script, you'll be prompted to input the following details:
    - Strike price of the long call
    - Strike price of the short call
    - Value of the long call
    - Value of the short call

- The script will perform calculations based on the provided inputs and display metrics such as intrinsic value, break-even point, potential profits, etc.
