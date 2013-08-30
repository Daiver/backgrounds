import os, sys, random

def_dir = '/home/daiver/backgrounds/.'
def setBG(path):
    os.system('feh --bg-max %s' % path)

def test_name(path):
    txt = path.lower()[-4:]
    return txt in ['.jpg', '.png', 'bmp']

if __name__ == '__main__':
    fls = [os.path.join(def_dir, x) for x in filter(test_name, os.listdir(def_dir))]
    name = fls[int(random.random()*len(fls))]
    setBG (name)
