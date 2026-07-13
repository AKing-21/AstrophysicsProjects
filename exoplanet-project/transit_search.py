import lightkurve as lk
import matplotlib.pyplot as plt

print("Searching NASA archives for Kepler-10...")
search_result = lk.search_lightcurve('Kepler-10', author='Kepler', quarter=3)

print("Downloading data... This might take a moment.")
lc = search_result.download()

print("Cleaning data pipelines...")
clean_lc = lc.remove_nans().remove_outliers()

flat_lc = clean_lc.flatten(window_length=401)

folded_lc = flat_lc.fold(period=0.837495)

print("Generating light curve graph...")
fig, ax = plt.subplots(figsize=(10, 6))

folded_lc.scatter(ax=ax, color='royalblue', alpha=0.3, label='Raw Data Points')

folded_lc.bin(time_bin_size=0.01).plot(ax=ax, color='crimson', lw=2, label='Binned Average')

ax.set_title('Exoplanet Transit Detection: Kepler-10b', fontsize=14, fontweight='bold')
ax.set_xlabel('Time Since Transit Midpoint (Days)', fontsize=12)
ax.set_ylabel('Normalized Star Brightness (Flux)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(fontsize=11)

plt.savefig('kepler10b_transit.png', dpi=300)
print("Your plot has been saved as 'kepler10b_transit.png'")
plt.show()