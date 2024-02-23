import os

class DiffHistorySupport:

    name = ["DIFF_HISTORY_SUPPORT"]

    def on_file_moved_to_other_project(self,
        old_filename,
        new_filename):

        old_history_file = get_old_history_filename(old_filename)        
        if os.path.exists(old_history_file):
            new_history_file = make_new_history_filename(new_filename)
            os.rename(old_history_file, new_history_file)

    def on_file_renamed(self,
        old_filename,
        new_filename):

        old_history_file = get_old_history_filename(old_filename)  
        if os.path.exists(old_history_file):
            renamed_history_file = make_new_history_filename(new_filename)
            os.rename(old_history_file, renamed_history_file)

def get_old_history_filename(filename):
    return os.path.join(
        os.path.dirname(filename), 
        '_diff',
        os.path.basename(filename) + '.diff')

def make_new_history_filename(filename):
    if not os.path.exists(os.path.join(
        os.path.dirname(filename),
        '_diff')):
        os.mkdir(os.path.join(os.path.dirname(filename), '_diff'))
    return os.path.join(
        os.path.dirname(filename),
        '_diff',
        os.path.basename(filename) + '.diff')

urtext_extensions=[DiffHistorySupport]