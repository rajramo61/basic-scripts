"""
==============
Finding Files:
==============
For this problem, the goal is to write code for finding all files under a directory
(and all directories beneath it) that end with ".c"

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h

Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)
os.path.isfile(path)
os.listdir(directory)
os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily.
However, for this problem you are not allowed to use os.walk().
"""
import os
from pathlib import Path


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    my_files_ending_extn_in_c = []
    lookup_dirs = set()
    lookup_dirs.add(path)
    # Tail recursion
    return find_local_files(suffix, my_files_ending_extn_in_c, lookup_dirs)


def find_local_files(suffix, my_files_ending_extn_in_c, lookup_dirs):
    if len(lookup_dirs) == 0:
        return my_files_ending_extn_in_c
    local_dirs = set()
    for directory in lookup_dirs:
        # delete directory
        current_dir_files = os.listdir(directory)
        for name in current_dir_files:
            file_or_dir = Path(directory + '/' + name)
            if os.path.isfile(file_or_dir) and name.endswith(suffix):
                my_files_ending_extn_in_c.append(file_or_dir)
            if os.path.isdir(file_or_dir):
                local_dirs.add(str(file_or_dir))
    # Clean up processed directories
    lookup_dirs.clear()
    # Add the new directories
    lookup_dirs = local_dirs
    return find_local_files(suffix, my_files_ending_extn_in_c, lookup_dirs)


files = find_files('.c', '/Users/rajeshdwivedi/Downloads/testdir/')
for file in files:
    print(file)


"""
I have attempted the solution using Tail recursion.
As we need to print all the files with suffix '.c' and there is nothing which is repeated as the 
directories and the files are unknown so we can not use memoization.

Time Complexity: O(2^n) where n is the maximum depth 
Space complexity: O(n) At one time there could be maximum n (maximum directory depth) 
    function stacks at a time.
"""