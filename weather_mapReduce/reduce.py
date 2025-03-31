import pandas as pd
def reducer(mapped_data):
    grouped = mapped_data.groupby("year")["tavg"].apply(list)  # Group by year, keep all tavg values
    avg_temps = mapped_data.groupby("year")["tavg"].mean()  # Compute mean tavg per year
    
    result_df = pd.DataFrame({"tavg_values": grouped, "avg_tavg": avg_temps})
    
    return result_df


