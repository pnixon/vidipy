import argparse

class ArgParser:
    def __init__(self):
        parser = argparse.ArgumentParser(description="A simple script to demonstrate argparse usage.")

        parser.add_argument("-p", "--project", type=str, help="Project to build", required=False)
        parser.add_argument("-n", "--newProject", type=str, help="Create the folder structure for a new project", required=False)
        parser.add_argument("-v", "--verbose", action="store_true", help="Verbose log output")
        self.args = parser.parse_args()

        if self.args.verbose:
            print(f"Verbose mode is on.")
        
        if self.args.project == None and self.args.newProject == None:
            parser.print_help()
            exit(0)

    def get_args(self):
        return self.args
