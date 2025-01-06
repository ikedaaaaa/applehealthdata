import subprocess
import sys
def main(argv):
    # 最初のスクリプトを実行
    print("Running applehealthdata.py...")
    subprocess.run(["python", "applehealthdata.py",argv])

    # 次のスクリプトを実行
    print("Running split_by_workout.py...")
    dir = "/".join(argv.split("/")[:-1])
    subprocess.run(["python", "split_by_workout.py",dir])

if __name__ == "__main__":
    main(sys.argv[1])
