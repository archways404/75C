# Generating a 1GB text file filled with repetitive data to ensure large size

file_path = "./data/1gb.txt"
chunk_size = 1024 * 1024  # 1 MB
total_size = 1024 * 1024 * 1024  # 1 GB
data = "This is a test line to fill the file.\n"  # Example text line
chunk = data * (chunk_size // len(data))  # Generate 1 MB worth of lines

with open(file_path, "w") as file:
    for _ in range(total_size // chunk_size):
        file.write(chunk)
