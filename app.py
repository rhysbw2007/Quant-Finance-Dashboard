from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = Path(__file__).parent / "data" / "prices.csv"


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    prepared = df.sort_values(["ticker", "date"]).copy()
    prepared["return"] = prepared.groupby("ticker")["close"].pct_change()
    prepared["vol_30d"] = prepared.groupby("ticker")["return"].transform(
        lambda s: s.rolling(window=min(30, len(s)), min_periods=2).std(ddof=0) * (252 ** 0.5)
    )
    prepared["vol_30d"] = prepared["vol_30d"].fillna(0.0)
    return prepared


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    return prepare_data(df)


def compute_metrics(df: pd.DataFrame, ticker: str) -> tuple[float, float, float]:
    ticker_df = df[df["ticker"] == ticker].copy()
    ticker_df = ticker_df.dropna(subset=["close", "return"]).copy()
    if ticker_df.empty:
        return 0.0, 0.0, 0.0

    start_close = ticker_df["close"].iloc[0]
    end_close = ticker_df["close"].iloc[-1]
    total_return = ((end_close / start_close) - 1) * 100 if start_close else 0.0

    volatility = ticker_df["return"].std(ddof=0) * (252**0.5) * 100
    sharpe = (
        ticker_df["return"].mean() / ticker_df["return"].std(ddof=0)
        if ticker_df["return"].std(ddof=0)
        else 0.0
    )
    return total_return, volatility, sharpe


st.set_page_config(page_title="Quant Finance Dashboard", layout="wide")
st.title("Quant Finance Dashboard")
st.caption("A lightweight Python dashboard for tracking market performance and volatility.")

df = load_data(DATA_PATH)

if df.empty:
    st.error("No market data was found. Please check the data file.")
    st.stop()

all_tickers = sorted(df["ticker"].unique())
selected_ticker = st.sidebar.selectbox("Ticker", all_tickers)

start_date = st.sidebar.date_input(
    "Start date",
    value=df.loc[df["ticker"] == selected_ticker, "date"].min().date(),
)
end_date = st.sidebar.date_input(
    "End date",
    value=df.loc[df["ticker"] == selected_ticker, "date"].max().date(),
)

filtered = df[(df["ticker"] == selected_ticker) & (df["date"].dt.date >= start_date) & (df["date"].dt.date <= end_date)].copy()

if filtered.empty:
    st.warning("No data available for the selected date range.")
    st.stop()

total_return, volatility, sharpe = compute_metrics(filtered, selected_ticker)

col1, col2, col3 = st.columns(3)
col1.metric("Total Return (%)", f"{total_return:.2f}")
col2.metric("Annualized Volatility (%)", f"{volatility:.2f}")
col3.metric("Sharpe Ratio", f"{sharpe:.2f}")

fig_line = px.line(filtered, x="date", y="close", title=f"{selected_ticker} Close Price")
st.plotly_chart(fig_line, width="stretch")

fig_vol = px.line(filtered, x="date", y="vol_30d", title=f"{selected_ticker} 30-Day Volatility")
st.plotly_chart(fig_vol, width="stretch")

st.dataframe(filtered[["date", "close", "return", "vol_30d"]].tail(10), use_container_width=True)
