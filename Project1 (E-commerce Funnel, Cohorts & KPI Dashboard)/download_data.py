import kagglehub
import os
import shutil

def download_data():
    print("Downloading dataset...")
    try:
        # Download latest version
        path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
        print(f"Dataset downloaded to: {path}")
        
        # Create a local data directory if it doesn't exist
        local_data_dir = os.path.join(os.getcwd(), "data")
        os.makedirs(local_data_dir, exist_ok=True)
        
        # List files in the downloaded directory
        print("\nFiles in dataset:")
        files = os.listdir(path)
        for f in files:
            print(f" - {f}")
            # Optionally copy to local data dir for easier access
            # src = os.path.join(path, f)
            # dst = os.path.join(local_data_dir, f)
            # shutil.copy2(src, dst)
            
        print(f"\nYou can find the data at: {path}")
        return path
    except Exception as e:
        print(f"Error downloading data: {e}")
        return None

if __name__ == "__main__":
    download_data()
