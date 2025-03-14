import numpy as np

np.random.seed(42)
rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0

rainy_days = np.sum(rainfall > 0)

heavy_rain_days = np.sum(rainfall > 5)
heavy_rain_percentage = (heavy_rain_days / 365) * 100

dry_days = (rainfall == 0).astype(int)
dry_spell_lengths = np.diff(np.where(np.concatenate(([0], dry_days, [0])))[0])
longest_dry_spell = np.max(dry_spell_lengths - 1)

print("Number of Rainy Days:", rainy_days)
print("Percentage of Heavy Rain Days:", heavy_rain_percentage)
print("Longest Dry Spell:", longest_dry_spell)
