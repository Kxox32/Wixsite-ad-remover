import os
from bs4 import BeautifulSoup

# The folder where your downloaded site files are located
target_folder = '.'

def remove_specific_wix_ad():
    files_modified = 0
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            if file.endswith(".html") or file.endswith(".htm"):
                file_path = os.path.join(root, file)
                
                # Load the file
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    soup = BeautifulSoup(content, 'html.parser')

                # Find the div with the specific ID 'WIX_ADS'
                wix_ad_div = soup.find('div', id='WIX_ADS')

                if wix_ad_div:
                    # Deletes the div and everything inside it (the link, etc.)
                    wix_ad_div.decompose()
                    
                    # Save the cleaned file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    print(f"Removed ad from: {file}")
                    files_modified += 1

    print(f"Process finished. {files_modified} files were cleaned.")

if __name__ == "__main__":
    remove_specific_wix_ad()
