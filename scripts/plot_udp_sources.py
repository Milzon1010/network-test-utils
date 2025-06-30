import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("output/parsed_udp_packets.csv")

# Hitung 10 IP sumber terbanyak
top_src_ips = df['src_ip'].value_counts().head(10)

# Plot
plt.figure(figsize=(10, 6))
top_src_ips.plot(kind='bar')
plt.title("Top 10 UDP Source IPs")
plt.xlabel("Source IP")
plt.ylabel("Packet Count")
plt.xticks(rotation=45)
plt.tight_layout()

# Simpan ke file
os.makedirs("viz", exist_ok=True)
plt.savefig("viz/top_udp_sources.png")
plt.show()
