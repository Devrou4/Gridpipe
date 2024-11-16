import os.path
import urllib.request
import zipfile


class GameFetch:
    def __init__(self, games):
        self.games = games
        self.row = None
        self.file_name = None

    def download_file(self, url, row):
        self.row = row

        try:
            # Use urllib.request.urlretrieve with a built-in progress report
            self.file_name = os.path.basename(url)
            download_path = os.path.join(os.path.abspath('./games'), self.file_name)
            print(f'Downloading {self.file_name}')
            urllib.request.urlretrieve(url, download_path, reporthook=self.download_progress)
        except Exception as e:
            print(e)
            return False
        try:
            self.install_game(download_path)
        except zipfile.BadZipfile:
            print("\nCorrupted zip or non-zip file")
            if os.path.exists(download_path):
                os.remove(download_path)
            return False
        except zipfile.error:
            print(zipfile.error)
        except Exception as e:
            print(e)
        return True


    def install_game(self, zip_path):

        install_path = os.path.abspath("games")

        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(install_path)

        if os.path.exists(zip_path):
            os.remove(zip_path)
        print('extracted game data')

    def download_progress(self, block_num, block_size, total_size):
        if total_size > 0:  # Make sure total_size is greater than zero
            downloaded = block_num * block_size
            percent = (downloaded / total_size) * 100

            self.games.item(self.row, 1).setText(f"\rDownloaded: {percent:.2f}%")

            print(f"\rDownloaded: {percent:.2f}%", end="", flush=True)

        else:
            self.games.item(self.row, 1).setText(f"\rDownloading...")
            print("\rDownloading...", end="", flush=True)
