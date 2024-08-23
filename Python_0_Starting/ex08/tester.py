from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

print("test de ft_tqdm :")
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

print("test de tqdm :")
for elem in tqdm(range(333)):
    sleep(0.005)
print()
