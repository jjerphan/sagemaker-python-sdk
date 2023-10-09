def is_likely_a_pandas_df(X):
    """Return True if the X is likely a pandas dataframe."""
    return X.__class__.__name__ == "DataFrame" and hasattr(X, "columns") and hasattr(X, "iloc")
