import os
import json
import csv
import pickle


class DirectoryWalker:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.results = []

    def walk_directory(self):
        for root, dirs, files in os.walk(self.dir_path):
            for name in files:
                full_path = os.path.join(root, name)
                self.results.append({
                    "parent_directory": root,
                    "is_file": True,
                    "name": name,
                    "size_in_bytes": os.path.getsize(full_path)
                })

            for name in dirs:
                full_path = os.path.join(root, name)
                self.results.append({
                    "parent_directory": root,
                    "is_file": False,
                    "name": name,
                    "size_in_bytes": self.get_size(full_path)
                })

    def get_size(self):
        total = 0
        for dir_path, dir_names, file_names in os.walk(self.dir_path):
            for f in file_names:
                fp = os.path.join(dir_path, f)
                total += os.path.getsize(fp)
        return total

    def save_to_json(self, filename):
        with open(filename, "w") as json_file:
            json.dump(self.results, json_file)

    def save_to_csv(self, filename):
        with open(filename, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
            writer.writeheader()
            writer.writerows(self.results)

    def save_to_pickle(self, filename):
        with open(filename, "wb") as pickle_file:
            pickle.dump(self.results, pickle_file)


if __name__ == '__main__':
    walker = DirectoryWalker('.')
    walker.walk_directory()
    walker.save_to_json("output.json")
    walker.save_to_csv("output.csv")
    walker.save_to_pickle("output.pickle")
