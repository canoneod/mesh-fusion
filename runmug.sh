
# change path to right one 
source_path = "/mnt/c/Users/Kim/Desktop/ShapeNetCore.v2/03797390"

while read line || [ -n "$line" ] ; do
    echo "Currently working on $line"
    input_path = "$source_path/$line/model"
    output_path = "mugs/$line"
    echo "converting and scaling"
    #python 1_scale.py --in_dir=examples/0_in/ --out_dir=examples/1_scaled/
    echo "$input_path/"

    echo "depth map & watertight meshes"
    #python 2_fusion.py --mode=render --in_dir=examples/1_scaled/ --depth_dir=examples/2_depth/ --out_dir=examples/2_watertight/ --n_views 200

    echo "processing watertight meshes $output_path"
    #python 3_simplify.py --in_dir=examples/2_watertight/ --out_dir=examples/3_out/
done < valid_mugID.txt