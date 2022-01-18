import csv
import os

class Top30CSVGenerator:

    def generate_top_30_csv(self, top_30_array, csv_file_location=os.getcwd().replace("\\","/") + '/Flask/Downloads/', file_name='ItJobsWatchTop30.data', headers_array=None):
        with open(csv_file_location + file_name, 'w+', newline='') as top30csv:
            writer = csv.writer(top30csv)
            if headers_array is not None:
                writer.writerow(headers_array)
            writer.writerows(top_30_array[0:30])


if __name__ == '__main__':
    print()
