import os

class MoveDiffWithFile:

    name = ["MOVE_FILE_WITH_DIFF"]

    def on_file_moved_to_other_project(self,
        old_filename,
        new_filename):

        old_history_file = os.path.join(
            os.path.dirname(old_filename), 
            '_diff',
            os.path.basename(old_filename))
        
        if os.path.exists(old_history_file):
            if not os.path.exists(os.path.join(
                os.path.dirname(new_filename),
                '_diff'
                )):
                os.mkdir(
                    os.path.join(os.path.dirname(new_filename), '_diff'))
            new_history_file = os.path.join(
                os.path.dirname(new_filename),
                '_diff',
                os.path.basename(new_filename) + '.diff')
            os.rename(old_history_file, new_history_file)

urtext_extensions=[MoveDiffWithFile]