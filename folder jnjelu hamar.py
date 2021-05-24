def del_func(dir_):
    # check if dir_ is file we delete it
    if os.path.isfile(dir_):
        os.remove(dir_)
    # check if dir_ is not file but is empty we delete it
    elif not os.listdir(dir_):
        os.rmdir(dir_)
    # in other cases we try to get each element from dir_
    else:
        for path in os.listdir(dir_):
            # for each element we try to understand
            if os.path.isfile(path):  # we delete the file of dir_
                os.remove(path)
            # in other cases we create new directory ex. (DIR1/DIR2)
            else:
                new_dir_ = os.path.join(dir_, path)
                # so now we call our del_func with new argument DIR1/DIR2
                del_func(new_dir_)
        # and after all we delete the dir_ as well
        os.rmdir(dir_)