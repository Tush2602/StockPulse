import os
import sys

# Base Directory
CURRENT_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "../../.."))


# Data Directories
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
RAW_DATA_STOCK_DIR =os.path.join(RAW_DATA_DIR, "stock")
RAW_DATA_SENTIMENT_DIR =os.path.join(RAW_DATA_DIR, "sentiment")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
PROCESSED_DATA_STOCK_DIR = os.path.join(PROCESSED_DATA_DIR, "stock")
PROCESSED_DATA_SENTIMENT_DIR = os.path.join(PROCESSED_DATA_DIR, "sentiment")
EXTERNAL_DATA_DIR= os.path.join(os.path.join(DATA_DIR, "external"))
EXTERNAL_DATA_STOCK_DIR = os.path.join(EXTERNAL_DATA_DIR, "stock")
EXTERNAL_DATA_SENTIMENT_DIR = os.path.join(EXTERNAL_DATA_DIR, "sentiment")


# Log Directories
LOGS_DIR  = os.path.join(BASE_DIR, "logs")

# Model Directory
MODEL_DIR = os.path.join(BASE_DIR, "model")

