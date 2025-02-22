import random

def energy_distribution(demand, solar, wind, tidal):
    total_supply = solar + wind + tidal
    shortfall = demand - total_supply

    if shortfall > 0:
        print(f"Energy Deficit: {shortfall} kW - Need backup power!")
    else:
        print(f"Energy Balanced! Surplus: {-shortfall} kW")

# Example: 5000 kW demand, 2000 kW solar, 1500 kW wind, 1800 kW tidal
energy_distribution(5000, 2000, 1500, 1800)
