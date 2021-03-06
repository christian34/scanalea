from openalea.plantgl.all import *
from scanalea import segmentation as seg
from scanalea.codecs import read, ply
import numpy as np

from time import time

fn = '/media/pradal/DONNEES/pradal/data/plantscan/segmented/segmentedMesh.vtk'
fn = '/media/pradal/DONNEES/pradal/data/plantscan/segmented/segmentedMesh_manualseg.vtk'
scene = read(fn)
Viewer.display(scene)

scene1, stems, leaves, coords = seg.organs(scene)


"""
from scanalea.light import caribu, display, turtle

caribu_scene, res = caribu(scene, source=turtle(16))
display(scene, res)
"""

leaves_data = '/media/pradal/DONNEES/pradal/data/plantscan/segmented3/leaves_data.csv'
g = seg.create_mtg(stems, leaves,coords, leaves_data=leaves_data)
Viewer.display(Scene(g.property('geometry').values()))

g = add_leaves_data(g,leaves_data)

"""
fn = '/media/pradal/DONNEES/pradal/data/plantscan/663_4_tp/FourTPsec_20130326_3199_663_res1280_full_vh_smoothed_textured.ply'
t1 = time()
scene = read(fn)
t2 = time()
print 'Case1 ', t2-t1
Viewer.display(scene)


fn = '/media/pradal/DONNEES/pradal/data/plantscan/663_4_tp/FourTPsec_20130326_3199_663_res1280_full_vh_smoothed_textured.ply'
c=ply.PlyCodecVTK()
t1 = time()
scene=c.read(fn)
t2 = time()
Viewer.display(scene)
print 'Case VTK ', t2-t1
t1=t2

"""

