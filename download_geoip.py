import os
import tarfile
import requests
from pathlib import Path

def download_geolite2_database():
    # Create geoip directory if it doesn't exist
    geoip_dir = Path('geoip')
    geoip_dir.mkdir(exist_ok=True)
    
    # URL for the GeoLite2 Country database (this is a direct link to a specific version)
    url = "https://raw.githubusercontent.com/P3TERX/GeoLite.mmdb/download/GeoLite2-Country.mmdb"
    
    # Download the database
    print("Downloading GeoLite2 Country database...")
    response = requests.get(url)
    
    if response.status_code == 200:
        # Save the database
        database_path = geoip_dir / 'GeoLite2-Country.mmdb'
        with open(database_path, 'wb') as f:
            f.write(response.content)
        print(f"Database downloaded successfully to {database_path}")
    else:
        print("Failed to download the database")

if __name__ == '__main__':
    download_geolite2_database() 