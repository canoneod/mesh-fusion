import os
import argparse
import ntpath
import common
# added
import pymeshlab as ml

class Simplification:
    """
    Perform simplification of watertight meshes.
    """

    def __init__(self):
        """
        Constructor.
        """

        parser = self.get_parser()
        self.options = parser.parse_args()
        self.simplification_script = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'simplification.mlx')

    def get_parser(self):
        """
        Get parser of tool.

        :return: parser
        """

        parser = argparse.ArgumentParser(description='Scale a set of meshes stored as OFF files.')
        parser.add_argument('--in_dir', type=str, help='Path to input directory.')
        parser.add_argument('--out_dir', type=str, help='Path to output directory; files within are overwritten!')

        return parser

    def read_directory(self, directory):
        """
        Read directory.

        :param directory: path to directory
        :return: list of files
        """

        files = []
        for filename in os.listdir(directory):
            files.append(os.path.normpath(os.path.join(directory, filename)))

        return files

    def run(self):
        """
        Run simplification.
        """

        assert os.path.exists(self.options.in_dir)
        common.makedir(self.options.out_dir)
        files = self.read_directory(self.options.in_dir)

        # changed
        for filepath in files:
            ms = ml.MeshSet()
            ms.load_new_mesh(filepath)
            ms.load_filter_script(self.simplification_script)
            ms.apply_filter_script()
            ms.save_current_mesh(os.path.join(self.options.out_dir, ntpath.basename(filepath)))

if __name__ == '__main__':
    app = Simplification()
    app.run()
