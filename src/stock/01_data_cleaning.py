# import os
# import time
# import pandas as pd
# from datetime import datetime, timedelta
# from twelvedata import TDClient
# from src.logger import logger  # your logger
# # from src.exception import CustomException  # optional

# API_KEY = "<YOUR_API_KEY>"
# td = TDClient(API_KEY)

# symb = SETTINGS["data"]["n_symbol"]
# interval = SETTINGS["data"]["interval"]  # "1min", "5min", ...
# days = SETTINGS["data"]["days"]
# initial_size = SETTINGS["data"].get("initial_fetch_size", 5000)
# realtime_size = SETTINGS["data"].get("realtime_fetch_size", 1)
# save_path = SETTINGS["data"].get("save_path", f"data/raw/stock/{symb}.csv")

# def interval_seconds(interval_str: str) -> int:
#     mapping = {"1min":60, "5min":300, "15min":900, "30min":1800, "60min":3600, "1day":86400}
#     return mapping.get(interval_str, 60)

# def fetch_historical():
#     end = datetime.now()
#     start = end - timedelta(days=days)
#     obj = td.time_series(
#         symbol=symb,
#         interval=interval,
#         start_date=start.strftime("%Y-%m-%d %H:%M:%S"),
#         end_date=end.strftime("%Y-%m-%d %H:%M:%S"),
#         outputsize=initial_size
#     )
#     df = obj.as_pandas()
#     df.index = pd.to_datetime(df.index)
#     df = df.sort_index()
#     return df

# def fetch_latest(n=realtime_size):
#     """Fetch last n bars (no start_date) — returns pandas DataFrame indexed by timestamp."""
#     obj = td.time_series(symbol=symb, interval=interval, outputsize=n)
#     df = obj.as_pandas()
#     df.index = pd.to_datetime(df.index)
#     df = df.sort_index()
#     return df

# def ensure_dir_for_file(path):
#     os.makedirs(os.path.dirname(path), exist_ok=True)

# # main loop
# try:
#     ensure_dir_for_file(save_path)

#     if os.path.exists(save_path):
#         df = pd.read_csv(save_path, index_col=0, parse_dates=True)
#         df.index = pd.to_datetime(df.index)
#         logger.info(f"Loaded existing data, {len(df)} rows, last_ts={df.index.max()}")
#     else:
#         df = fetch_historical()
#         df.to_csv(save_path)
#         logger.info(f"Fetched historical {len(df)} rows and saved to {save_path}")

#     last_ts = df.index.max() if not df.empty else None
#     sleep_seconds = interval_seconds(interval)

#     while True:
#         try:
#             new_df = fetch_latest(n=realtime_size)

#             # keep only bars strictly after last_ts
#             if last_ts is not None:
#                 new_df = new_df[new_df.index > last_ts]

#             if not new_df.empty:
#                 df = pd.concat([df, new_df])
#                 # drop exact-duplicate timestamps (keep last)
#                 df = df[~df.index.duplicated(keep='last')]
#                 df = df.sort_index()
#                 df.to_csv(save_path)
#                 last_ts = df.index.max()
#                 logger.info(f"Appended {len(new_df)} new bars; last_ts={last_ts}")
#             else:
#                 logger.debug("No new bars returned by API")

#         except Exception as e:
#             # handle API errors, transient problems
#             logger.exception("Error while fetching latest bars")
#             # optionally add exponential backoff, or continue
#         # wait until next interval
#         time.sleep(sleep_seconds)

# except Exception as e:
#     logger.exception("Realtime fetcher stopped due to exception")
#     raise
