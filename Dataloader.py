import laspy
import numpy as np 

class Dataloader:

    def __init__(self, path):
        try:
            self.infile = laspy.file.File(path, mode="r")
        except:
            print("Invalid path!")
            exit(1)

    '''
    X	X (x for scaled)	long[1] (4)
    Y	Y (y for scaled)	long[1] (4)
    Z	Z (z for scaled)	long[1] (4)
    Intensity	intensity	unsigned short[1] (2)
    (Flag Byte)	flag_byte	unsigned byte[1] (1)
    (Classification Byte)	raw_classification	unsigned byte[1] (1)
    User Data	user_data	unsigned char[1] (1)
    Point Source Id	pt_src_id	unsigned short[1] (2)
    GPS Time	gps_time	double[1] (8)
    '''
    def get_points(self):
        return self.infile.points
    
    def get_headers(self):
        return self.infile.header
    
    def get_coords(self):
        x = self.infile.X
        y = self.infile.Y
        z = self.infile.Z

        coord = [x,y,z]
        coord = np.array(coord).T
        return coord


def main():
    print(laspy.__version__)
    path = "./Data/4880E_54560N.las"
    dataloader = Dataloader(path)
    
    print("Point format id =", dataloader.get_headers().data_format_id)
    print("Point Scale Factor =", dataloader.get_headers().scale)
    print("Point offset =", dataloader.get_headers().offset)
    print(dataloader.get_headers().data_record_length)

    print("================")
    print("X, Y, Z, Intensity, Unknown, classification , unknown, unknown, PointSourceId, GPS Time")
    points = dataloader.get_points()
    print(points[1:5])
    print(dataloader.get_coords()[1:5])



if __name__ == "__main__":
    main()