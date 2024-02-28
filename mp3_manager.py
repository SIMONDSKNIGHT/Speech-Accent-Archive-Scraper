import os

def delete_duplicate_mp3s(directory):
    mp3_files = [file for file in os.listdir(directory) if file.endswith('.mp3')]
    removed_files = []
    unremoved_files = []

    for mp3_file in mp3_files:
        if '_' in mp3_file:
            identifier = mp3_file.split('_')[0]
            if identifier+'.mp3' in mp3_files:
                #compare the filesizes
                file1 = os.path.join(directory, mp3_file)
                file2 = os.path.join(directory, identifier+'.mp3')
                if os.path.getsize(file1) == os.path.getsize(file2):
                    #move the files to a folder called duplicates
                    duplicate_directory = os.path.join(directory, 'duplicates')
                    os.makedirs(duplicate_directory, exist_ok=True)
                    os.rename(file1, os.path.join(duplicate_directory, mp3_file))

                    print(f"Removed {mp3_file} because it is a duplicate of {identifier}.mp3")
                    removed_files.append(mp3_file)
                else:
                    print(f"did not remove {mp3_file} because it is a different file size than {identifier}.mp3")
                    unremoved_files.append(mp3_file)
    return removed_files, unremoved_files

# Usage example
directory = '/Users/dagafed/Documents/GitHub/DISS/scraper_folder/mp3s'
if __name__ == "__main__":
    removed_files, unremoved_files =delete_duplicate_mp3s(directory)
    print(f"Removed files: {removed_files}")
    print(f"Unremoved files: {unremoved_files}")
