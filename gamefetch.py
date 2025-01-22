import os.path
import urllib.request
import zipfile


class GameFetch:
    def __init__(self, games):
        self.games = games
        self.is_mod = None
        self.row = None
        self.file_name = None
        self.mod = None
        self.download_progress_counter = 0
        self.is_downloading = False

    def download_file(self, url, is_mod, row):

        self.row = int(row)
        self.is_mod = is_mod
        self.mod = str(self.is_mod).split('/')

        if self.is_downloading:
            print("Download already in progress.")
            self.games.item(self.row, 1).setText("Download already in progress.")
            return

        self.is_downloading = True

        if self.mod[0] == 'hl' and not os.path.exists(os.path.abspath('./games/Half-Life')):
            print('Half-Life not Installed')
            self.games.item(self.row, 1).setText("Install Half-Life")
            return
        else:
            pass

        try:
            # Use urllib.request.urlretrieve with a built-in progress report
            self.file_name = os.path.basename(url)
            download_path = os.path.join(os.path.abspath('./games'), self.file_name)
            print(f'Downloading {self.file_name}')
            urllib.request.urlretrieve(url, download_path, reporthook=self.download_progress)
        except Exception:
            self.games.item(self.row, 1).setText("Connection ERROR")
            return
        try:
            self.install_game(download_path)
        except zipfile.BadZipfile:
            print("\nCorrupted zip or non-zip file")
            self.games.item(self.row, 1).setText("Format ERROR")
            if os.path.exists(download_path):
                os.remove(download_path)
            return False
        except zipfile.error:
            print(zipfile.error)
        except Exception as e:
            print(f'\nERROR:{e}')
        return True

    def install_game(self, zip_path):

        if str(self.mod[0]) == 'hl' and os.path.exists(os.path.abspath('./games/Half-Life')):
            install_path = os.path.abspath(f'./games/Half-Life/{self.mod[1]}')
            print(f'\nHL mod detected: {self.mod[1]}')
        else:
            install_path = os.path.abspath("games")

        self.games.item(self.row, 1).setText("Installing...")
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(install_path)

        if os.path.exists(zip_path):
            os.remove(zip_path)
        print('extracted game data')

    def download_progress(self, block_num, block_size, total_size):
        if total_size > 0:  # Make sure total_size is greater than zero
            downloaded = block_num * block_size
            percent = (downloaded / total_size) * 100

            # Only update every 10 blocks (or any other threshold)
            self.download_progress_counter += 1
            if self.download_progress_counter % 50 == 0:  # Update every 50 blocks
                self.games.item(self.row, 1).setText(f"\rDownloaded: {percent:.2f}%")
                print(f"\rDownloaded: {percent:.2f}%", end="", flush=True)

            print(f"\rDownloaded: {percent:.2f}%", end="", flush=True)

        else:
            self.games.item(self.row, 1).setText(f"\rDownloading...")
            print("\rDownloading...", end="", flush=True)
