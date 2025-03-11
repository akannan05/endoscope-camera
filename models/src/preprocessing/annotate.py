import json

"""
for simplicity, we will only examine polyps
class # for polyp: 0
yolo needs a specific format for its in built models

this script converts the JSON provided by KVASIR into said format
"""


def parse_data():
    with open('kavsir_bboxes.json', 'r') as file:
        data = json.load(file)
    image_list = []
    for image_id in data.items():
        image_list.append(image_id)
    
    return image_list

def parse_entry(image_dict):
    """
        input: dictionary associated with a specific image ID
        output: list of strings, corresponding to the normalized bboxes of polyps in
        image
    """

    h = image_dict['height']
    w = image_dict['width']

    # note that the bbox entry for this json is a tuple

    bboxes = image_dict['bbox']

    bbox_strs = []

    for d in bboxes: # for simplicity we'll just ignore label (since they are all 0)
        bbox_dim = []
        bbox_dim.append(d['xmin'])
        bbox_dim.append(d['ymin'])
        bbox_dim.append(d['xmax'])
        bbox_dim.append(d['ymax'])

        bbox_strs.append(convert_image_coords(h, w, bbox_dim))

    return bbox_strs

def convert_image_coords(h, w, bbox_dim):
    """
        input: height + width of an image, and the bbox dimensions (in pixels)
        output: 0-1 normalized coordinates
    """

    xmin = bbox_dim[0]/w
    xmax = bbox_dim[2]/w

    ymin = bbox_dim[1]/h
    ymax = bbox_dim[3]/h

    xcenter = (xmax + xmin)/2
    ycenter = (ymax + ymin)/2

    bwidth = xmax-xmin
    bheight = ymax-ymin

    return "0 " + format(xcenter, '.7f') + " " + format(ycenter, '.7f') + " " + format(bwidth, '.7f') + " " + format(bheight, '.7f')

def write_to_txt(imageID, bbox_strs):
    fileToCreate = "labels/" + imageID + ".txt"

    f = open(fileToCreate, "w")

    for s in bbox_strs:
        f.write(s+'\n')

def main():
    image_list = parse_data()

    for i in range(1000):
        write_to_txt(image_list[i][0], parse_entry(image_list[i][1]))
    

if __name__ == "__main__":
    main()
