import maya.cmds as asdf

# polyCube: w = width, h = height, d = depth, sx = subdivisionsX, sz = subdivisionsZ, ax = axis, cuv = createUVs, ch = constructionHistory
# polyCylinder: r = radius, h = height, sx = subdivisionsX, sy = subdivisionsY, sz = subdivisionsZ, ax = axis, rcp = roundCap, cuv = createUVs, ch = constructionHistory
# move: r = relative
# rotate: r = relative, os = objectSpace, fo = forceOrderXYZ
# scale: ws = worldSpace, r = relative
# group: n = n***

# listRelatives

move_coords1 = [0,0,2.467181]
rotate_coords1 = [15,0,0]
scale_coords1 = [1.732995,1.732995,1.732995]

move_coords2 = [-8.452844,4.424261,-7.376775]
rotate_coords2 = [-36.24423,-26.732558,-26.602506]
scale_coords2 = [1.386358,1.386358,1.386358]

asdf.polyCube(w=1, h=1, d=1, sx=1, sz=1, ax=[0,1,0], cuv=4, ch=1)
asdf.move(move_coords1[0],move_coords1[1],move_coords1[2], r=True)
asdf.rotate(rotate_coords1[0],rotate_coords1[1],rotate_coords1[2], r=True, os=True, fo=True)
asdf.scale(scale_coords1[0],scale_coords1[1],scale_coords1[2], ws=True, r=True)

asdf.polyCylinder(r=1, h=2, sx=20, sy=1, sz=1, ax=[0,1,0], rcp=False, cuv=3, ch=1)
asdf.move(move_coords2[0],move_coords2[1],move_coords2[2], r=True)
asdf.rotate(rotate_coords2[0],rotate_coords2[1],rotate_coords2[2], r=True, os=True, fo=True)
asdf.scale(scale_coords2[0],scale_coords2[1],scale_coords2[2], ws=True, r=True)

asdf.select(clear=True)
asdf.group(n='group1', empty=True)
asdf.move(move_coords1[0],move_coords1[1],move_coords1[2], r=True)
asdf.rotate(rotate_coords1[0],rotate_coords1[1],rotate_coords1[2], r=True, os=True, fo=True)
asdf.scale(scale_coords1[0],scale_coords1[1],scale_coords1[2], ws=True, r=True)

asdf.select(clear=True)
asdf.group(n='group2', empty=True)
asdf.move(move_coords2[0],move_coords2[1],move_coords2[2], r=True)
asdf.rotate(rotate_coords2[0],rotate_coords2[1],rotate_coords2[2], r=True, os=True, fo=True)
asdf.scale(scale_coords2[0],scale_coords2[1],scale_coords2[2], ws=True, r=True)

asdf.parent('pCube1', 'group1')
asdf.parent('pCylinder1', 'group2')

asdf.rename('group1', 'pCube1_Grp')
asdf.rename('group2', 'pCylinder1_Grp')