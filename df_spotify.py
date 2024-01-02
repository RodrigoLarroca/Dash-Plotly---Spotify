from librerias import pd, gspread
from base_de_datos import client

spreadsheet_id = "1bjaPIweetryTORHAHOs8_MWZVXv4LZUqLNIoQO0YceM"
sheet = client.open_by_key(spreadsheet_id).worksheet("spotify-2023")
data = sheet.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
df['in_spotify_playlists'] = pd.to_numeric(df['in_spotify_playlists'], errors='coerce')