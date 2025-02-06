import pandas as pd
import geopandas as gpd
import folium

def create_nz_poc_map(df, map_filename="nz_poc_map.html", zoom_start=7):  # Adjusted zoom
    """Creates an interactive map of POC locations on a base map of New Zealand.

    Args:
        df (pd.DataFrame): DataFrame with POC data. Must include 'POC code', 'NZTM easting',
                           'NZTM northing', and optionally 'Island' or other relevant columns.
        map_filename (str, optional): Filename to save the map. Defaults to "nz_poc_map.html".
        zoom_start (int, optional): Initial zoom level. Defaults to 7 (suitable for NZ).
    """

    if 'NZTM easting' not in df.columns or 'NZTM northing' not in df.columns:
        print("Error: 'NZTM easting' and 'NZTM northing' columns are required.")
        return

    try:
        # 1. Create GeoDataFrame:
        # gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['NZTM easting'], df['NZTM northing']), crs="EPSG:2193")

        # 2. Load New Zealand Shapefile (or GeoJSON):
        # *This is the crucial step* - replace with the path to your NZ shapefile or GeoJSON file.
        nz_shapefile = "../data/raw/POCs/new_zealand_New_Zealand_Boundary_MAPOG/new_zealand_New_Zealand_Boundary.shp"  # <--- **IMPORTANT: Put the correct file path here!**
        try:
            nz = gpd.read_file(nz_shapefile)
        except Exception as e:
            print(f"Error loading NZ shapefile: {e}. Make sure the path is correct and the file exists.")
            return

        # 3. Calculate Map Center (using NZ shapefile):
        bounds = nz.total_bounds  # Use NZ bounds for centering
        center_lat = (bounds[1] + bounds[3]) / 2
        center_lon = (bounds[0] + bounds[2]) / 2

        # 4. Create Folium Map (using a tile layer suitable for NZ):
        m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom_start, tiles="OpenStreetMap") # or "Stamen Terrain"

        # 5. Add New Zealand outline:
        folium.GeoJson(nz).add_to(m) # Add NZ shapefile to the map

        # 6. Add POC Markers with Popups:
        # for index, row in gdf.iterrows():
        #     popup_text = f"POC Code: {row['POC code']}"
        #     if 'Island' in row:
        #         popup_text += f"<br>Island: {row['Island']}"
        #     popup = folium.Popup(popup_text, max_width=300)

        #     folium.CircleMarker(
        #         location=[row.geometry.y, row.geometry.x],
        #         radius=5,
        #         color="blue",
        #         fill=True,
        #         fill_color="blue",
        #         fill_opacity=0.6,
        #         popup=popup,
        #     ).add_to(m)

        # 7. Save Map:
        m.save(map_filename)
        print(f"Map saved to {map_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")



# Example usage (in your main script):
try:
    df = pd.read_csv('../data/raw/POCs/Network_supply_points_table_20250206234023.csv', on_bad_lines='skip', encoding='utf-8')
    df = df.dropna(subset=['NZTM easting', 'NZTM northing'])  # Removes rows with NaN in either column
except UnicodeDecodeError:
    df = pd.read_csv('../data/raw/POCs/Network_supply_points_table_20250206234023.csv', on_bad_lines='skip', encoding='latin-1')
    df = df.dropna(subset=['NZTM easting', 'NZTM northing'])  # Removes rows with NaN in either column

create_nz_poc_map(df, map_filename="nz_poc_map.html")
