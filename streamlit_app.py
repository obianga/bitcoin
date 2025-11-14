import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="AIL-2045 Crypto Finance Calculator", layout="wide")
st.title("AIL-2045 Bitcoin & Crypto Financing Model")
st.markdown("### Test $4T Industrial Leap with BTC, Bonds, FDI & NFTs (2026–2045)")
st.markdown("**Now with 6 Real AfDB/Afreximbank Projects!**")

# Sidebar Inputs
st.sidebar.header("Model Parameters")
btc_seed = st.sidebar.slider("BTC Reserve Seed ($B)", 10.0, 100.0, 35.0, 5.0)
btc_cagr = st.sidebar.slider("BTC CAGR (%)", 5.0, 25.0, 15.0, 1.0) / 100
years = st.sidebar.slider("Forecast Years", 15, 25, 19)
bond_amount = st.sidebar.slider("Tokenized Bonds ($B)", 50.0, 300.0, 200.0, 25.0)
bond_yield = st.sidebar.slider("Bond Yield (%)", 2.0, 6.0, 4.0, 0.5) / 100
fdi_amount = st.sidebar.slider("Crypto FDI ($B)", 20.0, 100.0, 50.0, 10.0)
nft_amount = st.sidebar.slider("Carbon NFTs ($B)", 5.0, 50.0, 15.0, 5.0)
inflation = st.sidebar.slider("Annual Inflation (%)", 1.0, 10.0, 3.0, 0.5) / 100

# Calculations
btc_final = btc_seed * (1 + btc_cagr) ** years
btc_gain = btc_final - btc_seed
bond_interest = bond_amount * bond_yield * 10
fdi_return = fdi_amount * (1.20 ** 10)
nft_return = nft_amount * (1.12 ** years)
total_unlocked = btc_final + bond_interest + fdi_return + nft_return
gap_covered = min(total_unlocked / 1.5, 1.0)
roi_crypto = ((total_unlocked - (btc_seed + bond_amount + fdi_amount + nft_amount)) / (btc_seed + bond_amount + fdi_amount + nft_amount)) * 100

# Traditional
trad_cost = (bond_amount * 0.07 * 10) + (fdi_amount * 0.08 * 10) + (btc_seed * 0.03 * years)
savings = (bond_interest + fdi_return + btc_gain + nft_return) - trad_cost
jobs = int(total_unlocked * 100_000)

# Dashboard
col1, col2 = st.columns(2)
with col1:
    st.metric("BTC Value in 2045", f"${btc_final:.1f}B", f"+${btc_gain:.1f}B")
    st.metric("Total Unlocked Capital", f"${total_unlocked:.1f}B")
    st.metric("Financing Gap Covered", f"{gap_covered:.1%}")
with col2:
    st.metric("Crypto ROI (20Y)", f"{roi_crypto:.1f}%")
    st.metric("Savings vs. Traditional", f"${savings:.1f}B")
    st.metric("Jobs Created", f"{jobs:,}")

# Chart
years_list = list(range(2026, 2026 + years))
btc_curve = [btc_seed * (1 + btc_cagr) ** i for i in range(years)]
fig, ax = plt.subplots()
ax.plot(years_list, btc_curve, label="BTC Reserve", color="#F7931A")
ax.axhline(1500, color="red", linestyle="--", label="$1.5T Gap")
ax.set_title("BTC Appreciation vs. Financing Gap")
ax.set_ylabel("$ Billion")
ax.legend()
st.pyplot(fig)

# === NEW: 6 PROJECT PILOTS ===
st.subheader("Pilot: Apply to Real AIL Projects (AfDB + Afreximbank)")
proj = st.selectbox("Choose Project", [
    "LAPSSET Corridor ($1.2B)",
    "Rufiji Hydro Dam ($0.5B)",
    "Eastern Angola Agri ($211M) - NEW",
    "Egypt Pharma Biosimilars ($746M) - NEW",
    "Nacala Corridor Rail/Port ($2.7B) - NEW",
    "Nigeria Export Mfg Zones ($300M+) - NEW"
], key="pilot")

# Pilot Calculations
if proj == "LAPSSET Corridor ($1.2B)":
    pilot_btc = st.slider("BTC Bond Tranche ($M)", 100, 1000, 500)
    pilot_gain = pilot_btc / 1000 * (1 + btc_cagr) ** years
    st.success(f"**$500M BTC Bond → ${pilot_gain:.1f}B by 2045**")
    st.info("Trade cost -10% by 2030 | +1.2M jobs | **Integrate Africa**")

elif proj == "Rufiji Hydro Dam ($0.5B)":
    pilot_fdi = st.slider("Crypto FDI Tranche ($M)", 50, 500, 200)
    pilot_irr = ((1.22 ** 10) - 1) * 100
    st.success(f"**$200M FDI → 22% IRR | Scales to 100 GW**")
    st.info("500 MW online by 2028 | +0.5M jobs | **Power Africa**")

elif proj == "Eastern Angola Agri ($211M) - NEW":
    pilot_btc = st.slider("BTC Bond Tranche ($M)", 50, 300, 100)
    pilot_gain = pilot_btc / 1000 * (1 + btc_cagr) ** years
    st.success(f"**$100M BTC Bond → ${pilot_gain:.2f}B by 2045**")
    st.info("Lobito Corridor food hub | +300K jobs | **Feed Africa**")

elif proj == "Egypt Pharma Biosimilars ($746M) - NEW":
    pilot_btc = st.slider("BTC Bond Tranche ($M)", 100, 1000, 300)
    pilot_gain = pilot_btc / 1000 * (1 + btc_cagr) ** years
    st.success(f"**$300M BTC Bond → ${pilot_gain:.2f}B by 2045**")
    st.info("Oncology & autoimmune drugs | +800K jobs | **Quality of Life**")

elif proj == "Nacala Corridor Rail/Port ($2.7B) - NEW":
    pilot_btc = st.slider("BTC Bond Tranche ($M)", 300, 1500, 800)
    pilot_gain = pilot_btc / 1000 * (1 + btc_cagr) ** years
    st.success(f"**$800M BTC Bond → ${pilot_gain:.1f}B by 2045**")
    st.info("SADC trade -50% cost | +2.5M jobs | **Integrate Africa**")

elif proj == "Nigeria Export Mfg Zones ($300M+) - NEW":
    pilot_fdi = st.slider("Crypto FDI Tranche ($M)", 50, 500, 150)
    pilot_return = pilot_fdi / 1000 * (1.25 ** 10)
    st.success(f"**$150M FDI → ${pilot_return:.1f}B in 10Y** (25% IRR)")
    st.info("SME export hubs | +1M jobs | **Industrialize Africa**")

# Export
data = {"Year": years_list, "BTC Value ($B)": btc_curve}
df = pd.DataFrame(data)
csv = df.to_csv(index=False)
st.download_button("Download BTC Forecast (CSV)", csv, "ail2045_forecast.csv")

st.markdown("---")
st.caption("AIL-2045 Crypto Calculator | For AIF 2025 | [x.ai/grok](https://x.ai/grok)")
