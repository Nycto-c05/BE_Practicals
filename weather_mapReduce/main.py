from data_load import data_loading
from map import mapper
from reduce import reducer

if __name__ == "__main__":
    df = data_loading()
    print("Weather Data loaded\n")
    # print(df)

    mapped_data = mapper()
    print("Mapped Data loaded\n")
    # print(mapped_data)

    reduced_result = reducer(mapped_data)
    print("Reduced Data loaded\n")
    print(reduced_result.head())

    hottest_year = reduced_result["avg_tavg"].idxmax()
    coldest_year = reduced_result["avg_tavg"].idxmin()

    print(f"Hottest Year: {hottest_year} with avg temp {reduced_result.loc[hottest_year, 'avg_tavg']:.2f}°C")
    print(f"Coldest Year: {coldest_year} with avg temp {reduced_result.loc[coldest_year, 'avg_tavg']:.2f}°C")



