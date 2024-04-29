# import os

# def delete_every_fifth_file(folder_path, prefix, total_files, file_extension):
#     # Iterate over the range of file indices and delete every 5th file
#     for i in range(1, total_files + 1):
#         if i % 5 != 0:
#             file_name = f"{prefix}{i}.{file_extension}"
#             file_path = os.path.join(folder_path, file_name)
#             #print(f"Checking: {file_path}")
#             try:
#                 os.remove(file_path)
#                 print(f"Deleted: {file_path}")
#             except Exception as e:
#                 print(f"Error deleting {file_path}: {e}")

# # Provide the path to the folder containing the files
# for prefix in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     folder_path = rf'aslsigndataset/asl_alphabet_train/asl_alphabet_train/{prefix}'
#     # Prefix for file 