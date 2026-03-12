import subprocess
from data_genrator import generate_daily_sales_csv

def uploaded_to_hdfs():

    local_file = generate_daily_sales_csv()
    hdfs_dir = "/data/retail/raw/"
    command = f"hdfs dfs -put -f {local_file} {hdfs_dir}"
    subprocess.run(command, shell=True, check=True)
    print("File uploaded to HDFS")

