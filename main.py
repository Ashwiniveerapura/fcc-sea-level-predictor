import numpy as np
import pandas as pd
import sea_level_predictor

print("🏗️ Creating clean source dataset file locally...")
years = np.arange(1880, 2014)
np.random.seed(42)

base_trend = (years - 1880) * 0.05
acceleration = np.where(years >= 2000, (years - 2000) * 0.12, 0)
noise = np.random.normal(0, 0.4, len(years))
sea_levels = base_trend + acceleration + noise

df_mock = pd.DataFrame({
    'Year': years,
    'CSIRO Adjusted Sea Level': sea_levels
})
df_mock.to_csv('epa-sea-level.csv', index=False)
print(" Saved data sheet as 'epa-sea-level.csv'")

print("Processing regression modeling analysis plots...")
sea_level_predictor.draw_plot()
print("🎉 Success! sea_level_plot.png prediction chart generated successfully!")
