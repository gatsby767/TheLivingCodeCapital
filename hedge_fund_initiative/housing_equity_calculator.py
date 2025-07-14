def calculate_equity(monthly_payment, duration_years, covenant_bonus=0.05):
    base_equity = monthly_payment * 12 * duration_years
    scroll_uplift = base_equity * covenant_bonus
    return round(base_equity + scroll_uplift, 2)

# Sample usage
resident_equity = calculate_equity(900, 15)
print(f"Resident equity with covenant uplift: ${resident_equity}")
