bracket_rate = [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
bracket_type = [
    [22000, 89450, 190750, 364200, 462500, 693750],  # joint
    [15700, 59850, 95350, 182100, 231250, 578100],  # head
    [11000, 44725, 95375, 182100, 231250, 578125],  # single

]
print("Tax Calculation\n---------------------------------")
print(
    """Filing Status \n 
    1 - Married Filling Jointly or Qualifying Surviving Spouse
    2 - Head of Household
    3 - Single or Married Filing Seperately\n"""
)


def calculate_tax():

    filingStatus = inputHandlerFiling("Input the number in Filing Status: ")

    if filingStatus == 1:
        standardDeduction = float(27700)
        bracket = bracket_type[0]
    elif filingStatus == 2:
        standardDeduction = float(20800)
        bracket = bracket_type[1]
    elif filingStatus == 3:
        standardDeduction = float(13850)
        bracket = bracket_type[2]

    annualIncome = inputHandlerIncome("Annual Income: $")
    adjustments = inputHandlerIncome("Adjustments: -$")
    adjustedGrossIncome = annualIncome - adjustments
    taxableIncome = adjustedGrossIncome - standardDeduction

    print("Adjusted Gross Income: ", "${0:.2f}".format(adjustedGrossIncome))
    print("Standard Deduction: -", "${0:.2f}".format(standardDeduction))
    print("Taxable Income:", "${0:.2f}".format(taxableIncome))

    totalTaxLiability = 0
    prevVal = 0
    i = 0
    print("Tax Brackets Applied: ")
    for tax_type in bracket:
        currVal = tax_type - prevVal
        taxPercentage = bracket_rate[i] * (tax_type - prevVal)
        if taxableIncome <= tax_type:
            lastVal = taxableIncome - prevVal
            lastTax = bracket_rate[i]
            lastTaxPercentage = bracket_rate[i] * (lastVal)
            break
        totalTaxLiability += bracket_rate[i] * (tax_type - prevVal)
        prevVal = tax_type
        print(
            str(int(bracket_rate[i] * 100)) + "% on the next",
            currVal,
            ":",
            "${0:.2f}".format(taxPercentage),
        )
        i += 1

    totalTaxLiability += bracket_rate[i] * (taxableIncome - prevVal)
    print(
        str(int(lastTax * 100)) + "% on the next",
        lastVal,
        ":",
        "${0:.2f}".format(lastTaxPercentage),
    )

    print("Total Tax Liability:", "${0:.2f}".format(totalTaxLiability))

    federalTax = inputHandlerIncome("Federal Tax Withheld: $")

    refundOwed = federalTax - totalTaxLiability
    print("Refund Owed:", "${0:.2f}".format(refundOwed))


def inputHandlerFiling(txt):
    while True:
        try:
            inputFiling = float((input(txt)))
        except ValueError:
            print("Please input a number")
            continue
        if inputFiling > 3:
            print("Invalid number")
        else:
            break
    return inputFiling


def inputHandlerIncome(txt):
    while True:
        try:
            incomeInput = float((input(txt)))
        except ValueError:
            print("Please input a number and no comma")
            continue
        if incomeInput < 0:
            print("Invalid number")
        elif len(str(incomeInput)) > 9:
            print("Please input realistic number")
        else:
            break
    return incomeInput


if __name__ == "__main__":
    calculate_tax()
