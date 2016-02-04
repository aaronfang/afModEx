'''
This class definds several methords to make the math easier.

methords:
distance
pixel ratio
isDigits
isAlpha
isDash
average normal
sort
center
position
angle
random
shape
transform
material
vector
uv shell
UDIM

selection convert(to vtx,to edge,to face)
'''

import maya.cmds as cmds

class _math(object):
	def __init__(self):
		pass

	def distance(self,point1,point2):
		pass

    def scale_uv_by_ratio(self,tex_res,ratio):
        multi = 1
        cur_unit = cmds.currentUnit(q=True,f=True)
        if not cur_unit == "centimeter":
            if cur_unit == "meter":
                multi = 0.01
            elif cur_unit == "millimeter":
                multi = 10
            else:
                cmds.confirmDialog(t="sorry",button="ok",message="Only work on cm/m/mm unit.")
        multi = (multi*(8192/tex_res))/8
		unfold=0.0009765625*(ratio)
		scale_ratio = unfold*mult
        
        return scale_ratio
	
	def convert_seletion(self,cur_sel,component):
		get_sel = pm.ls(sl=1,fl=1)
		if len(get_sel)>0 and component="vtx"
			mesh = pm.listRelatives(pm.listRelatives(get_sel[0],p=1)[0],p=1)
			vtx = cmds.ls(cmds.polyListComponentConversion(get_sel[0],tv=1),fl=1)
		