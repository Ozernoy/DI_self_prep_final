from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------

l_1 = [chr(97+i) for i in range(26)]
l_2 = l_1.copy()
l_3 = [f"{i}{j}" for i in l_1 for j in l_2]

for guess in l_3:
    secret_password = guess + 'bcmpda'
    if unzip_with_7z(zip_file_path, dest_path, secret_password):
        print(f"The correct password is: {secret_password}")
        break
    else:
        print(f"Failed with password: {secret_password}")