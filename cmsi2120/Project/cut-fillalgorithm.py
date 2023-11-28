import pandas as pd

def calculate_cut_fill(csv_file):
    # Load the CSV file containing elevation data
    df = pd.read_csv(csv_file)

    # Assuming the CSV has columns 'Station' and 'Elevation'
    station_column = 'Station'
    elevation_column = 'Elevation'

    # Create a design surface (you may obtain this from engineering specifications)
    design_surface_elevation = 100.0  # Replace with the desired elevation

    # Calculate cut and fill volumes
    cut_volume = 0.0
    fill_volume = 0.0

    for i in range(1, len(df)):
        # Calculate the average elevation of each section
        avg_elevation = (df.at[i - 1, elevation_column] + df.at[i, elevation_column]) / 2.0

        # Calculate the cut or fill volume for each section
        volume = (design_surface_elevation - avg_elevation) * (df.at[i, station_column] - df.at[i - 1, station_column])

        # Update cut and fill volumes based on the volume sign
        if df.at[i, elevation_column] < design_surface_elevation:
            cut_volume += volume
        else:
            fill_volume += volume

    return cut_volume, fill_volume

# Example usage
csv_file_path = 'path/to/your/elevation_data.csv'
cut_volume, fill_volume = calculate_cut_fill(csv_file_path)

print(f"Cut Volume: {cut_volume} cubic units")
print(f"Fill Volume: {fill_volume} cubic units")
