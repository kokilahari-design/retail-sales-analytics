import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def upload_to_hdfs(local_file):

    hdfs_dir = "/data/retail/raw/"
    try:
        command = ["hdfs", "dfs", "-put", "-f", local_file, hdfs_dir]
        subprocess.run(command, check=True)
        logging.info(f"{local_file} uploaded to HDFS {hdfs_dir}")
        return True
    except subprocess.CalledProcessError as e:
        logging.error("HDFS upload failed")
        raise e

