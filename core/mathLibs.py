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
center of selection(with angle)

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
		if len(get_sel)!=0:
			if select is polyvtx or polyedge or polyface:
				if component="vtx":
					mesh = pm.listRelatives(pm.listRelatives(get_sel[0],p=1)[0],p=1)
					shape = pm.listRelatives(get_sel[0],p=1)[0]
					result = cmds.ls(cmds.polyListComponentConversion(get_sel[0],tv=1),fl=1)
				elif len(get_sel)>0 and component="edge":
					mesh = pm.listRelatives(pm.listRelatives(get_sel[0],p=1)[0],p=1)
					shape = pm.listRelatives(get_sel[0],p=1)[0]
					result = cmds.ls(cmds.polyListComponentConversion(get_sel[0],te=1),fl=1)
				elif component="face":
					mesh = pm.listRelatives(pm.listRelatives(get_sel[0],p=1)[0],p=1)
					shape = pm.listRelatives(get_sel[0],p=1)[0]
					result = cmds.ls(cmds.polyListComponentConversion(get_sel[0],tf=1),fl=1)
				
		return [mesh,shape,result]
		
	def is_component(self,sel_list):
		is_comp = []
		for sel in sel_list:
			if ".vtx[" in sel:
				if "vtx" not in is_comp:
					is_comp.append("vtx")
				is_comp.append(sel)
			elif ".e[" in sel:
				if "edge" not in is_comp:
					is_comp.append("edge")
				is_comp.append(sel)
			elif ".f[" in sel:
				if "face" not in is_comp:
					is_comp.append("face")
				is_comp.append(sel)
			elif ".map[" in sel:
				if "uv" not in is_comp:
					is_comp.append("uv")
				is_comp.append(sel)
		if len(is_comp[1:]) == len(sel_list):
			return is_comp[0]
