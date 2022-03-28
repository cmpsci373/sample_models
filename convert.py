
import os 

def copy_obj_to_js(obj_fd, js_fd, obj_name):
    js_fd.write(f"let {obj_name}_model = `\n")
    for line in obj_fd:
        js_fd.write("    " + line)
    js_fd.write('`;')

def main():
    cwd = os.getcwd() 
    obj_path = os.path.join(cwd, "objects")
    js_path = os.path.join(cwd, "js")

    obj_fnames = [f for f in os.listdir(obj_path) \
        if os.path.isfile(os.path.join(obj_path, f))]
    
    for obj_fname in obj_fnames: 
        obj_fd = open(os.path.join(obj_path, obj_fname), 'r')

        obj_name = obj_fname.split('.')[0]
        js_fd = open(os.path.join(js_path, obj_name + '.js'), 'a+')

        copy_obj_to_js(obj_fd, js_fd, obj_name)

        # cleanup 
        obj_fd.close()
        js_fd.close()

if __name__ == "__main__":
    main()
