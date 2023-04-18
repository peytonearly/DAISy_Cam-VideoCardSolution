from pixy2 import pixy2

pixy = pixy2.Pixy2()
pixy.set_max_blocks(5)

while True:
    num_blocks = pixy.get_num_blocks()
    if num_blocks > 0:
        blocks = pixy.get_blocks()
        for block in blocks:
            print("Block Type:", block.type)
            print("Block X:", block.x)
            print("Block Y:", block.y)