
import pandas as pd
import sys
import os

def main(directory):
    # ファイルパスを作成
    workout_file = os.path.join(directory, 'Workout.csv')
    heartrate_file = os.path.join(directory, 'HeartRate.csv')

    # ファイルの存在確認
    if not os.path.exists(workout_file) or not os.path.exists(heartrate_file):
        print("Workout.csv または HeartRate.csv が指定のディレクトリに存在しません。")
        return

    # CSVファイルを読み込む
    workout_df = pd.read_csv(workout_file)
    heartrate_df = pd.read_csv(heartrate_file)

    # 日付をdatetime型に変換
    workout_df['startDate'] = pd.to_datetime(workout_df['startDate'])
    workout_df['endDate'] = pd.to_datetime(workout_df['endDate'])
    heartrate_df['startDate'] = pd.to_datetime(heartrate_df['startDate'])

    # ワークアウトごとに心拍データを抽出
    for i, workout in workout_df.iterrows():
        workout_start = workout['startDate']
        workout_end = workout['endDate']
        
        # 心拍データをフィルタリング
        filtered_heartrate = heartrate_df[
            (heartrate_df['startDate'] >= workout_start) &
            (heartrate_df['startDate'] <= workout_end)
        ]
        
        # 新規でディレクトリを作成
        output_dir = os.path.join(directory, 'split_heartrate')
        os.makedirs(output_dir, exist_ok=True) 

        # ファイル名を作成
        output_file = os.path.join(output_dir, f'heartrate_workout_{i+1}.csv')
        
        # フィルタリング結果を保存
        if not filtered_heartrate.empty:
            filtered_heartrate.to_csv(output_file, index=False)
            print(f"Workout {i+1}: データを '{output_file}' に保存しました。")
        else:
            print(f"Workout {i+1}: この期間に心拍データはありません。")

if __name__ == "__main__":
    # コマンドライン引数を確認
    if len(sys.argv) != 2:
        print("使用法: python split_by_workout.py <directory>")
        sys.exit(1)

    # ディレクトリを取得
    directory = sys.argv[1]
    main(directory)
